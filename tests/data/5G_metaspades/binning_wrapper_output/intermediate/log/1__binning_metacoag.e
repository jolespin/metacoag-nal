2024-12-12 17:19:57,882 - INFO - Detecting assembler type from contigs: tests/data/5G_metaspades/contigs.fasta
2024-12-12 17:19:57,882 - INFO - Detected assembler type: spades
2024-12-12 17:19:57,882 - INFO - Welcome to MetaCoAG: Binning Metagenomic Contigs via Composition, Coverage and Assembly Graphs.
2024-12-12 17:19:57,882 - INFO - Input arguments: 
2024-12-12 17:19:57,882 - INFO - Assembler used: spades
2024-12-12 17:19:57,882 - INFO - Contigs file: tests/data/5G_metaspades/contigs.fasta
2024-12-12 17:19:57,882 - INFO - Assembly graph file: tests/data/5G_metaspades/assembly_graph_with_scaffolds.gfa
2024-12-12 17:19:57,882 - INFO - Contig paths file: tests/data/5G_metaspades/contigs.paths
2024-12-12 17:19:57,882 - INFO - Abundance file: tests/data/5G_metaspades/coverm_mean_coverage.tsv
2024-12-12 17:19:57,882 - INFO - Final binning output file: tests/data/5G_metaspades/binning_wrapper_output/
2024-12-12 17:19:57,882 - INFO - Marker gene file hmm: auxiliary/marker.hmm.gz
2024-12-12 17:19:57,883 - INFO - Minimum length of contigs to consider: 1500
2024-12-12 17:19:57,883 - INFO - Depth to consider for label propagation: 10
2024-12-12 17:19:57,883 - INFO - p_intra: 0.1
2024-12-12 17:19:57,883 - INFO - p_inter: 0.01
2024-12-12 17:19:57,883 - INFO - bin_mg_threshold: 0.33333
2024-12-12 17:19:57,883 - INFO - min_bin_size: 200000 base pairs
2024-12-12 17:19:57,883 - INFO - d_limit: 20
2024-12-12 17:19:57,883 - INFO - Number of threads: 12
2024-12-12 17:19:57,883 - INFO - MetaCoAG started
2024-12-12 17:19:57,895 - INFO - Total number of contigs available: 519
2024-12-12 17:19:57,941 - INFO - Total number of edges in the assembly graph: 1065
2024-12-12 17:19:57,942 - INFO - Total isolated contigs in the assembly graph: 1
2024-12-12 17:19:57,942 - INFO - Obtaining lengths and coverage values of contigs
2024-12-12 17:19:58,087 - INFO - Total long contigs: 232
2024-12-12 17:19:58,087 - INFO - Total isolated long contigs in the assembly graph: 1
2024-12-12 17:19:58,087 - INFO - Obtaining tetranucleotide frequencies of contigs
2024-12-12 17:20:07,198 - INFO - Scanning for single-copy marker genes
2024-12-12 17:20:07,224 - INFO - Obtaining hmmout file
2024-12-12 17:20:07,224 - INFO - Using marker file: /Users/jolespin/miniconda3/envs/metacoag_env/lib/python3.9/site-packages/metacoag/metacoag_utils/auxiliary/marker.hmm.gz
2024-12-12 17:20:27,052 - INFO - Obtaining contigs with single-copy marker genes
2024-12-12 17:20:27,055 - INFO - Number of contigs containing single-copy marker genes: 88
2024-12-12 17:20:27,055 - INFO - Determining contig counts for each single-copy marker gene
2024-12-12 17:20:27,055 - INFO - Initialising bins
2024-12-12 17:20:27,055 - INFO - Matching and assigning contigs with single-copy marker genes to bins
2024-12-12 17:20:27,228 - INFO - Further assigning contigs with single-copy marker genes
2024-12-12 17:20:29,535 - INFO - Propagating labels to connected vertices of unlabelled long contigs
2024-12-12 17:20:29,537 - INFO - Further propagating labels to vertices of unlabelled long contigs
  0%|          | 0/148 [00:00<?, ?it/s]100%|██████████| 148/148 [00:00<00:00, 711061.85it/s]
2024-12-12 17:20:29,574 - INFO - Further propagating labels to connected vertices of unlabelled long contigs
2024-12-12 17:20:30,514 - INFO - Elapsed time: 32.6316020488739 seconds
2024-12-12 17:20:30,536 - INFO - Writing the Final Binning result to file
Splitting contigs into bins: 0it [00:00, ?it/s]Splitting contigs into bins: 73it [00:00, 728.66it/s]Splitting contigs into bins: 519it [00:00, 4232.90it/s]
2024-12-12 17:20:30,661 - INFO - Producing 8 bins...
2024-12-12 17:20:30,661 - INFO - Final binning results can be found in tests/data/5G_metaspades/binning_wrapper_output//bins
2024-12-12 17:20:30,661 - INFO - Thank you for using MetaCoAG!
