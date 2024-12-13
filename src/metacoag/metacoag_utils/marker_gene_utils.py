#!/usr/bin/env python3

import logging
import os
import pathlib
import shutil
from collections import defaultdict

from metacoag import __version__


# create logger
logger = logging.getLogger(f"MetaCoaAG {__version__}")


# Modified from SolidBin
def scan_for_marker_genes(output_directory, contigs_file, nthreads, markerURL, proteins, hmm_marker_field, score_type,threshold_method, evalue):

    pyrodigalURL = "pyrodigal"
    pyrodigalURL = shutil.which(pyrodigalURL)
    if not pyrodigalURL:
        raise FileNotFoundError(f"Could not find Pyrodigal executable: {pyrodigalURL}")
    pyhmmsearchURL = "pyhmmsearch"
    pyhmmsearchURL = shutil.which(pyhmmsearchURL)
    if not pyhmmsearchURL:
        raise FileNotFoundError(f"Could not find PyHMMSearch executable: {pyhmmsearchURL}")

    if markerURL == "auxiliary/marker.hmm.gz":
        software_path = pathlib.Path(__file__).parent.absolute()
        markerURL = os.path.join(software_path, "auxiliary", "marker.hmm.gz")
    if not (os.path.exists(markerURL)):
        raise FileNotFoundError(f"Could not find HMMs: {markerURL}")
    
    logger.info("Using marker file: " + markerURL)

    if proteins:
        if not (os.path.exists(proteins)):
            raise FileNotFoundError(
                f"Could not find provided proteins file: {proteins}"
            )
        pyrodigalResultURL = str(proteins)

    else:
        pyrodigalResultURL = os.path.join(output_directory, "pyrodigal.faa")
        if not (os.path.exists(pyrodigalResultURL)):
            pyrodigalCmd = [
                pyrodigalURL, 
                '-a', 
                pyrodigalResultURL, 
                '-i', 
                contigs_file, 
                '-p',
                'meta', 
                "-j", 
                str(nthreads),
                "1>",
                os.path.join(output_directory, "logs", "pyrodigal.out"),
                "2>",    
                os.path.join(output_directory, "logs", "pyrodigal.err"),
            ]
            pyrodigalCmd = " ".join(map(str, pyrodigalCmd))
            logger.debug(f"exec cmd: {pyrodigalCmd}")
            os.system(pyrodigalCmd)
            

    hmmResultURL = os.path.join(output_directory, "pyhmmsearch.tsv")

    if os.path.exists(pyrodigalResultURL):
            # pyhmmsearch, 
            # '--n_jobs', 
            # parameters.threads, 
            # "-d", 
            # parameters.hmm_database, 
            # "-i", 
            # input_fasta, 
            # "-o", 
            # output_file, 
            # "--hmm_marker_field", 
            # parameters.hmm_marker_field, 
            # "--threshold_method", 
            # parameters.threshold_method,
            # "--evalue", 
            # parameters.evalue,
            # "--score_type", 
            # parameters.score_type,

        if not (os.path.exists(hmmResultURL)):
            hmmCmd = [
                pyhmmsearchURL,
                '-i', 
                pyrodigalResultURL, 
                "-o", 
                hmmResultURL,
                '-d', 
                markerURL, 
                "--n_jobs", 
                nthreads,
                "--hmm_marker_field",
                hmm_marker_field,
                "--threshold_method",
                threshold_method,
                "--evalue",
                evalue,
                "--score_type",
                score_type,
                "1>",
                os.path.join(output_directory, "logs", "pyhmmsearch.out"),
                "2>",    
                os.path.join(output_directory, "logs", "pyhmmsearch.err"),
            ]
            hmmCmd = " ".join(map(str, hmmCmd))
            logger.debug(f"exec cmd: {hmmCmd}")
            os.system(hmmCmd)

        else:
            logger.debug(f"PyHMMSearch search failed! Path: {hmmResultURL} does not exist.")
    else:
        logger.debug(f"Pyrodigal failed! Path: {pyrodigalResultURL} does not exist.  Please provide Pyrodigal protein fasta file using --proteins or try again after reinstall Pyrodigal.")


# # Get contigs containing marker genes
# def get_all_contigs_with_marker_genes(
#     contigs_file, 
#     hmmout_file,
#     contig_names_rev, 
#     mg_length_threshold,
#     proteins_to_contigs,
# ):
#     protein_to_contig = dict()
#     if protein_to_contig:
#         with open(protein_to_contig, 'r') as open_file:
#             for line in open_file:
#                 if not line.startswith('#'):
#                     line = line.strip()
#                     id_protein, id_contig = line.split()
#                     protein_to_contig[id_protein] = id_contig
        
                    
    
#     contig_markers = defaultdict(set)

#     with open(hmmout_file, "r") as f:
#         next(f)
#         for line in f:
#             line = line.strip()
#             if line:
#                 if not line.startswith('#'):
#                     id_protein, id_hmm, *tmp = line.split()
#                     id_contig = protein_to_contig.get(id_protein, lambda x: x.rsplit("_", maxsplit=1)[0])
#                     contig_num = contig_names_rev[id_contig]
#                     contig_markers[contig_num].add(id_hmm)
                    

#     #             # Marker gene length
#     #             marker_gene_length = int(strings[5])

#     #             # Mapped marker gene length
#     #             mapped_marker_length = int(strings[16]) - int(strings[15])

 
#     #             if mapped_marker_length > marker_gene_length * mg_length_threshold:
#     #                 # Get marker genes in each contig
#     #                 if contig_num not in contig_markers:
#     #                     contig_markers[contig_num] = [marker_gene]
#     #                 else:
#     #                     if marker_gene not in contig_markers[contig_num]:
#     #                         contig_markers[contig_num].append(marker_gene)
#     contig_markers = {k:list(v) for k,v in contig_markers.items()}
#     return contig_markers


# Get contigs containing marker genes
def get_contigs_with_marker_genes(
    contigs_file, 
    hmmout_file,
    contig_names_rev, 
    # mg_length_threshold,
    contig_lengths, #
    min_length,
    protein_to_contig,
):
    marker_contigs = defaultdict(set)
    contig_markers = defaultdict(set)

    with open(hmmout_file, "r") as f:
        next(f)
        for line in f:
            line = line.strip()
            if line:
                if not line.startswith('#'):
                    id_protein, id_hmm, *tmp = line.split()
                    id_protein, id_hmm, *tmp = line.split()
                    try:
                        id_contig = protein_to_contig[id_protein]
                    except KeyError:
                        id_contig = id_protein.rsplit("_", maxsplit=1)[0]
                    contig_num = contig_names_rev[id_contig]
                    contig_markers[contig_num].add(id_hmm)
                    contig_length = contig_lengths[contig_num]

                    if (
                        contig_length >= min_length
                        # and mapped_marker_length > marker_gene_length * mg_length_threshold
                    ):
                        contig_markers[contig_num].add(id_hmm)
                        marker_contigs[id_hmm].add(contig_num)
                                
    marker_contig_counts = {id_hmm:len(contigs) for id_hmm, contigs in marker_contigs.items()}
    marker_contigs = {k:list(v) for k,v in marker_contigs.items()}
    contig_markers = {k:list(v) for k,v in contig_markers.items()}

    return marker_contigs, marker_contig_counts, contig_markers


# Get contigs containing marker genes
def get_contigs_with_marker_genes_megahit(    
    contigs_file, 
    hmmout_file,
    contig_names_rev, 
    graph_to_contig_map_rev,
    # mg_length_threshold,
    contig_lengths, #
    min_length,
    protein_to_contig,
):
    marker_contigs = {}
    marker_contig_counts = {}
    contig_markers = {}

    marker_contigs = defaultdict(set)
    contig_markers = defaultdict(set)

    with open(hmmout_file, "r") as f:
        next(f)
        for line in f:
            line = line.strip()
            if line:
                if not line.startswith('#'):
                    id_protein, id_hmm, *tmp = line.split()
                    try:
                        id_contig = protein_to_contig[id_protein]
                    except KeyError:
                        id_contig = id_protein.rsplit("_", maxsplit=1)[0]
                    contig_num = contig_names_rev[graph_to_contig_map_rev[id_contig]]
                    contig_markers[contig_num].add(id_hmm)
                    contig_length = contig_lengths[contig_num]

                    if (
                        contig_length >= min_length
                        # and mapped_marker_length > marker_gene_length * mg_length_threshold
                    ):
                        contig_markers[contig_num].add(id_hmm)
                        marker_contigs[id_hmm].add(contig_num)
                                
    marker_contig_counts = {id_hmm:len(contigs) for id_hmm, contigs in marker_contigs.items()}
    marker_contigs = {k:list(v) for k,v in marker_contigs.items()}
    contig_markers = {k:list(v) for k,v in contig_markers.items()}

    return marker_contigs, marker_contig_counts, contig_markers


def count_contigs_with_marker_genes(marker_contig_counts):
    marker_frequencies = {}

    for marker in marker_contig_counts:
        if marker_contig_counts[marker] not in marker_frequencies:
            marker_frequencies[marker_contig_counts[marker]] = 1
        else:
            marker_frequencies[marker_contig_counts[marker]] += 1

    return marker_frequencies
