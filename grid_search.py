#! /usr/bin/python
import string
import argparse
import json
import itertools as it
import os.path

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("dataset", choices=["wn18rr", "fb15k237"])
    parser.add_argument("output", help="directory to put the configuration files")
    parser.add_argument("--dimensions", type=int, nargs="*", default=[50])
    parser.add_argument("--regularisation", nargs="*", choices=["L1", "L2"], default=["L2"])
    parser.add_argument("--margin", nargs="*", type=float, default=[0.5])
    parser.add_argument("--learning-rate", nargs="*", type=float, default=[0.1])
    parser.add_argument("--batch-size", nargs="*", type=int, default=[64])
    parser.add_argument("--epochs", nargs="*", type=int, default=[500])

    args = parser.parse_args()

    filtered_args = {key: value for key, value in vars(args).items()
                     if value is not None and key not in ["output", "dataset"]}

    keys, values = zip(*sorted(filtered_args.items()))

    if not os.path.exists(args.output):
        os.mkdir(args.output)

    script_paths = []

    for value in it.product(*values):
        config = dict(zip(keys, value))

        # Generate a unique key that will be used to name the config file, bash
        # script, and output directory.
        config_key = '-'.join(["{}-{}".format(key, value) for key, value in config.items()])

        # Path to the configuration file.
        config_path = os.path.abspath(os.path.join(args.output, config_key + ".json"))
        out_path = os.path.abspath(os.path.join(args.output, config_key + ".out"))
        script_path = os.path.abspath(os.path.join(args.output, config_key + ".sh"))

        # Add output directory to the configuration object.
        config["output"] = os.path.abspath("{}/{}".format(args.output, config_key))

        # Write the configuration file.
        with open(config_path, "w") as file:
            json.dump(config, file, indent=True, sort_keys=True)

        # Write the Bash script.
        with open(script_path, "w") as file:
            file.write(
                "./train.sh {} --config {} &> {}".format(
                    args.dataset,
                    config_path.replace(" ", "\ "),
                    out_path.replace(" ", "\ "),
                )
            )

        script_paths.append(script_path.replace(" ", "\ "))

    with open(os.path.join(args.output, "run.sh"), "w") as file:
        for script_path in script_paths:
            file.write("bash {}\n".format(script_path))

if __name__ == "__main__":
    main()
