#! /usr/bin/python
from WN_exp import *
import argparse
import json

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--config", help="path to parameter configuration file")
    parser.add_argument("--dimensions", type=int, default=20, help="number of dimensions in the embeddings")
    parser.add_argument("--epochs", type=int, default=500, help="number of epochs to train for")
    parser.add_argument("--regularisation", choices=["L1", "L2"], default="L1", help="type of regularisation")
    parser.add_argument("--margin", type=float, default=2, help="size of margin used in loss function")
    parser.add_argument("--learning-rate", type=float, default=0.01, help="learning rate used by SGD")
    parser.add_argument("--batch-size", type=int, default=64, help="number of triples in each batch")
    parser.add_argument("--output", default="WN18RR_TransE")

    args = parser.parse_args()

    if args.config:
        with open(args.config) as file:
            config = json.load(file)

        launch(
            op="TransE",
            dataset="WN18RR",
            ndim=config["dimensions"],
            nhid=config["dimensions"],
            totepochs=config["epochs"],
            neval=config["epochs"],
            simfn=config["regularisation"],
            marge=config["margin"],
            lremb=config["learning_rate"],
            lrparam=config["learning_rate"],
            savepath=config["output"],
            batch_size=config["batch_size"],
            test_all=10,
            datapath='../data/'
        )
    else:
        launch(
            op="TransE",
            dataset="WN18RR",
            simfn=args.regularisation,
            ndim=args.dimensions,
            nhid=args.dimensions,
            marge=args.margin,
            lremb=args.learning_rate,
            lrparam=args.learning_rate,
            totepochs=args.epochs,
            neval=args.epochs,
            savepath=args.output,
            batch_size=args.batch_size,
            test_all=10,
            datapath='../data/'
        )


if __name__ == "__main__":
    main()
