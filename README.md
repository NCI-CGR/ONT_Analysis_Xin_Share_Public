# ONT_Analysis_Xin_Share_Pubic
This is the repository that shared with all CGR internal group members and our collaborators. 

If you plan to post or update something that you believe may be private, please contact me (xin.li4@nih.gov) beforehand.

# Results
## Wet Lab Running Results
1. RawData
```
/DCEG/CGF/Sequencing/ONT/Prom24/RawData
```
2. PostRun_Analysis
```
/DCEG/CGF/Sequencing/ONT/Prom24/PostRun_Analysis
```
## Bioinformatics Analysis Running Results
1. Main directory
```
/DCEG/CGF/Sequencing/ONT/Prom24/Bioinformatics
```
2. Folder structure
   * Experiment
   * Pipeline + Version
   * SampleName/Barcode/General-description
```
./Bioinformatics/
└── Experiment
    ├── 20250701_1804_1C_PBE55027_8e8920e8
    │   ├── wf-human-variant
    │   │   └── v2.7.2
    │   │       └── SD386613
    │   └── wf-toulligqc
    │       └── v1.3
    │           └── Flowcell-level
    ├── 20250701_1804_1F_PBE54594_26fb9d5f
    │   ├── wf-human-variant
    │   │   └── v2.7.2
    │   │       └── SD407538
    │   └── wf-toulligqc
    │       └── v1.3
    │           └── Flowcell-level
    └── 20251007_1416_2E_PBE95329_69e83be9
        ├── wf-human-variant
        │   └── v2.7.2
        │       ├── barcode01
        │       └── barcode02
        └── wf-toulligqc
            └── v1.3
                ├── Flowcell-level
                ├── barcode01-based
                └── barcode02-based
```
## Notice
1. Only production-level results will be in
```
/DCEG/CGF/Sequencing/ONT/Prom24/Bioinformatics
```
3. For all testing purpose results, they will be in
```

```
