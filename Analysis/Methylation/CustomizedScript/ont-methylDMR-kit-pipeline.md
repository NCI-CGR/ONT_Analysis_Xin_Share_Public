## Outline
- [ont-methylDMR-kit](#ont-methylDMR-kit)
  - [How to use it](#How-to-use-it)


# ont-methylDMR-kit
This is a pipeline that be used for all-way methylation analysis

## How-to-use-it
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

## Three usefull sub-running modes
### To run the end-to-end DMR analysis workflow between between two haplotypes:
```
nextflow run ont-methylDMR-kit/main.nf -profile singularity \
  --pileup \
  --plot \
  --phased_mC \ # or --phased_mA or --phased_hmC
  --phased_modBam /path/to/phased modBam for the sample \
  --output_dir /path/to/write output \
  --reference /path/to/ref genome \
  --gene_list /path/to/gene_list.txt  # if not provided, all regions will be plotted or use --imprinted to plot across imprinted genes
```
### To run DMR analysis from bedmethyls as the starting point between between two haplotypes (the output from modkit)
```
nextflow run ont-methylDMR-kit/main.nf -profile singularity \
  --input_file1 /path/to/bedmethyl file for haplotype 1 \
  --input_file2 /path/to/bedmethyl file for haplotype 2 \
  --phased_mC \ # or --phased_mA or --phased_hmC
  --phased_modBam /path/to/phased modBam for the sample \
  --output_dir /path/to/write output \
  --gene_list /path/to/gene_list.txt  or --imprinted  # if not provided, all regions will be plotted
  ##--reference provide a reference to plot DMRs using methylartist as well
```
### To run plots-only mode for DMRs identified between haplotypes
```
nextflow run ont-methylDMR-kit/main.nf -profile singularity \
  --plots-only \
  --phased_mC \ # or --phased_mA or --phased_hmC
  --annotated_dmrs /path/to/dmrs_table_annotated.bed \
  --phased_modBam /path/to/phased modBam for the sample \
  --output_dir /path/to/write output \
  --gene_list /path/to/gene_list.txt or --imprinted # if not provided, all regions will be plotted
  ##--reference provide a reference to plot DMRs using methylartist as well
```

## Thresholds used by ont-methylDMR-kit to generate DMR plots
```
Thresholds used by ont-methylDMR-kit to generate DMR plots

When you run ont-methylDMR-kit, it first uses DSS (a differential methylation tool) to identify statistically significant DMRs.
Only regions passing certain thresholds will be plotted in the dmr plot step.

>>>>>>>>>>>>>>>>>>>>>>>>>
Default thresholds (can be customized):

Methylation difference (delta): ≥ 10% (|Δmethylation| ≥ 0.10)

Statistical significance: p-value ≤ 0.01 (from DSS)

Region length: ≥ 100 bp

CpG count within region: ≥ 10

Merge distance: < 100 bp (adjacent DMRs closer than this are merged)
<<<<<<<<<<<<<<<<<<<<<<<<<<

Plotting rules:

Only DMRs that pass these thresholds and are successfully annotated will be plotted with modbamtools.

Supports plotting for sample pairs or haplotype pairs (requires corresponding modBAM files).

Does not directly support group-wise DMR plotting.

You can restrict plotting to specific genes with the --gene_list option.
```
