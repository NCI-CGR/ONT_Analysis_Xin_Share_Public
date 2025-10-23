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
### BED File (Lift-lover based)
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
3. Why the lift-over source code should be created
   * Once the T2T reference be more popular and widely used in research community, we may need to life over some of our existing hg38-based capture kits to T2T-based capture kits. Therefore, for long-term purpose, it is necessary for us to create our own script to lift over hg38-based to T2T-based  bed file.
   * Since the hg38-based bed file was provided by wet-lab, in order to keep everything be consistent, it may be a good idea to discuss with the wet-lab colleagues and use the same resources to grab the related T2T-based bed file.
   * Since wet-lab is currently doing T2T-reference based adaptive sampling, the bed file and reference will be used for running. I more prefer to use the same bed file that wet-lab used for data analysis (not download from my side).
   * I am currently more focus on how to make the pipeline be completed without error by using T2T reference, therefore, the most important thing from my side is making sure that the bed file is correct. The liftover bed is imperfect but should be 100% correct. 
   
### BED File (Download from internet directly)
1. Since we consider all bases in chrX, the perfect bed file can be downloaded from the link below
```
https://s3-us-west-2.amazonaws.com/human-pangenomics/T2T/CHM13/assemblies/annotation/chm13v2.0_cytobands_allchrs.bed
```

2. File location and script in CGR cluster
```
/DCEG/Projects/Exome/SequencingData/DAATeam/Xin/ad_hoc/ONT/Data/Dependence/T2T/wise_region_bed_from_downloaded
```

### Reference
1. The reference and the bed file should be share the same way to name the chromosome. 
2. THe chromosome name in the bed file we current using (e.g. chrX) is inconsistent with the NCBI T2T reference (e.g., NC_060947.1 Homo sapiens isolate CHM13 chromosome X, alternate assembly T2T-CHM13v2.0).
3. As a result, I am currently using UCSC-verson T2T reference to run the pipeline
```
/DCEG/CGF/Bioinformatics/Production/data/T2T/UCSC/hs1.fa

Please check READNE.txt in the same folder for more details
```

# Self-alignment0-based Analysis
This analysis is based on the fastq files from hg38-based wetlab run. Then, we realign the reads to T2T reference through pipeline.

## uBAMs
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
## Script Example
1. how to run nextflow
```
CMD="nextflow run ${DIRScript} \
	 --bam ${DIRData} \
	 --ref '${reference}' \
	 --bed '${bedfile}' \
	 --sample_name '${sampleName}' \
	 -c ${configFile} \
	 --snp \
	 --sv \
	 --mod \
	 --phased \
	 -profile singularity"
```
2. nextflow.config
```
singularity {
    enabled = true
    autoMounts = true
    cacheDir = '/mnt/nfs/gigantor/ifs/DCEG/Projects/Exome/SequencingData/DAATeam/Xin/ad_hoc/ONT/SingularityCache' 
    runOptions = "--bind /DCEG/Projects/Exome/SequencingData/DAATeam/Xin/ad_hoc/ONT/TMP"
}

docker.enabled = false

process {
  //container = 'docker://ontresearch/wf-human-variation-sv:sha8134f9fef5e19605c7fb4c1348961d6771f1af79'
  executor = 'local'
  containerEngine = 'singularity'
  // errorStrategy = 'retry'
}

params {
    snp = true
    sv = true
    mod = true
    cnv = false
    phased = true
    //ref = "/DCEG/CGF/Bioinformatics/Production/data/T2T/NCBI/GCF_009914755.1_T2T-CHM13v2.0_genomic.fna" 
    ref = "/DCEG/CGF/Bioinformatics/Production/data/T2T/UCSC/hs1.fa"
    bed = "/DCEG/Projects/Exome/SequencingData/DAATeam/Xin/ad_hoc/ONT/Data/Dependence/T2T/T2T_chrX_regionwise.bed" 
    sample_name = "SD386613"
}
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
### Lift-over-bed-file-based results
1. SD386613
```
/DCEG/Projects/Exome/SequencingData/DAATeam/Xin/ad_hoc/ONT/Run/T2T/wf-human-variant/SD386613_With_Bed/output.liftover.bed.based

job:
/DCEG/Projects/Exome/SequencingData/DAATeam/Xin/ad_hoc/ONT/Run/T2T/wf-human-variant/SD386613_With_Bed/job.sh
```

2. SD407538
```
/DCEG/Projects/Exome/SequencingData/DAATeam/Xin/ad_hoc/ONT/Run/T2T/wf-human-variant/SD407538_With_Bed/output.liftover.bed.based

job:
/DCEG/Projects/Exome/SequencingData/DAATeam/Xin/ad_hoc/ONT/Run/T2T/wf-human-variant/SD407538_With_Bed/job.sh
```

### Downloaded-bed-file-based results
1. SD386613
```
/DCEG/Projects/Exome/SequencingData/DAATeam/Xin/ad_hoc/ONT/Run/T2T/wf-human-variant/SD386613_With_Bed/output.wise.region

job:
/DCEG/Projects/Exome/SequencingData/DAATeam/Xin/ad_hoc/ONT/Run/T2T/wf-human-variant/SD386613_With_Bed/job_real_wise_region_bed.sh
```

2. SD407538
```
/DCEG/Projects/Exome/SequencingData/DAATeam/Xin/ad_hoc/ONT/Run/T2T/wf-human-variant/SD407538_With_Bed/output.wise.region

job:
/DCEG/Projects/Exome/SequencingData/DAATeam/Xin/ad_hoc/ONT/Run/T2T/wf-human-variant/SD407538_With_Bed/job_real_wise_region_bed.sh
```

### NOTICE
All jobs have been completed successfully. Both Lift-over-bed-file-based results and Downloaded-bed-file-based results are ready to review.
