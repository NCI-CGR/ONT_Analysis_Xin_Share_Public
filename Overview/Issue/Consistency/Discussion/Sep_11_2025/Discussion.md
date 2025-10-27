# Dataset
## 20% Reads
1. SD386613
   * Total Size of Passed BAM(aligned): 63 GB
```
/DCEG/CGF/Sequencing/ONT/Prom24/RawData/AS_chrX_ONT_training_07012025/SD386613/20250701_1804_1C_PBE55027_8e8920e8/bam_pass
```
2. SD407538
   * Total Size of Passed BAM(aligned): 19.63 GB
```
/DCEG/CGF/Sequencing/ONT/Prom24/RawData/AS_chrX_ONT_training_07012025/SD407538/20250701_1804_1F_PBE54594_26fb9d5f/bam_pass
```
## Whole Flowcell
1. SD386613
   * Reload 3 times
   * Total Size of Passed BAM(aligned): 148.68 GB
```
/DCEG/CGF/Sequencing/ONT/Prom24/PostRun_Analysis/20250701_1804_1C_PBE55027_8e8920e8/pass
```
2. SD407538
   * Only load one time
   * Total Size of Passed BAM(aligned): 77.50 GB
```
/DCEG/CGF/Sequencing/ONT/Prom24/PostRun_Analysis/20250701_1804_1F_PBE54594_26fb9d5f/pass
```
# Discussions
1. The coverage issue between "20% Reads" and "Whole Flowcell"
2. The reads number in chrX VS reads number in the whoe BAM
3. The consistancy between the results from self-count and toulling QC

## The coverage issue between "20% Reads" and "Whole Flowcell"
### Output From humane-variant pipeline
We use 4 types of results for quick evaluation, including 
   * bed_summary.tsv
   * flagstat.tsv
   * mosdepth.summary.txt
   * reads_per_hour.png (draw it based on "sequencing_summary.txt" from my code)

1. SD386613
```
(1) "20% Reads" 
    a) General reslts: https://github.com/Bio-Developer-lxwg/ProjectRecord/tree/main/Ad-hoc/ONT/Discussion/Sep_11_2025/Results

(2) Whole Flowcell
    a) General reslts: https://github.com/Bio-Developer-lxwg/ProjectRecord/tree/main/Ad-hoc/ONT/Discussion/Sep_11_2025/Results
    b) Plot of reads_per_hour: https://github.com/Bio-Developer-lxwg/ProjectRecord/tree/main/Ad-hoc/ONT/Discussion/Sep_11_2025/Results/Whole_Flowcell_huname_variant_pipeline_SD386613_reads_per_hour.png
```
```
Interpretation of the Plot (based on "sequencing_summary.txt"):

Very high throughput during the first ~5 hours: Each hour generated ~2.5–3 million reads.

After that, a gradual decline in hourly reads — almost exponential.

By hour 30–40, the output drops to ~700k reads/hour or even lower.

🧠 What does this mean?
✅ The early part of the run was very successful:

Active pores were high.

Library was successfully loaded.

❌ After ~20 hours:

Read output steadily decreased.

No visible "spikes" or recovery after any reloads.

This suggests that your multiple reloads didn’t meaningfully increase output.
```
   
2. SD407538
```
(1) "20% Reads" 
    a) General reslts: https://github.com/Bio-Developer-lxwg/ProjectRecord/tree/main/Ad-hoc/ONT/Discussion/Sep_11_2025/Results

(2) Whole Flowcell
    a) General reslts: https://github.com/Bio-Developer-lxwg/ProjectRecord/tree/main/Ad-hoc/ONT/Discussion/Sep_11_2025/Results
    b) Plot of reads_per_hour: https://github.com/Bio-Developer-lxwg/ProjectRecord/tree/main/Ad-hoc/ONT/Discussion/Sep_11_2025/Results/Whole_Flowcell_huname_variant_pipeline_SD407538_reads_per_hour.png
```
```
Interpretation of the Plot (based on "sequencing_summary.txt"):
✅ Early Phase (0–5 hours):

Very high throughput (≈ 3 million reads/hour)

This is expected — pores are most active, and the first library load is effective.

📉 Gradual Decline (~6–30 hours):

Reads per hour slowly decreases, likely due to:

Pore exhaustion or deactivation

Natural loss of sequencing efficiency

Depletion of loaded library

📈 Sudden Spikes (notably at ~17h, ~33h, ~38h):

These spikes suggest that you reloaded the flowcell at those points.

You can clearly see read counts jump temporarily (e.g., from ~1.1M/hour → ~2.5M/hour).

❌ Post-Spike Behavior:

After each spike, reads/hour again declines steadily.

This suggests that:

Reloads temporarily help, but

Do not sustain long-term increases in yield.

🧠 Key Insights:
Observation	Interpretation
Initial high throughput	Good library and active pores
Declining trend	Normal sequencing behavior, pores deactivating
Spikes at ~17h, 33h, 38h	Likely reload events or flowcell flushes
No long-term gain from reloads	Likely limited pore recovery or suboptimal reload conditions
```
