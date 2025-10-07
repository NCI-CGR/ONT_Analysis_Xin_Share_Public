# BAM Statistical Info
## General Info
We summarize the information from 2 samples, including
* SD386613
* SD407538
### SD386613
1. wf-human-variant pipeline results
```
/DCEG/Projects/Exome/SequencingData/DAATeam/Xin/ad_hoc/ONT/Run/SD386613/output
```
2. Merged CRAM
```
/DCEG/Projects/Exome/SequencingData/DAATeam/Xin/ad_hoc/ONT/Run/SD386613/output/SD386613.haplotagged.cram
```
3. Original BAM and fastq
```
/DCEG/Projects/Exome/SequencingData/DAATeam/Xin/ad_hoc/ONT/Data/SD386613
this is the softlink of "/DCEG/CGF/Sequencing/ONT/Prom24/PostRun_Analysis/20250701_1804_1C_PBE55027_8e8920e8/pass"
```
4. ToulingQC results
```
/DCEG/Projects/Exome/SequencingData/DAATeam/Xin/ad_hoc/ONT/Run/wf-toulligqc/v1.3/SD386613/output
```
5. MinKnow Report (from wetlab)
```
Original:
/DCEG/CGF/Sequencing/ONT/Prom24/RawData/AS_chrX_ONT_training_07012025/SD386613/20250701_1804_1C_PBE55027_8e8920e8/report_PBE55027_20250701_1806_8e8920e8.html
Backup:
/DCEG/Projects/Exome/SequencingData/DAATeam/Xin/ad_hoc/ONT/Run/MinKnow/SD386613/report_PBE55027_20250701_1806_8e8920e8.html
```

### SD407538
1. wf-human-variant pipeline results
```
/DCEG/Projects/Exome/SequencingData/DAATeam/Xin/ad_hoc/ONT/Run/SD407538/output
```
2. Merged CRAM
```
/DCEG/Projects/Exome/SequencingData/DAATeam/Xin/ad_hoc/ONT/Run/SD407538/output/SD407538.haplotagged.cram
```
3. Original BAM and fastq
```
/DCEG/Projects/Exome/SequencingData/DAATeam/Xin/ad_hoc/ONT/Data/SD407538
this is the softlink of "/DCEG/CGF/Sequencing/ONT/Prom24/PostRun_Analysis/20250701_1804_1F_PBE54594_26fb9d5f/pass"
```
4. ToulingQC results
```
/DCEG/Projects/Exome/SequencingData/DAATeam/Xin/ad_hoc/ONT/Run/wf-toulligqc/v1.3/SD407538/output
```
5. MinKnow Report (from wetlab)
```
Original:
/DCEG/CGF/Sequencing/ONT/Prom24/RawData/AS_chrX_ONT_training_07012025/SD407538/20250701_1804_1F_PBE54594_26fb9d5f/report_PBE54594_20250701_1810_26fb9d5f.html
Backup:
/DCEG/Projects/Exome/SequencingData/DAATeam/Xin/ad_hoc/ONT/Run/MinKnow/SD407538/report_PBE54594_20250701_1810_26fb9d5f.html
```

### Other Running Results 
1. on-target, off-target, total reads 
```
/DCEG/Projects/Exome/SequencingData/DAATeam/Xin/ad_hoc/ONT/Run/customized_script/BAM_Report
```

## Statistical Table
### Samtools-Based
| | SD386613 | SD407538 | Definition | Commnets |
| :--  | :--      | :--   | :--   | :--   | 
| On-target reads | 5457428 | 2380591 | Number of reads be assgined to chrX (bed file) | <br>(1)based on cram and samtools <br>(2)cram is from wf-human-variant pipeline <br>(3)total number of unique reads in chrX |
| Off-taget reads | 98832126 | 57046206 | Number of reads NOT be assgined to chrX |<br>(1)based on cram and samtools <br>(2)cram is from wf-human-variant pipeline <br>(3)(total number of reads) - ("on-target" reads) |
| Total reads | 104289554 | 59426797 | Total number of reads | <br>(1)based on cram and samtools <br>(2)cram is from wf-human-variant pipeline (3)total number of unique reads |

### Pipeline-Report-Based
| | SD386613 | SD407538 | Definition | Commnets |
| :--  | :--      | :--   | :--   | :--   | 
| <br>(1)Total based called reads <br>(2)High Quality Reads <br>(3)Low Quality Reads | <br>110026219 <br>101129796(91.91%) <br>8896423(8.09%) | <br>62908003 <br>57425882(91.29%) <br>5482121(8.71%) | <br>(1)Total reads from **super accurate basecall** <br>(2)**Pass**: The read passed the basecaller's filters ( Q ≥ 8 same as the settings in MinKnow) <br>(3)**Fail**: The read failed basecalling QC (short, noisy, etc.) | <br>(1) From **wf-ToulligQC** <br>(2)Based on **sequencing_summary.txt** <br>(3)Based on passes_filtering == TRUE and passes_filtering == FALSE <br>(4)High Quality Reads: Pass <br>(5)Low Quality Reads: Fail |
| <br>(1)Accepted reads <br>(2)High Quality Reads <br>(3)Low Quality Reads | <br>22.27M <br>19.89M <br>2.38M | <br>11.25M <br>8.73M <br>2.52M | <br>(1)Reads accepcted by **fast basecall** <br>(2) Based on the provided BED file <br>(3)**Pass**: Out of those Q≥8 reads, and passed all the basecaller’s quality filters <br>(4)**Fail**: Q≥8 but failed other filters (such as being too short, or failing signal-level filtering)| <br>(1)based on **MinKnow Report** <br>(2)High Quality Reads: Pass <br>(3)Low Quality Reads: Fail |
| Rejected reads | (Total based called reads)- (Accepted reads) | (Total based called reads)- (Accepted reads) | | Based on toullingQC and MinKnow Report|
| Sample mean coverage (all chroms) | 26.373x | 12.218x | | <br>Based on wf-human-variant pipeline **without** BED file|
| Sample mean coverage (chrX) | 159.501x | 34.452x | | <br>Based on wf-human-variant pipeline **without** BED file|



