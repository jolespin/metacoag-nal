# Change Log
## 1.2.3rc1
* [2024.12.12] - Added support for `Pyrodigal` and `PyHMMSearch` instead of `FragGeneScan` and `HMMSearch`
* [2024.12.12] - Added support for precomputed genes via `--proteins` and `--proteins_to_contigs` arguments
* [2024.12.11] - Changed .fasta to .fa extension
* [2024.12.11] - Removed `--prefix` argument
* [2024.12.11] - Removed `--no_cut_tc` and `--mg_threshold` because PyHMMSearch does not use coverage filter at the moment
* [2024.12.11] - Changed `output_path` to `output_directory` with intermediate files being added in this directory only
