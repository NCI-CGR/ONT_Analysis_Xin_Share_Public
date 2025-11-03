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

# Self-alignment-based Analysis
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

# Wet lab experiement 20251007_1416_2E_PBE95329-based analysis (T2T reference was used directly)
## Wet lab Running Results
### Raw Data 
```
/DCEG/CGF/Sequencing/ONT/Prom24/RawData/CGR_Experiments/CGR_Experiments/20251007_1416_2E_PBE95329_69e83be9

# expired: /DCEG/CGF/Sequencing/ONT/Prom24/RawData/CGR_Experiments/10072025_AS_chrX_T2T/20251007_1416_2E_PBE95329_69e83be9
```
### PostRun_Analysis
```
/DCEG/CGF/Sequencing/ONT/Prom24/PostRun_Analysis/20251007_1416_2E_PBE95329_69e83be9
```
### Notice
1. Raw Data 
   * The BAM file contains 3 types of RG info in header, including barcode01, barcode02, and unclassified (unexpected).
   * Each "RG info" contains the "al" tag (CGR sample ID (SD386619 or SD407538), and "unclassified")
   * The RG info from "barcode01" and "barcode02" contain the "SM" tag (barcode01/barcode02), while RG info from "unclassified" does not contains "SM" tag.
   * I just manually checked multiple BAMs from SD386619 and SD407538. Based on my testing cases
      * The BAM header indeed contains 3 types of RG info (barcode01, barcode02, and unclassified)
      * Regarding the reads inside BAM file, SD386619 only contain the reads from barcode01, while SD407538 only contain the reads from barcode02 (expected). 

2. PostRun_Analysis
   * There is no folder named by using CGR Sample ID (we only have folders with the name "barcode*" and "unclassified")
   * If we combine the information from "raw data" folder, we can think that "barcode01" should be associated with SD386619, and "barcode02" should be associated with SD407538.
   * Regarding the BAM file inside the folder barcode01/barcode02
      * The "SM" tag contains the value of barcode01/barcode02 (e.g, SM:barcode01)
      * The "al" tag is not the CGR sample ID but the flow cell name "10072025_AS_chrX_T2T" (e.g., al:10072025_AS_chrX_T2T) (unexpected).

# Bioinformatics Analysis Results 
## Cytoband-chrX-bed-file-based Analysis
### ToulingQC
1. Flowcell-level
```
/DCEG/CGF/Sequencing/ONT/Prom24/Bioinformatics/Experiment/20251007_1416_2E_PBE95329_69e83be9/wf-toulligqc/v1.3/Flowcell-level/output
```
2. barcode01-based running results (should be associated with SD386619)
```
/DCEG/CGF/Sequencing/ONT/Prom24/Bioinformatics/Experiment/20251007_1416_2E_PBE95329_69e83be9/wf-toulligqc/v1.3/barcode01-based-SD386619/output_barcode01
```
3. barcode02-based running results (should be associated with SD407538)
```
/DCEG/CGF/Sequencing/ONT/Prom24/Bioinformatics/Experiment/20251007_1416_2E_PBE95329_69e83be9/wf-toulligqc/v1.3/barcode02-based-SD407538/output_barcode02
```
3. Notice
   * Some parts of report are identical among Flowcell-level, Barcode01-based and Barcode02-based analysis.
   * You will see the additional section in Barcode01-based and Barcode02-based analysis report (please check the screenshot below as an example).
<img width="1246" height="686" alt="image" src="https://github.com/user-attachments/assets/2e88eb62-48a7-4057-acec-fdfffe4569a0" />

### wf-human-variant-pipeline
1. barcode01-based analysis (should be associated with SD386619)
```
/DCEG/CGF/Sequencing/ONT/Prom24/Bioinformatics/Experiment/20251007_1416_2E_PBE95329_69e83be9/wf-human-variant/v2.7.2/barcode01-based-SD386619/output.wise.region
```
2. barcode02-based analysis (should be associated with SD407538)
```
/DCEG/CGF/Sequencing/ONT/Prom24/Bioinformatics/Experiment/20251007_1416_2E_PBE95329_69e83be9/wf-human-variant/v2.7.2/barcode02-based-SD407538/output.wise.region
```

## Whole-genome-bed-file-based Analysis
The major purpose of this run is getting the coverage summarization table
<img width="2704" height="1324" alt="image" src="https://github.com/user-attachments/assets/a63af763-576b-477b-9d30-4634e5457e28" />

### Chromosome-size-and-cytoband-chrX-based Analysis 
This type of analysis is based on using the bed file that was constructed below
1. Use chromosone size to create the regions for chromosome 1 to chromosome 22 and chromosome M
   * Use the artificial mask to create the fake annotations for each region (column 4 and 5)
   * Please check the example below
<img width="422" height="141" alt="image" src="https://github.com/user-attachments/assets/7e175860-ca0b-4e6f-bc53-bf7d5104b961" />

2. Use cytoband regions for chromosome X
   * Please check the example below
<img width="508" height="199" alt="image" src="https://github.com/user-attachments/assets/e1f42473-8051-4005-917b-98037a87cd45" />

3. Bed File
```
/DCEG/CGF/Sequencing/ONT/Prom24/Bioinformatics/Testing/WholeGenomeBed/wf-human-variant/v2.7.2/ChromSizeAndCytoBandX/hs1.chrom.sizes.cyto.chrX.artificial.mask.bed
```
4. Notification
   * Set "--bam_min_coverage 0" to handle the whole genome sequence analysis
5. Results Directory
```
/DCEG/CGF/Sequencing/ONT/Prom24/Bioinformatics/Testing/WholeGenomeBed/wf-human-variant/v2.7.2/ChromSizeAndCytoBandX
```
6. **Running Results (Each Sample)**
   * 20250701_1804_1C_PBE55027_8e8920e8 (SD386613)
   ```
   /DCEG/CGF/Sequencing/ONT/Prom24/Bioinformatics/Testing/WholeGenomeBed/wf-human-variant/v2.7.2/ChromSizeAndCytoBandX/20250701_1804_1C_PBE55027_8e8920e8/SD386613/output.chrom.size.and.cytoband.X
   ```
   * 20250701_1804_1F_PBE54594_26fb9d5f (SD407538)
   ```
   /DCEG/CGF/Sequencing/ONT/Prom24/Bioinformatics/Testing/WholeGenomeBed/wf-human-variant/v2.7.2/ChromSizeAndCytoBandX/20250701_1804_1F_PBE54594_26fb9d5f/SD407538/output.chrom.size.and.cytoband.X
   ```
   * 20251007_1416_2E_PBE95329_69e83be9 (SD386619)
   ```
   /DCEG/CGF/Sequencing/ONT/Prom24/Bioinformatics/Testing/WholeGenomeBed/wf-human-variant/v2.7.2/ChromSizeAndCytoBandX/20251007_1416_2E_PBE95329_69e83be9/SD386619/output.chrom.size.and.cytoband.X
   ```
   * 20251007_1416_2E_PBE95329_69e83be9 (SD407538)
   ```
   /DCEG/CGF/Sequencing/ONT/Prom24/Bioinformatics/Testing/WholeGenomeBed/wf-human-variant/v2.7.2/ChromSizeAndCytoBandX/20251007_1416_2E_PBE95329_69e83be9/SD407538/output.chrom.size.and.cytoband.X
   ```
### Chromosome-size-based Analysis 
This type of analysis is based on using the bed file that was constructed below
1. Use chromosome size to create the regions for all chromosomes (1 to chrom22, X, Y and M)
   * Use the artificial mask to create the fake annotations for each region (column 4 and 5)
   * Please check the example below
<img width="422" height="141" alt="image" src="https://github.com/user-attachments/assets/7e175860-ca0b-4e6f-bc53-bf7d5104b961" />

2. Bed File
```
/DCEG/CGF/Sequencing/ONT/Prom24/Bioinformatics/Testing/WholeGenomeBed/wf-human-variant/v2.7.2/ChromSize/hs1.chrom.sizes.artificial.mask.bed
```
3. Notification
   * Set "--bam_min_coverage 0" to handle the whole genome sequence analysis
4. Results Directory
```
/mnt/nfs/gigantor/ifs/DCEG/CGF/Sequencing/ONT/Prom24/Bioinformatics/Testing/WholeGenomeBed/wf-human-variant/v2.7.2/ChromSize
```
5. **Running Results (Each Sample)**
   * 20250701_1804_1C_PBE55027_8e8920e8 (SD386613)
   ```
   /DCEG/CGF/Sequencing/ONT/Prom24/Bioinformatics/Testing/WholeGenomeBed/wf-human-variant/v2.7.2/ChromSize/20250701_1804_1C_PBE55027_8e8920e8/SD386613/output.chrom.size
   ```
   * 20250701_1804_1F_PBE54594_26fb9d5f (SD407538)
   ```
   /DCEG/CGF/Sequencing/ONT/Prom24/Bioinformatics/Testing/WholeGenomeBed/wf-human-variant/v2.7.2/ChromSize/20250701_1804_1F_PBE54594_26fb9d5f/SD407538/output.chrom.size
   ```
   * 20251007_1416_2E_PBE95329_69e83be9 (SD386619)
   ```
   /DCEG/CGF/Sequencing/ONT/Prom24/Bioinformatics/Testing/WholeGenomeBed/wf-human-variant/v2.7.2/ChromSize/20251007_1416_2E_PBE95329_69e83be9/SD386619/output.chrom.size
   ```
   * 20251007_1416_2E_PBE95329_69e83be9 (SD407538)
   ```
   /DCEG/CGF/Sequencing/ONT/Prom24/Bioinformatics/Testing/WholeGenomeBed/wf-human-variant/v2.7.2/ChromSize/20251007_1416_2E_PBE95329_69e83be9/SD407538/output.chrom.size
   ```
