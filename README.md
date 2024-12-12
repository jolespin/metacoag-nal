<p align="center">
  <img src="https://raw.githubusercontent.com/metagentools/MetaCoAG/develop/docs/images/MetaCoAG_Logo_light.png#gh-light-mode-only" width="500" title="MetaCoAG logo" alt="MetaCoAG logo">
  <img src="https://raw.githubusercontent.com/metagentools/MetaCoAG/develop/docs/images/MetaCoAG_Logo_dark.png#gh-dark-mode-only" width="500" title="MetaCoAG logo" alt="MetaCoAG logo">
</p>

# MetaCoAG: Binning Metagenomic Contigs via Composition, Coverage and Assembly Graphs

Modified by [Josh L. Espinoza](https://github.com/jolespin/metacoag-nal) for [Pyrodigal](https://github.com/althonos/pyrodigal) and [PyHMMSearch](https://github.com/jolespin/pyhmmsearch) support.

[![DOI](https://img.shields.io/badge/DOI-10.1007/978--3--031--04749--7__5-informational)](https://doi.org/10.1007/978-3-031-04749-7_5)
[![DOI](https://img.shields.io/badge/DOI-10.1089/cmb.2022.0262-green)](https://doi.org/10.1089/cmb.2022.0262)

MetaCoAG is a metagenomic contig binning tool that makes use of the connectivity information found in assembly graphs, apart from the composition and coverage information. MetaCoAG makes use of single-copy marker genes along with a graph matching technique and a label propagation technique to bin contigs. MetaCoAG is tested on contigs obtained from next-generation sequencing (NGS) data. Currently, MetaCoAG supports contigs assembled using metaSPAdes and MEGAHIT, and recently we have added support for Flye assemblies (has not been tested extensively).

For detailed instructions on installation, usage and visualisation, please refer to the [documentation hosted at Read the Docs](https://metacoag.readthedocs.io/).

For original implementation, please refer to https://github/metagentools/MetaCoAG

## Dependencies
MetaCoAG installation requires Python 3.7 or above. You will need the following python dependencies to run MetaCoAG and related support scripts. The latest tested versions of the dependencies are listed as well.
* [python](https://www.python.org/)
* [python-igraph](https://igraph.org/python/)
* [biopython](https://biopython.org/)
* [networkx](https://networkx.github.io/)
* [scipy](https://www.scipy.org/)
* [numpy](https://numpy.org/)
* [tqdm](https://github.com/tqdm/tqdm)
* [click](https://click.palletsprojects.com/)


## Modifications
MetaCoAG NAL mod allows for precomputed gene predictions, cleans up intermediate files, and uses the following tools to scan for single-copy marker genes. These tools have been tested on the following versions.
* [Pyrodigal](https://github.com/althonos/pyrodigal)
* [PyHMMSearch](http://github.com/jolespin/pyhmmsearch)

## Installing NewAtlantis Labs modified MetaCoAG

### Install via pip

pip install git+https://github.com/jolespin/metacoag-nal

### Test the setup

After setting up, run the following command to ensure that metacoag is working.

```
metacoag --help
```

## Example Usage

### metaSPAdes
```
metacoag --assembler spades --graph /path/to/graph_file.gfa --contigs /path/to/contigs.fasta --paths /path/to/paths_file.paths --abundance /path/to/abundance.tsv --output /path/to/output_folder
```

### MEGAHIT
```
metacoag --assembler megahit --graph /path/to/graph_file.gfa --contigs /path/to/contigs.fasta --abundance /path/to/abundance.tsv --output /path/to/output_folder
```

### metaFlye
```
metacoag --assembler flye --graph /path/to/assembly_graph.gfa --contigs /path/to/assembly.fasta --paths /path/to/assembly_info.txt --abundance /path/to/abundance.tsv --output /path/to/output_folder
```

### Adding precomputed gene predictions

```
metacoag --assembler megahit --graph /path/to/graph_file.gfa --contigs /path/to/contigs.fasta --abundance /path/to/abundance.tsv --output /path/to/output_folder --proteins /path/to/proteins.faa
```

### Adding precomputed gene predictions that do not follow Prodigal formatting

```
metacoag --assembler megahit --graph /path/to/graph_file.gfa --contigs /path/to/contigs.fasta --abundance /path/to/abundance.tsv --output /path/to/output_folder --proteins /path/to/proteins.faa --proteins_to_contigs /path/to/proteins_to_contigs.tsv
```

## Citation

If you use MetaCoAG in your work, please cite the following publications.

> Mallawaarachchi, V., Lin, Y. (2022). MetaCoAG: Binning Metagenomic Contigs via Composition, Coverage and Assembly Graphs. In: Pe'er, I. (eds) Research in Computational Molecular Biology. RECOMB 2022. Lecture Notes in Computer Science(), vol 13278. Springer, Cham. DOI: [https://doi.org/10.1007/978-3-031-04749-7_5](https://doi.org/10.1007/978-3-031-04749-7_5)

> Vijini Mallawaarachchi and Yu Lin. Accurate Binning of Metagenomic Contigs Using Composition, Coverage, and Assembly Graphs. Journal of Computational Biology 2022 29:12, 1357-1376. DOI: [https://doi.org/10.1089/cmb.2022.0262](https://doi.org/10.1089/cmb.2022.0262)

## Funding

Initial implementation of MetaCoAG is funded by an [Essential Open Source Software for Science Grant](https://chanzuckerberg.com/eoss/proposals/cogent3-python-apis-for-iq-tree-and-graphbin-via-a-plug-in-architecture/) from the Chan Zuckerberg Initiative.

<p align="left">
  <img src="https://chanzuckerberg.com/wp-content/themes/czi/img/logo.svg" width="300">
</p>
