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

