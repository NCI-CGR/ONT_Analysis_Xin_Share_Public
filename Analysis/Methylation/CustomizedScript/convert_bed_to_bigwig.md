# How to create bigwag
## 🧬 Step-by-Step: Convert `bedMethyl` to `.bigWig` Format

If you're using ONT's `wf-human-variation` pipeline with `--call_mods true`, methylation data is typically output in **BEDMethyl** format. This guide shows you how to convert it to `.bigWig` for visualization in genome browsers.

---

### 🛠 Requirements

Install the required tools:

```bash
# BEDTools
sudo apt install bedtools

# UCSC bedGraphToBigWig tool (download and make executable)
wget https://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/bedGraphToBigWig
chmod +x bedGraphToBigWig
```

---

### 🗂 Step 1: Sort the BEDMethyl File

Make sure the file is sorted by chromosome and position:

```bash
sort -k1,1 -k2,2n mod_output.bed > mod_output.sorted.bed
```

---

### 🌐 Step 2: Download Chromosome Size File

Pick the genome build used in your analysis (e.g., hg38):

```bash
wget http://hgdownload.soe.ucsc.edu/goldenPath/hg38/bigZips/hg38.chrom.sizes
```

---

### 🔄 Step 3: Convert to BigWig Format

Use the UCSC tool to convert:

```bash
./bedGraphToBigWig mod_output.sorted.bed hg38.chrom.sizes methylation.bigWig
```

---

### ✅ Output

The file `methylation.bigWig` is ready for use in:

- [IGV](https://software.broadinstitute.org/software/igv/)
- [UCSC Genome Browser](https:/)

### IGV
Import bigwig files (from different haplotype) into IGV and set the data range (max log scale)
<img width="1512" height="583" alt="image" src="https://github.com/user-attachments/assets/c882d448-5aa1-429b-9759-e732cb6db515" />


# Results
1. SD386613 (CGR Cluster)
```
/DCEG/Projects/Exome/SequencingData/DAATeam/Xin/ad_hoc/ONT/Run/SD386613/output/Methylation_Analysis

haplotype 1: wf_mods.1.bw
haplotype 2: wf_mods.2.bw
```
<img width="1924" height="890" alt="image" src="https://github.com/user-attachments/assets/891b247c-51e1-4af7-a6f7-f5612584713c" />


# Reference
1. Where to download UCSC tool: bedGraphToBigWig
```
🔽 Download for Linux:
wget https://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/bedGraphToBigWig
chmod +x bedGraphToBigWig
sudo mv bedGraphToBigWig /usr/local/bin/

🔽 Download for macOS:
wget https://hgdownload.soe.ucsc.edu/admin/exe/macOSX.x86_64/bedGraphToBigWig
chmod +x bedGraphToBigWig
sudo mv bedGraphToBigWig /usr/local/bin/
```

2. Convert methylated bed file into the standard bed file that can be processed by "bedGraphToBigWig"
```
(base) lix33@NCI-02294434-ML:~/lxwg/ad-hoc/ONT/Results/wf-human-variation/SD386613/Methylation_Analysis$ sort -k1,1 -k2,2n wf_mods.1.bedGraph > wf_mods.1.sorted.bedGraph
(base) lix33@NCI-02294434-ML:~/lxwg/ad-hoc/ONT/Results/wf-human-variation/SD386613/Methylation_Analysis$ sort -k1,1 -k2,2n wf_mods.2.bedGraph > wf_mods.2.sorted.bedGraph
```  

3. Merge overlap bed regions to make UCSC tool works
```
(1) Merge overlapped regions
(2) sort merged bed file
(3) convert bed file to bigwig file 

*** For haplotype 1 ***
(base) lix33@NCI-02294434-ML:~/lxwg/ad-hoc/ONT/Results/wf-human-variation/SD386613/Methylation_Analysis$ bedtools merge -i wf_mods.1.sorted.bedGraph -c 4 -o mean > wf_mods.1.merged.bedGraph
(base) lix33@NCI-02294434-ML:~/lxwg/ad-hoc/ONT/Results/wf-human-variation/SD386613/Methylation_Analysis$ sort -k1,1 -k2,2n wf_mods.1.merged.bedGraph > wf_mods.1.merged.sorted.bedGraph
(base) lix33@NCI-02294434-ML:~/lxwg/ad-hoc/ONT/Results/wf-human-variation/SD386613/Methylation_Analysis$ ./bedGraphToBigWig wf_mods.1.merged.sorted.bedGraph hg38.chrom.sizes wf_mods.1.bw

*** For haplotype 2 ***
(base) lix33@NCI-02294434-ML:~/lxwg/ad-hoc/ONT/Results/wf-human-variation/SD386613/Methylation_Analysis$ bedtools merge -i wf_mods.2.sorted.bedGraph -c 4 -o mean > wf_mods.2.merged.bedGraph
(base) lix33@NCI-02294434-ML:~/lxwg/ad-hoc/ONT/Results/wf-human-variation/SD386613/Methylation_Analysis$ sort -k1,1 -k2,2n wf_mods.2.merged.bedGraph > wf_mods.2.merged.sorted.bedGraph
(base) lix33@NCI-02294434-ML:~/lxwg/ad-hoc/ONT/Results/wf-human-variation/SD386613/Methylation_Analysis$ ./bedGraphToBigWig wf_mods.2.merged.sorted.bedGraph hg38.chrom.sizes wf_mods.2.bw
```

4. Summarize the the bigwig info
```
 wget http://hgdownload.soe.ucsc.edu/admin/exe/macOSX.x86_64/bigWigInfo

(base) lix33@NCI-02294434-ML:~/lxwg/ad-hoc/ONT/Results/wf-human-variation/SD386613/Methylation_Analysis$ chmod +x ./bigWigInfo 
(base) lix33@NCI-02294434-ML:~/lxwg/ad-hoc/ONT/Results/wf-human-variation/SD386613/Methylation_Analysis$ ./bigWigInfo ./wf_mods.1.bw 
version: 4
isCompressed: yes
isSwapped: 0
primaryDataSize: 7,759,067
primaryIndexSize: 45,272
zoomLevels: 10
chromCount: 1
basesCovered: 1,066,682
mean: 40.838497
min: 0.000000
max: 50.000000
std: 10.701555
```

5. Figure Illumination
- figeno gui
<img width="1482" height="757" alt="image" src="https://github.com/user-attachments/assets/4d745cf4-8297-4f51-8188-ac902801c51c" />

<img width="458" height="457" alt="image" src="https://github.com/user-attachments/assets/c65b563e-8859-4411-8d6d-5b2b8cde88de" />


