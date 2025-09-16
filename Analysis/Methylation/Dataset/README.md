## Dataset

1. The BAM files of WGS-scale
```
https://42basepairs.com/browse/s3/ont-open-data/giab_2025.01/basecalling/hac
```

2. the wf-human-variation outputs (including bedmethyl files) 
```
https://42basepairs.com/browse/s3/ont-open-data/giab_2025.01/analysis/wf-human-variation/hac
``` 

## Notice 
1. These are not ‘benchmarks’ in the sense that we know what the methylation status is, but these will serve to set expectations about quality control and result outputs and interpretations.
2. The "Modified BAM" is requred for Methylation-related analysis
   * Ensure Modified Base Calling Is Enabled
   * Check that your output BAM includes **MM** and **ML** tags for methylation.

