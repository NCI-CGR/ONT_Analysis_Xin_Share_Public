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

## Results 
### SD386613
1. SD386613-hg38-Centeromere
<img width="3600" height="1200" alt="image" src="https://github.com/user-attachments/assets/901ed42d-bcd9-4977-b431-a9422c9d3291" />
   
2. SD386613-T2T-Centeromere
<img width="3600" height="1200" alt="image" src="https://github.com/user-attachments/assets/0b741117-1d2d-4725-a833-1882e73bf2bb" />

3. Stacked Plots
<img width="3600" height="1500" alt="image" src="https://github.com/user-attachments/assets/1cfceb1c-5ac8-45d6-a518-1120b8888611" />
