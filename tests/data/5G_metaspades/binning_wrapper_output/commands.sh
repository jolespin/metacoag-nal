# 1__binning_metacoag
echo '' > tests/data/5G_metaspades/binning_wrapper_output/scaffolds_to_bins.tsv && mkdir -p tests/data/5G_metaspades/binning_wrapper_output/bins && /Users/jolespin/miniconda3/envs/metacoag_env/bin/metacoag --assembler auto --contigs tests/data/5G_metaspades/contigs.fasta --abundance tests/data/5G_metaspades/coverm_mean_coverage.tsv --graph tests/data/5G_metaspades/assembly_graph_with_scaffolds.gfa --paths tests/data/5G_metaspades/contigs.paths --output tests/data/5G_metaspades/binning_wrapper_output/ --min_bin_size 200000 --min_length 1500 --nthreads 12 --hmm_marker_field accession --score_type full --threshold_method trusted --evalue 10.0

# 2__compile
'/Users/jolespin/Cloud/Informatics/Development/Packages/veba/bin/scripts/scaffolds_to_bins.py' -x fa -i tests/data/5G_metaspades/binning_wrapper_output/bins --bin_prefix METACOAG__ > tests/data/5G_metaspades/binning_wrapper_output/scaffolds_to_bins.tsv && cut -f1 tests/data/5G_metaspades/binning_wrapper_output/scaffolds_to_bins.tsv > tests/data/5G_metaspades/binning_wrapper_output/binned.list && cut -f2 tests/data/5G_metaspades/binning_wrapper_output/scaffolds_to_bins.tsv | sort -u > tests/data/5G_metaspades/binning_wrapper_output/bins.list && cat tests/data/5G_metaspades/contigs.fasta | grep "^>" | cut -c2- > tests/data/5G_metaspades/binning_wrapper_output/unbinned.list 

    for FP in tests/data/5G_metaspades/binning_wrapper_output/bins/*.fa;
        do ID_GENOME=$(basename ${FP} .fa);
        mv $FP tests/data/5G_metaspades/binning_wrapper_output/bins/METACOAG__${ID_GENOME}.fa
        done

     /Users/jolespin/miniconda3/envs/metacoag_env/bin/seqkit stats --basename --all -T -j 12 tests/data/5G_metaspades/binning_wrapper_output/bins/*.fa | python -c 'import sys, pandas as pd; df = pd.read_csv(sys.stdin, sep="	", index_col=0); df.index = df.index.map(lambda x: x[:-3]); df.to_csv(sys.stdout, sep="	")'> tests/data/5G_metaspades/binning_wrapper_output/genome_statistics.tsv

