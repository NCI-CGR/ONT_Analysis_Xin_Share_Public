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
## Jobs 
### Issues 
1. The BAM downloaded from ONT online Repo (e.g. HG002)
   * missing some required "@PG" group information
   * does contain "SM" tag in "@RG" group, however the name is not expected (e.g. hg002)
2. The BAM from CGR (SD3, SD4) -> question for kristie
   * missing "SM" tag in "@RG" group

### Pipeline
1. Time cost is out of default settings (2 hours limitation)
```
Execution cancelled -- Finishing pending tasks before exit ERROR ~ Error executing process > 'modkit_phased_mC (1)' Caused by: Process exceeded running time limit (2h) Command executed: # compute sample probabilities probs=$( modkit sample-probs HG002.PAW70337.sorted.bam \ -p 0.1 \ --interval-size 5000000 \ --only-mapped \ --threads 24 \ 2> /dev/null | awk 'NR>1 {ORS=" "; print "--filter-threshold "$1":"$3}' ) # run modkit pileup for phased 5mC modkit pileup \ --ref GRCh38.p2.maimcontigs.fa \ --interval-size 1000000 \ --log-filepath modkit_phased_HG002.PAW70337.sorted.log \ ${probs} \ --prefix HG002.PAW70337.sorted_5mC \ --partition-tag HP \ --combine-strands \ --cpg \ --threads 24 \ HG002.PAW70337.sorted.bam \ HG002.PAW70337.sorted mv HG002.PAW70337.sorted/*.bed ./ # Move the output files to the current directory Command exit status: - Command output: (empty) Command error: WARNING: group: unknown groupid 20010 > calculated chunk size: 36, interval size 1000000, processing 36000000 positions concurrently > filtering to only CpG motifs > creating HG002.PAW70337.sorted > using threshold 0.7285156 for base A > using threshold 0.72265625 for base C > no default pass threshold was provided, so base modifications at primary sequence bases other than A,C will not be filtered > Using filter threshold 0.7285156 for A. > Using filter threshold 0.72265625 for C. Work dir: /mnt/nfs/gigantor/ifs/DCEG/Projects/Exome/SequencingData/DAATeam/Xin/ad_hoc/ONT/Run/ont-methylDMR-kit/HG002/PAW70337/work/71/24fe67d0f9ee4081f68ac54d06382f
```
2. HiPhase can not handle the BAM missing "SM"
3. wf-human-vairant cannot handle the BAM missing some "@PG" info


### Coverage 
1. SD386613
<img width="1108" height="411" alt="image" src="https://github.com/user-attachments/assets/e5577156-386e-45b4-9901-786b4fe40f90" />

2. SD407538
<img width="1132" height="410" alt="image" src="https://github.com/user-attachments/assets/3b7ddeec-08f7-4fe3-8dee-6c11df356ae3" />

3. HG002
<img width="1177" height="414" alt="image" src="https://github.com/user-attachments/assets/7bd2546d-00db-4cfc-8ed3-9594a1773a64" />



