#!/usr/bin/env python3

from argparse import ArgumentParser, FileType

import pandas as pd


def get_args():
    parser = ArgumentParser()
    parser.add_argument("nf1_csv")
    parser.add_argument("nf2_csv")
    parser.add_argument("--output_csv", type=FileType("wb"), default="-")
    return parser.parse_args()


def main():
    args = get_args()

    nf1_data = pd.read_csv(args.nf1_csv)
    nf2_data = pd.read_csv(args.nf2_csv)

    columns = [
        "group_family",
        "group_rank",
        "representation",
        "Nf",
        "L",
        "T",
        "beta",
        "m",
        "value_A1++_mass",
        "uncertainty_A1++_mass",
        "value_E++_mass",
        "uncertainty_E++_mass",
    ]

    data = pd.concat([nf1_data, nf2_data])[columns]
    data.dropna(inplace=True)
    data.to_csv(args.output_csv, index=False)


if __name__ == "__main__":
    main()
