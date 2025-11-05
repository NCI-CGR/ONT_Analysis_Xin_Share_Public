# Centromere Coverage Explore
## Centromere Bed file
1. JIRA Ticket
https://tracker.nci.nih.gov/browse/CGRSA-1375

2. Original Email
```
Hi All,

As we discussed in today's meeting, I found that Heng Li compiled the centromere regions in T2T and GRCh38 genome versions for each chromosome.

You can get the two bed files from the following link.

https://zenodo.org/records/17204470

For convenience, I uploaded the two bed files and the README here.

00README.md

hg38.cen-mask.bed

chm13v2.cen-mask.bed

We can use these two bed files for comparison.

Certainly, other files may be useful for future projects like *.PAR.bed etc.

Difei
```

3. Centeromere Bed file for hg38 and T2T
```
(1) hg38: hg38.cen-mask.bed
https://zenodo.org/records/17204470/files/hg38.cen-mask.bed?download=1

(2) T2T: chm13v2.cen-mask.bed
https://zenodo.org/records/17204470/files/chm13v2.cen-mask.bed?download=1
   
(3) Main website
https://zenodo.org/records/17204470
  
(4) Grab chrX bed file
cat ./chm13v2.cen-mask.bed | grep -i 'chrX' > chm13v2.cen-mask.chrX.only.bed
cat ./hg38.cen-mask.bed | grep -i 'chrX' > hg38.cen-mask.chrX.only.bed
```

## Results (Samtools-Depth-Based Plot)
### SD386613
1. SD386613-hg38-Centeromere
<img width="3600" height="1200" alt="image" src="https://github.com/user-attachments/assets/901ed42d-bcd9-4977-b431-a9422c9d3291" />

```
[INFO] Coverage plot saved to SD386613_chrX_hg38_samtools_depth_plot.png
  chrom  position  depth
0  chrX  58524641    153
1  chrX  58524642    152
2  chrX  58524643    152
3  chrX  58524644    152
4  chrX  58524645    152
           position         depth
count  3.981731e+06  3.981731e+06
mean   6.051551e+07  1.268376e+02
std    1.149427e+06  2.040075e+02
min    5.852464e+07  0.000000e+00
25%    5.952007e+07  2.600000e+01
50%    6.051551e+07  5.900000e+01
75%    6.151094e+07  1.430000e+02
max    6.250637e+07  1.973000e+03
Max depth: 1973
Min depth: 0
```
   
2. SD386613-T2T-Centeromere
<img width="3600" height="1200" alt="image" src="https://github.com/user-attachments/assets/0b741117-1d2d-4725-a833-1882e73bf2bb" />

```
[INFO] Coverage plot saved to SD386613_chrX_T2T_samtools_depth_plot.png
  chrom  position  depth
0  chrX  57819764    150
1  chrX  57819765    150
2  chrX  57819766    150
3  chrX  57819767    149
4  chrX  57819768    151
           position         depth
count  3.107432e+06  3.107432e+06
mean   5.937348e+07  1.619599e+02
std    8.970385e+05  1.794680e+02
min    5.781976e+07  0.000000e+00
25%    5.859662e+07  4.500000e+01
50%    5.937348e+07  1.160000e+02
75%    6.015034e+07  2.020000e+02
max    6.092720e+07  1.301000e+03
Max depth: 1301
Min depth: 0
```

3. Stacked Plots
<img width="3600" height="1500" alt="image" src="https://github.com/user-attachments/assets/1cfceb1c-5ac8-45d6-a518-1120b8888611" />


### SD407538
1. SD407538-hg38-Centeromere
   * SD407538_chrX_hg38_samtools_depth_plot.png

<img width="3600" height="1200" alt="image" src="https://github.com/user-attachments/assets/28203a08-0feb-493a-8f8c-f7c616d0bc0d" />

```
[INFO] Coverage plot saved to SD407538_chrX_hg38_samtools_depth_plot.png
  chrom  position  depth
0  chrX  58524641     30
1  chrX  58524642     31
2  chrX  58524643     31
3  chrX  58524644     31
4  chrX  58524645     31
           position         depth
count  3.981731e+06  3.981731e+06
mean   6.051551e+07  1.746709e+01
std    1.149427e+06  2.578450e+01
min    5.852464e+07  0.000000e+00
25%    5.952007e+07  4.000000e+00
50%    6.051551e+07  1.000000e+01
75%    6.151094e+07  2.000000e+01
max    6.250637e+07  3.920000e+02
Max depth: 392
Min depth: 0
```

2. SD407538-T2T-Centeromere
   * SD407538_chrX_T2T_samtools_depth_plot.png

<img width="3600" height="1200" alt="SD407538_chrX_T2T_samtools_depth_plot" src="https://github.com/user-attachments/assets/241d4694-1c4a-4843-ac32-39d51e269b85" />

```
[INFO] Coverage plot saved to SD407538_chrX_T2T_samtools_depth_plot.png
  chrom  position  depth
0  chrX  57819764     45
1  chrX  57819765     45
2  chrX  57819766     45
3  chrX  57819767     45
4  chrX  57819768     45
           position         depth
count  3.107432e+06  3.107432e+06
mean   5.937348e+07  2.240501e+01
std    8.970385e+05  3.641601e+01
min    5.781976e+07  0.000000e+00
25%    5.859662e+07  4.000000e+00
50%    5.937348e+07  1.100000e+01
75%    6.015034e+07  2.700000e+01
max    6.092720e+07  7.820000e+02
Max depth: 782
Min depth: 0
```

3. Stacked Plots
<img width="3600" height="1500" alt="SD407538_chrX_centromere_coverage_comparison" src="https://github.com/user-attachments/assets/720682f6-1913-4754-bb29-123af2affbfd" />


## Metrics Evaluation
### Introduction
We use metrics to evaluate the situation in centeromere regions. 

There are 2 experiments be used for testing, inccluding
1. 20250701_1804_1C_PBE55027_8e8920e8
   * SD386613
2. 20250701_1804_1F_PBE54594_26fb9d5f
   * SD407538
  
For each experiment, we have 3 types of running results, including
1. hg38-based dataset (from sequencer directly)
2. T2T-based dataset (based on self-alignment)
3. T2T-based dataset (from sequencer directly)

Regarding the metrics we used for evaluation, please check the list below
```
1 Experiment
2 Sample
3 Self-Aligned (Pipeline)
4 Reference
5 Mean coverage
6 20th percentile coverage
7 Fold 80 base penalty
8 total_reads (mapped)
9 mean_mapq
10 median_mapq
11 pct_mapq_ge_30
12 pct_mapq0
13 pct_secondary
14 pct_supplementary
15 pct_softclip
```

### Results
1. Screenshot
<img width="1454" height="221" alt="Screenshot 2025-11-04 at 12 26 12 PM" src="https://github.com/user-attachments/assets/32e987b2-e723-407d-9f75-690235c73df5" />

2. File
[Centromere_Evaluation_Metrics.xlsx](https://github.com/user-attachments/files/23342667/Centromere_Evaluation_Metrics.xlsx)

## Coverage Depth Plot (log)
### Sample: SD386613
1. hg38
<img width="3600" height="1200" alt="image" src="https://github.com/user-attachments/assets/10bcdf30-1965-477f-8264-179df8131380" />

2. T2T
<img width="3600" height="1200" alt="image" src="https://github.com/user-attachments/assets/f41ff18d-7e83-421a-adff-a8e8d0d1e9fb" />

### Sample: SD407538
1. hg38
<img width="3600" height="1200" alt="image" src="https://github.com/user-attachments/assets/a3d8bca1-a31a-4574-af65-d67823866e05" />


2. T2T
<img width="3600" height="1200" alt="image" src="https://github.com/user-attachments/assets/dde63ed5-7ac9-466c-990a-466f4d562d1b" />

## MapQ Plot
### Sample: SD386613
1. hg38
<img width="3000" height="1500" alt="image" src="https://github.com/user-attachments/assets/ff6e0fea-8cfa-4263-b9ad-dd503ede930e" />

2. T2T
<img width="3000" height="1500" alt="image" src="https://github.com/user-attachments/assets/2e8cb271-f092-4636-bd5c-afd262517177" />


### Sample: SD407538
1. hg38
<img width="3000" height="1500" alt="image" src="https://github.com/user-attachments/assets/fb21d98c-4833-4ef0-a149-e90de116ca0a" />

2. T2T
<img width="3000" height="1500" alt="image" src="https://github.com/user-attachments/assets/cd8daa2b-4d44-46c3-a436-180ba36bbe02" />
