# Discussion
## Min Coverage
1. Original Question

```
(1)   --bam_min_coverage   [number]  Minimum read coverage required to run analysis. [default: 20]
For the case: SD407538
we just have 12.218x	
```

2. Comments 
   * For the target region (with BED file), it does make sense to keep the default setting as 20x
   * For the outside target region (without BED file, this is normally for the testing purpose), we should set "--bam_min_coverage" to 0x to make make sure the pipeline can keep going.

## Annotation
1. The default value of "--annotation" is true
2. We need to set it to "false" manually to disable it.

## About uBAM
1. The pipeline only accept uBAM or BAM not fastq
   * The reason is that some additional tag info (e.g., methylation info (MM, ML) tag) should be kept for downstream analysis
   * uBAM is much better than fastq to keep, save and extract these tag info.
2. How wet lab genrate bBAM instead of fastq.gz
   * As long as the wet lab does not generate aligned BAMs, the uBAM will be genereated
   * If wet lab generates aligned BAMs, only aligned BAM and fastq.gz will be generated
3. How to do alignment
   * Rob suggest use durado to do alignment first
   * Then use the aligned BAM as the input to run the wf-humane-variant pipeline.
   * Reason (why durado + wf-humane-variant VS use "wf-humane-variant" to do both alignment and downsteam analysis)
      *  The aligmment takes time. durado can take advantage of GPU nodes to do alignment which can help us save time.
      *  It we use "wf-humane-variant" to do everything, the first 10+ hours will be alignment and it takes time to know if the downstream analysis pops some errors.
      *  do the jobs separeate can help us improve running performance and make us easy debug the issues.

## Running Error "basecaller_model: null"
1. This error is caused by uBAM (convert from fastq.gz) misses the basecall_model.
2. We can use "--override_basecaller_cfg dna_r10.4.1_e8.2_400bps_sup@v4.3.0" to add this info back to BAM
3. Two models be contained by the wet-lab aligned-BAM
   * basecall_model=dna_r10.4.1_e8.2_400bps_sup@v4.3.0
   * modbase_models=dna_r10.4.1_e8.2_400bps_sup@v4.3.0_5mCG_5hmCG@v1
   * modbase_models is used to parse the methylation info while baase call.
   * basecall_model and modbase_models should match each other (both of them share the same keyword "dna_r10.4.1_e8.2_400bps_sup@v4.3.0").
4. Why basecall_model is required by the pipeline
   * This info will be used for SNP and small variant calling.
   * the pieline does not care about modbase_models
