# Resources for Analysis
# BED File
1. Location
```
/DCEG/CGF/Sequencing/ONT/Prom24/Resources/Bed_Files
```
2. Folder structure
<img width="675" height="712" alt="image" src="https://github.com/user-attachments/assets/43bef0f2-8009-476c-a8bb-3c860dc83b46" />


## hg38
1. Location
```
/DCEG/CGF/Sequencing/ONT/Prom24/Resources/Bed_Files/hg38
```
2. README.txt
   * Location
    ```
   /DCEG/CGF/Sequencing/ONT/Prom24/Resources/Bed_Files/hg38/README.txt
   ```
   * Contains the donwloadable link and the script about how to obtain the related resources.
3. Important bed files
   * Cytoband for all main chromosoms
   ```
   /DCEG/CGF/Sequencing/ONT/Prom24/Resources/Bed_Files/hg38/hg38.chrom.main.cytoBand.bed
   ```
   * Cytoband for chrX only (we used currently)
   ```
   /DCEG/CGF/Sequencing/ONT/Prom24/Resources/Bed_Files/hg38/hg38_chrX_regionwise.bed
   ```
   * Cytoband for chrX only (contain an additional 5th column with the information of “Stain type”, recommended)
   ```
   /DCEG/CGF/Sequencing/ONT/Prom24/Resources/Bed_Files/hg38/hg38.chrX.cytoBand.bed
   ```
   * Full size chromosome (from chr1 to chr22, chrX, chrY and chrM) + cytoband chrX (used for wd-human-variant pipeline)
   ```
   /DCEG/CGF/Sequencing/ONT/Prom24/Resources/Bed_Files/hg38/hg38.chrom.full.sizes.cytoband.chrX.artificial.mask.bed
   ```
   * Full size chromosome (from chr1 to chr22, chrY and chrM, **NOTICE: NO CHRX**) + cytoband chrX (used for wd-human-variant pipeline)
   ```
   /DCEG/CGF/Sequencing/ONT/Prom24/Resources/Bed_Files/hg38/hg38.chrom.sizes.cytoband.chrX.artificial.mask.bed
   ```
   * Centromere regions for chrX
   ```
   /DCEG/CGF/Sequencing/ONT/Prom24/Resources/Bed_Files/hg38/centromere/hg38.cen-mask.chrX.only.bed
   ```

## T2T
1. Location
```
/DCEG/CGF/Sequencing/ONT/Prom24/Resources/Bed_Files/T2T
```
2. README.txt
   * Location
   ```
   /DCEG/CGF/Sequencing/ONT/Prom24/Resources/Bed_Files/T2T/README.txt
   ```
   * Contains the donwloadable link and the script about how to obtain the related resources.
4. Important bed files
   * Cytoband for all main chromosoms
   ```
   /DCEG/CGF/Sequencing/ONT/Prom24/Resources/Bed_Files/T2T/chm13v2.0_cytobands_allchrs.bed
   ``` 
   * Cytoband for chrX only
   ```
   /DCEG/CGF/Sequencing/ONT/Prom24/Resources/Bed_Files/T2T/chrX_T2T-hs1.bed
   ```
   * Full size chromosome (from chr1 to chr22, chrX, chrY and chrM) + cytoband chrX (used for wd-human-variant pipeline)
   ```
   /DCEG/CGF/Sequencing/ONT/Prom24/Resources/Bed_Files/T2T/T2T.hs1.chrom.full.sizes.cytoband.chrX.artificial.mask.bed
   ```
   * Full size chromosome (from chr1 to chr22, chrY and chrM, **NOTICE: NO CHRX**) + cytoband chrX (used for wd-human-variant pipeline)
   ```
   /DCEG/CGF/Sequencing/ONT/Prom24/Resources/Bed_Files/T2T/T2T.hs1.chrom.sizes.cytoband.chrX.artificial.mask.bed
   ```
   * Centromere regions for chrX
   ```
   /DCEG/CGF/Sequencing/ONT/Prom24/Resources/Bed_Files/T2T/centromere/chm13v2.cen-mask.chrX.only.bed
   ```
   
