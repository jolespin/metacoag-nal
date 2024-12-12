#!/usr/bin/env python3

import click

from metacoag import metacoag_runner

__author__ = "Vijini Mallawaarachchi and Yu Lin"
__copyright__ = "Copyright 2020, MetaCoAG Project"
__license__ = "GPL-3.0"
__version__ = "1.2.3rc1"
__maintainer__ = "Vijini Mallawaarachchi"
__email__ = "vijini.mallawaarachchi@anu.edu.au"
__status__ = "Stable Release"


class ArgsObj:
    def __init__(
        self,
        assembler,
        graph,
        contigs,
        abundance,
        paths,
        output,
        hmm,
        # prefix,
        min_length,
        p_intra,
        p_inter,
        d_limit,
        depth,
        n_mg,
        # no_cut_tc,
        # mg_threshold,
        bin_mg_threshold,
        min_bin_size,
        delimiter,
        nthreads,
        proteins,
        proteins_to_contigs,
        hmm_marker_field,
        score_type,
        threshold_method,
        evalue,
    ):
        self.assembler = assembler
        self.graph = graph
        self.contigs = contigs
        self.abundance = abundance
        self.paths = paths
        self.output = output
        self.hmm = hmm
        # self.prefix = prefix
        self.min_length = min_length
        self.p_intra = p_intra
        self.p_inter = p_inter
        self.d_limit = d_limit
        self.depth = depth
        self.n_mg = n_mg
        # self.no_cut_tc = no_cut_tc
        # self.mg_threshold = mg_threshold
        self.bin_mg_threshold = bin_mg_threshold
        self.min_bin_size = min_bin_size
        self.delimiter = delimiter
        self.nthreads = nthreads
        self.proteins = proteins
        self.proteins_to_contigs = proteins_to_contigs
        self.hmm_marker_field = hmm_marker_field
        self.score_type = score_type
        self.threshold_method = threshold_method
        self.evalue = evalue


# Setup argument parser
# ---------------------------------------------------

@click.command()
@click.option(
    "--assembler",
    help="name of the assembler used. (Supports SPAdes, MEGAHIT and Flye)",
    type=click.Choice(["spades", "megahit", "megahitc", "flye", "custom"], case_sensitive=False),
    required=True,
)
@click.option(
    "--graph",
    help="path to the assembly graph file",
    type=click.Path(exists=True),
    required=True,
)
@click.option(
    "--contigs",
    help="path to the contigs file",
    type=click.Path(exists=True),
    required=True,
)
@click.option(
    "--abundance",
    help="path to the abundance file",
    type=click.Path(exists=True),
    required=True,
)
@click.option(
    "--paths",
    help="path to the contigs.paths (metaSPAdes) or assembly.info (metaFlye) file",
    type=click.Path(exists=True),
    required=False,
)
@click.option(
    "--output",
    help="path to the output folder",
    type=click.Path(dir_okay=True, writable=True, readable=True),
    required=True,
)
@click.option(
    "--proteins",
    help="path to proteins fasta in Prodigal format",
    type=str,
    required=False,
)
@click.option(
    "--proteins_to_contigs",
    help="Tab-delimited file mapping proteins to contigs [id_protein]<tab>[id_contig].  If --proteins and provided without --proteins_to_contigs then id_protein formatting is assumed to be [id_contig]_[gene_number]",
    type=str,
    required=False,
)
@click.option(
    "--hmm",
    help="path to marker.hmm[.gz] file.",
    default="auxiliary/marker.hmm.gz",
    show_default=True,
    type=str,
    required=False,
)
@click.option(
    "--hmm_marker_field",
    help="HMM reference type",
    default="accession",
    show_default=True,
    required=False,
    type=click.Choice(["accession", "name"]),
)
@click.option(
    "--score_type",
    help="Score reflects full sequence or domain only",
    default="full",
    show_default=True,
    required=False,
    type=click.Choice(["full", "domain"]),
)
@click.option(
    "--threshold_method",
    help="Cutoff threshold method",
    default="trusted",
    show_default=True,
    required=False,
    type=click.Choice(["gathering", "noise", "trusted", "e"]),
)
@click.option(
    "--evalue",
    help="E-value threshold .",
    type=float,
    default=10,
    show_default=True,
    required=False,
)

@click.option(
    "--min_length",
    help="minimum length of contigs to consider for binning.",
    type=int,
    default=1000,
    show_default=True,
    required=False,
)
@click.option(
    "--p_intra",
    help="minimum probability of an edge matching to assign to the same bin.",
    type=click.FloatRange(0, 1),
    default=0.1,
    show_default=True,
    required=False,
)
@click.option(
    "--p_inter",
    help="maximum probability of an edge matching to create a new bin.",
    type=click.FloatRange(0, 1),
    default=0.01,
    show_default=True,
    required=False,
)
@click.option(
    "--d_limit",
    help="distance limit for contig matching.",
    type=int,
    default=20,
    show_default=True,
    required=False,
)
@click.option(
    "--depth",
    help="depth to consider for label propagation.",
    type=int,
    default=10,
    show_default=True,
    required=False,
)
@click.option(
    "--n_mg",
    help="total number of marker genes.",
    type=int,
    default=108,
    show_default=True,
    required=False,
)
# @click.option(
#     "--no_cut_tc",
#     help="do not use --cut_tc for hmmsearch.",
#     is_flag=True,
#     default=False,
#     show_default=True,
#     required=False,
# )
# @click.option(
#     "--mg_threshold",
#     help="length threshold to consider marker genes.",
#     type=click.FloatRange(0, 1, clamp=True),
#     default=0.5,
#     show_default=True,
#     required=False,
# )
@click.option(
    "--bin_mg_threshold",
    help="minimum fraction of marker genes that should be present in a bin.",
    type=click.FloatRange(0, 1, clamp=True),
    default=0.33333,
    show_default=True,
    required=False,
)
@click.option(
    "--min_bin_size",
    help="minimum size of a bin to output in base pairs (bp).",
    type=int,
    default=200000,
    show_default=True,
    required=False,
)
@click.option(
    "--delimiter",
    help="delimiter for output results. Supports a comma (,), a semicolon (;), a tab ($'\\t'), a space (\" \") and a pipe (|) .",
    type=click.Choice([",", ";", "$'\\t'", "\" \""], case_sensitive=False),
    default=",",
    show_default=True,
    required=False,
)
@click.option(
    "--nthreads",
    help="number of threads to use.",
    type=int,
    default=8,
    show_default=True,
    required=False,
)
@click.version_option(__version__, "-v", "--version", is_flag=True)
def main(
    assembler,
    graph,
    contigs,
    abundance,
    paths,
    output,
    hmm,
    # prefix,
    min_length,
    p_intra,
    p_inter,
    d_limit,
    depth,
    n_mg,
    # no_cut_tc,
    # mg_threshold,
    bin_mg_threshold,
    min_bin_size,
    delimiter,
    nthreads,
    proteins,
    proteins_to_contigs,
    hmm_marker_field,
    score_type,
    threshold_method,
    evalue,
    
):
    """
    MetaCoAG: Binning Metagenomic Contigs via Composition, Coverage and Assembly Graphs
    """

    # Make args object
    args = ArgsObj(
        assembler,
        graph,
        contigs,
        abundance,
        paths,
        output,
        hmm,
        # prefix,
        min_length,
        p_intra,
        p_inter,
        d_limit,
        depth,
        n_mg,
        # no_cut_tc,
        # mg_threshold,
        bin_mg_threshold,
        min_bin_size,
        delimiter,
        nthreads,
        proteins,
        proteins_to_contigs,
        hmm_marker_field,
        score_type,
        threshold_method,
        evalue,
    )
    
    # Run MetaCoAG
    # ---------------------------------------------------
    metacoag_runner.main(args)


if __name__ == "__main__":
    main()
