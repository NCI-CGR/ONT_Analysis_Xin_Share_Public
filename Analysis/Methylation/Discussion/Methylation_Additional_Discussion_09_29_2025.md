# Question from Kristie
## Original Question
JIRA Ticket
```
https://tracker.nci.nih.gov/browse/CGRBI-242
```
## Comments and jobs arrangement from Xin
```
1: Would it be possible to run the other sample (SD407538) too, as well as one of the publicly available datasets from ONT?
   Comments: 
   Sure Kristie, I will process two samples below, including 
   1) SD407538 (from CGR) 
   2) HG002/PAW70337 (from ONT Public Repo) -> 
   
2: For each of the 3 samples, what is the average depth of coverage on chrX for each haplotagged bam (ie, what's the avg chrX coverage on haplotype 1, and what's the avg chrX coverage on haplotype
   Comments:
   Sure I will calculate the metrics below for sample SD386613, SD407538 and HG002
   1) the average chrX coverage for the haplotagged BAM (consider all records)
   2) the average chrX coverage for the haplotagged BAM (only consider the phased records)
   3) the average chrX coverage on haplotype 1
   4) the average chrX coverage on haplotype 2
   
3: For each of the 3 samples, can we determine what the phasing block sizes are for chrX? Rob mentioned he may have a script to do this.
   Comments:
   Sure I will find a way to generate a file to record all phasing blocks' sizes and plot the distribution. Once I got Rob's script, I will try his method to do this job again.

4: For each of the 3 samples, assuming the same parameters used for DMR, can we compare the stats for this analysis (ie, how many entries in dmrs_table.bed, average length of these regions)
   Comments:
   Sure, I will run the pipeline "ont-methylDMR-kit" for all these 3 samples, and then compare
   1) The number of entries in dmrs_table.bed
   2) average length of these regions
```
