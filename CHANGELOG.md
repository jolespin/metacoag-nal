# Change Log

## 1.2.3rc4
* [2024.12.16] - Added `--graph auto` and `--paths auto` to try and automatically detect files
* [2024.12.16] - Added alias for key command line arguments

## 1.2.3rc3
* [2024.12.13] - Added support for Python v3.8.x

## 1.2.3rc2
* [2024.12.12] - Added `--assembler auto` to automatically detect assembler used

## 1.2.3rc1
* [2024.12.12] - Added support for `Pyrodigal` and `PyHMMSearch` instead of `FragGeneScan` and `HMMSearch`
* [2024.12.12] - Added support for precomputed genes via `--proteins` and `--proteins_to_contigs` arguments
* [2024.12.11] - Changed .fasta to .fa extension
* [2024.12.11] - Removed `--prefix` argument
* [2024.12.11] - Removed `--no_cut_tc` and `--mg_threshold` because PyHMMSearch does not use coverage filter at the moment
* [2024.12.11] - Changed `output_path` to `output_directory` with intermediate files being added in this directory only

## Pending:
* Add precomputed `PyHMMSearch` results
* Check abundance tables to make sure there are 2 columns
* Allow for graphs with subsets of scaffolds
