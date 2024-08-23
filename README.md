# Unifying the data release for arXiv:1605.04258

This workflow collates data from other data releases,
and reformats them.

Specifically,

1. it takes the two CSV files from
   [the first data release for 1605.04258][v1-dr]
   and combines them in a common format with common metadata, and
2. it takes the input data for $SU(2)$, $N_f=2$ from
   [the analysis workflow release for 2408.00171][su2-analysis]
   and old data retained from the preparation of [1412.5994][su2-oldpaper]
   (included in this repository)
   and combines them to the form used in
   [1605.04258][lmh-paper].

## Requirements

- Conda, for example, installed from [Miniforge][miniforge]
- [Snakemake][snakemake], which may be installed using Conda

## Setup

1. Install the dependencies above.
2. Clone this repository
   (or download and `unzip` it)
   and `cd` into it:

   ```shellsession
   git clone https://github.com/edbennett/unify_lmh_2016
   cd unify_lmh_2016
   ```

## Running the workflow

The workflow is run using Snakemake:

``` shellsession
snakemake --cores 1 --use-conda
```

Snakemake will automatically download and install
all required Python packages,
as well as the data from the data releases mentioned above.

## Output

Output data are placed in the `assets` directory.

[v1-dr]: https://doi.org/10.5281/zenodo.13128485
[lmh-paper]: https://doi.org/10.48550/arXiv.1605.04258
[miniforge]: https://github.com/conda-forge/miniforge
[snakemake]: https://snakemake.github.io
[su2-oldpaper]: https://doi.org/10.48550/arXiv.1412.5994
[su2-analysis]: https://doi.org/10.5281/zenodo.12802810
