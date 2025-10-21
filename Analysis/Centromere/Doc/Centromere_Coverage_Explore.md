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

