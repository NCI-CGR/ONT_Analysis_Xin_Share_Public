# High-level Overview

We use sample **SD386613** as an example for discussion, since it was loaded three times.

Three steps involved, including
* Adaptive sampling
* Fastq basecall
* Super Arrucate basecall
For details, please check
```
https://github.com/Bio-Developer-lxwg/ProjectRecord/blob/main/Ad-hoc/ONT/Discussion/Sep_11_2025/Reference/Adaptive_Sequencing_Explain.png
```

## What Has Already Been Clarified

1. **MinKNOW Report Based on Adaptive Sequencing**
   - The bam comes from **"fast basecall"**
   - The **20.22%** of reads refer to those located within the specified target region (**chrX**) from the **entire sample** (loaded three times).
   - The report provides a general profile of the target region (**chrX**) across the **whole flowcell**.
     - The **coverage of chrX (146.71×)** in this report reflects the coverage status across the entire sample (**159.501×**).
   - The purpose of the metrics in this report is to quickly provide a general overview of the target region (**chrX**) for the **entire sample**.
   - The option "Basecall on target reads only"
     - This means that only the reads roughly match the reference in target region will be considered
     - The reads comes from the whole sample.

2. The coverage results (chrX) from the **entire sample** and **MinKNOW Report** are similar & this is **expected**
   - 146.71x VS 159.501x

3. The BAM file from the entire sample
   - Based on "super accurate basecall" 

4. Screenshot for illustration
<img width="463" height="468" alt="image" src="https://github.com/user-attachments/assets/e1e89167-3b1d-4f98-8628-65e4dba07f2c" />


## The Issue Still Need to be Addressed (Has Been Addressed!)
1. The inconsistancy of the number of targeted reads (inside chrX) between the **human-variant pipeline** and **minKnow report** (**I think this issue can also be explained reasonably**)
   * the number of targeted reads (inside chrX)  in **minKnow report**
      * Total sequenced **"19.89M"** reads and **"4632.96K (4.6M)"** reads aligned to chrX.
      * Total chrX covered bases **"24068.13M"**.
   * the number of targeted reads (inside chrX) in **human-variant pipeline**
      * Total **"8457909 (8.4M)"** reads in target region and **"3159785 (3.16M)"** unmapped
         * (So the **Mapped** should be **8.4M - 3.16M = 5.24M**)
      * Total chrX covered bases **26,301,808,009 (26301.81M)**
   * **Addressed**
      * 4.6M is similar to 5.24M
      * 24068.13M is similar to 26301.81M
<img width="460" height="480" alt="image" src="https://github.com/user-attachments/assets/836206f3-f6a3-475f-a30f-8a856cd8663d" />

