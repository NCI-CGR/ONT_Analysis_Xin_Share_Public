# ont-methylDMR-kit
This is a pipeline that be used for all-way methylation analysis

## How to use it
### From modkit pileup mode
```
# First download and index the ref genome
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/001/405/GCA_000001405.15_GRCh38/seqs_for_alignment_pipelines.ucsc_ids/GCA_000001405.15_GRCh38_no_alt_analysis_set.fna.gz && \
gunzip GCA_000001405.15_GRCh38_no_alt_analysis_set.fna.gz && \
samtools faidx GCA_000001405.15_GRCh38_no_alt_analysis_set.fna

# Run the pipeline from modkit pileup
cd ont-methylDMR-kit && tar -xvf test_data.tar.gz

nextflow run ont-methylDMR-kit/main.nf -profile singularity \
 --phased_mC   \
 --pileup \
 --plot \
 --phased_modBam ont-methylDMR-kit/HG002_base-mod-5mC_chr15/HG002_base-mod-5mC_chr15.bam \
 --reference GCA_000001405.15_GRCh38_no_alt_analysis_set.fna \
 --output_dir output
```
### From bedmethyl mode
```
nextflow run ont-methylDMR-kit/main.nf -profile singularity \
  --input_file1 ont-methylDMR-kit/HG002_base-mod-5mC_chr15/HG002_chr15_5mC.1.bed \
  --input_file2 ont-methylDMR-kit/HG002_base-mod-5mC_chr15/HG002_chr15_5mC.2.bed \
  --phased_mC \
  --plot \
  --phased_modBam ont-methylDMR-kit/HG002_base-mod-5mC_chr15/HG002_base-mod-5mC_chr15.bam \
  --output_dir output
##--reference provide a reference (hg38 for this example) to plot DMRs using methylartist as well
```

## Dependences 
1. Singlarity image files
```
-rwxrwxr-x 1 lix33 ncicgf_dceg_exome 358M Sep 17 19:02 nyagam-methylartist-v1.5.2.img
-rwxrwxr-x 1 lix33 ncicgf_dceg_exome 122M Sep 17 18:55 nyagam-seaborn-0.13.2.img
-rwxrwxr-x 1 lix33 ncicgf_dceg_exome 186M Sep 17 18:51 nyagam-modbamtools-v0.4.8.img
-rwxrwxr-x 1 lix33 ncicgf_dceg_exome 186M Sep 17 18:48 nyagam-modbamtools-v0.4.8.img.pulling.1758147449430
-rwxrwxr-x 1 lix33 ncicgf_dceg_exome 571M Sep 17 18:17 nyagam-ont-methyldmr-kit-v1.0.img
-rwxrwxr-x 1 lix33 ncicgf_dceg_exome  42M Sep 17 18:08 nyagam-modkit-v0.5.0.img
```
2. The online repo
```
https://github.com/NyagaM/ont-methylDMR-kit
```
## Notifications
1. only 5mC dmrs can be plotted at the moment
   * it supports haplotype-specific DMR plotting
   * it supports DMRs between two samples
   * it does NOT supoort plotting DMRs from group analysis
