#! /usr/bin/python
from FB15k_exp import *
import argparse
import json

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--config", help="path to parameter configuration file")
    parser.add_argument("--dimensions", type=int, default=50, help="number of dimensions in the embeddings")
    parser.add_argument("--epochs", type=int, default=500, help="number of epochs to train for")
    parser.add_argument("--regularisation", choices=["L1", "L2"], default="L2", help="type of regularisation")
    parser.add_argument("--margin", type=float, default=0.5, help="size of margin used in loss function")
    parser.add_argument("--learning-rate", type=float, default=0.01, help="learning rate used by SGD")
    parser.add_argument("--batch-size", type=int, default=64, help="number of triples in each batch")
    parser.add_argument("--output", default="FB15k237_TransE")

    args = parser.parse_args()

    if args.config:
        with open(args.config) as file:
            config = json.load(file)

        launch(
            op="TransE",
            dataset="FB15k237",
            ndim=config["dimensions"],
            nhid=config["dimensions"],
            totepochs=config["epochs"],
            simfn=config["regularisation"],
            marge=config["margin"],
            lremb=config["learning_rate"],
            lrparam=config["learning_rate"],
            savepath=config["output"],
            batch_size=config["batch_size"],
            test_all=10,
            neval=1000,
            datapath='../data/'
        )
    else:
        launch(
            op="TransE",
            dataset="FB15k237",
            simfn=args.regularisation,
            ndim=args.dimensions,
            nhid=args.dimensions,
            marge=args.margin,
            lremb=args.learning_rate,
            lrparam=args.learning_rate,
            totepochs=args.epochs,
            savepath=args.output,
            batch_size=args.batch_size,
            test_all=10,
            neval=1000,
            datapath='../data/'
        )


if __name__ == "__main__":
    main()
