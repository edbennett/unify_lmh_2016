#!/usr/bin/env python3

from argparse import ArgumentParser, FileType

import numpy as np
import pandas as pd


def A(r, Delta):
    # Eq. (3.7) of arXiv:1605.04258 in the case c1 = 0
    return 1 / (2 * Delta) * np.log(-1 + np.exp(2 * Delta * r))


def r(A, Delta):
    # Inverse of A(r, Delta)
    return np.log(1 + np.exp(2 * Delta * A)) / (2 * Delta)


def get_args():
    parser = ArgumentParser()
    parser.add_argument("fig4_csv")
    parser.add_argument("fig5_csv")
    parser.add_argument("--output_csv", type=FileType("wb"), default="-")
    return parser.parse_args()


def main():
    args = get_args()

    fig4_data = pd.read_csv(args.fig4_csv)
    fig5_data = pd.read_csv(args.fig5_csv)

    # Defined in the caption of Fig. 4 of arXiv:1605.04258
    fig4_data["rIR"] = 1e-6
    fig4_data["rUV"] = 25

    fig4_data["-A(rIR)"] = -A(fig4_data["rIR"], fig4_data["Delta"])
    fig4_data["normalisation"] = "M0"
    fig4_data.rename(columns={"M/M0": "normalised_M"}, inplace=True)

    # Defined in the caption of Fig. 5 of arXiv:1605.04258
    fig5_data["Delta"] = 1.5
    fig5_data["rIR"] = r(-fig5_data["-A(rIR)"], fig5_data["Delta"])
    fig5_data["rUV"] = r(8 - fig5_data["-A(rIR)"], fig5_data["Delta"])

    fig5_data["normalisation"] = "MT"
    fig5_data.rename(columns={"M/MT": "normalised_M"}, inplace=True)

    full_data = pd.concat([fig4_data, fig5_data])[
        ["Spin", "Delta", "rIR", "rUV", "-A(rIR)", "normalised_M", "normalisation"]
    ]
    full_data.to_csv(args.output_csv, index=False)


if __name__ == "__main__":
    main()
