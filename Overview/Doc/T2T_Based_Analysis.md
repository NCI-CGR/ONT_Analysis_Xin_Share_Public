# T2T-based Analysis
In this doc we will introduce how to use T2T-reference to run the wf-humane-variant pipeline
## Original Email
<img width="2500" height="1406" alt="image" src="https://github.com/user-attachments/assets/ebba64dd-13e1-4064-bc08-ad1bf1f31040" />

```
Hi Komal,

Here is the slide we discussed. The full documentation for the workflow steps can also be
found here: https://github.com/epi2me-labs/wf-human-variation?tab=readme-ov-file#pipeline-overview

We do not have a specific ONT recommended T2T reference genome, but this one should work:
https://hgdownload.soe.ucsc.edu/goldenPath/hs1/bigZips/hs1.fa.gz or you can download the full NCBI
RefSeq version here: Homo sapiens genome assembly T2T-CHM13v2.0 - NCBI - NLM. If you use the T2T reference
be aware that there are parts of the wf-human-variation workflow that will not work. There is a summary
table for this in the documentation:
https://github.com/epi2me-labs/wf-human-variation?tab=readme-ov-file#10-genome-compatibility-and-running-the-workflow-on-non-human-genomes.
Specifically – CNV, STR calling, and annotation will not work and should be disabled.

-Rob
Field Bioinformatics Scientist
rob.harbert@nanoporetech.com
```
## Notice
CNV, STR calling, and annotation will not work and should be disabled.

## Inputs Preparation
### BED File
The original bed file we got is based on hg38, we need to lift it over to T2T-based bed file.
1. T2T-based BED
```
/DCEG/Projects/Exome/SequencingData/DAATeam/Xin/ad_hoc/ONT/Data/Dependence/T2T/T2T_chrX_regionwise.bed
```
2. How to lift over
```
/DCEG/Projects/Exome/SequencingData/DAATeam/Xin/ad_hoc/ONT/Run/T2T/customize_script/BedConvert

Please check READNE.txt in the same folder for more details
```
3. The perfect bed file can be downloaded from the link below
```
https://s3-us-west-2.amazonaws.com/human-pangenomics/T2T/CHM13/assemblies/annotation/chm13v2.0_cytobands_allchrs.bed
```
### uBAMs
1. The wf-human-variant pipeline cannot take fastq.gz as an input.
2. The input should be either .bam or .ubam. For our case, we do need to use T2T reference to do the alignmnet again.
3. We only have fastq.gz and need to covert it to .ubam
4. The location of uBAM and how to convert fastq.gz to uBAM
```
(1) SD386613
/DCEG/Projects/Exome/SequencingData/DAATeam/Xin/ad_hoc/ONT/Run/customized_script/uBAM_Convert/SD386613/uBAM
/DCEG/Projects/Exome/SequencingData/DAATeam/Xin/ad_hoc/ONT/Run/customized_script/uBAM_Convert/SD386613/job.sh

(2) SD407538
/DCEG/Projects/Exome/SequencingData/DAATeam/Xin/ad_hoc/ONT/Run/customized_script/uBAM_Convert/SD407538/uBAM
/DCEG/Projects/Exome/SequencingData/DAATeam/Xin/ad_hoc/ONT/Run/customized_script/uBAM_Convert/SD407538/job.sh
```
### Reference
1. The reference and the bed file should be share the same way to name the chromosome. 
2. THe chromosome name in the bed file we current using (e.g. chrX) is inconsistent with the NCBI T2T reference (e.g., NC_060947.1 Homo sapiens isolate CHM13 chromosome X, alternate assembly T2T-CHM13v2.0).
3. As a result, I am currently using UCSC-verson T2T reference to run the pipeline
```
/DCEG/CGF/Bioinformatics/Production/data/T2T/UCSC/hs1.fa

Please check READNE.txt in the same folder for more details
```
## How to Run the Pipeline
1. SD386613
```
/DCEG/Projects/Exome/SequencingData/DAATeam/Xin/ad_hoc/ONT/Run/T2T/wf-human-variant/SD386613_With_Bed/job.sh
```
2. SD407538
```
/DCEG/Projects/Exome/SequencingData/DAATeam/Xin/ad_hoc/ONT/Run/T2T/wf-human-variant/SD407538_With_Bed/job.sh
```
## Running Results
1. SD386613
```
/DCEG/Projects/Exome/SequencingData/DAATeam/Xin/ad_hoc/ONT/Run/T2T/wf-human-variant/SD386613_With_Bed/output
```
2. SD407538
```
/DCEG/Projects/Exome/SequencingData/DAATeam/Xin/ad_hoc/ONT/Run/T2T/wf-human-variant/SD407538_With_Bed/output
```
### NOTICE
All jobs are still running, and I will update this doc once everything is all set.
