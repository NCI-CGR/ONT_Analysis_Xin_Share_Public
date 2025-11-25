# How to deploy Dorado in CGR Cluster
## Dependences
1. Reference
```
(1) T2T
/DCEG/CGF/Sequencing/ONT/Prom24/Resources/References/T2T/UCSC/hs1.fa

(2) hg38
/DCEG/CGF/Sequencing/ONT/Prom24/Resources/References/GRCh38.p2.maimcontigs.fa
```

2. dorado
```
/DCEG/Projects/Exome/SequencingData/DAATeam/Xin/ad_hoc/ONT/SourceCode/dorado/1.2.0/dorado-1.2.0-linux-x64/bin/dorado
```

3. Model
```
(1) model
/DCEG/Projects/Exome/SequencingData/DAATeam/Xin/ad_hoc/ONT/SourceCode/dorado/1.2.0/models/dna_r10.4.1_e8.2_400bps_sup@v5.2.0

(2) modifiedBaseModel
/DCEG/Projects/Exome/SequencingData/DAATeam/Xin/ad_hoc/ONT/SourceCode/dorado/1.2.0/models/dna_r10.4.1_e8.2_400bps_sup@v5.2.0_5mCG_5hmCG@v2
```
4. Kit Name
   * Depends on the specific experiment.
   * Will be provided by wetlab real time.

## Slurm Jobs script
1. Use GPU partition
2. In order to balance the running performance and computing resources
   * 4 a100 gpu cards
   * 16 cpus
3. SLURM job script (example)
   * job.dorado.sh
```
#!/bin/bash

#SBATCH --nodes=1
#SBATCH --partition=gpuq
#SBATCH --gres=gpu:a100:4
#SBATCH --ntasks-per-node=16
#SBATCH --job-name=Dorado
#SBATCH --mail-user=lix33@nih.gov
#SBATCH --mail-type=ALL
#SBATCH --time=7-00:00:00
#SBATCH --mem=100G
#SBATCH --output=dorado.gpu.stdout
#SBATCH --error=dorado.gpu.stderr

module load singularity/3.9.5
bash ./run.dorado.sh
```

## Dorado running script
1. Your input directory should contain 3 types of directory including
   * pod5_pass
   * pod5_fail
   * pod5_skip
2. Tips
   * In order to save the running time, you can create the softlink for the specific barcode-related pod5_pass and pod5_fail directories.
   * pod5_skip contains all barcode (not demultiplexed), therefore, all pod 5 files in this folder should be considered.
3. Two key steps, including
   * Basecaller: convert pods 5 to aligned BAM
      * This BAM contains all barcodes
   * demux: demultiplex the BAM based on Barcode defined in samplesheet
      * The barcodes defined in samplehsheet will come with the separate demultiplexed results.
      * All barcodes not defined in samplesheet will be put into a separate folder and treated as unclassified.
4. Please strictly follow the example below to set the parametes in the command line. Otherwise
   * You may get the BAM unaligned
   * You may get the BAM without barcode info
   * You may get nothing be demultiplexed
   * You may get the unaligned demultiplex results.
   * Again, please **strictly** follow the example below to set the parameters.
5. Example (**run.dorado.sh**)
```
#!/bin/bash

dorado="/DCEG/Projects/Exome/SequencingData/DAATeam/Xin/ad_hoc/ONT/SourceCode/dorado/1.2.0/dorado-1.2.0-linux-x64/bin/dorado"
modifiedBaseModel="/DCEG/Projects/Exome/SequencingData/DAATeam/Xin/ad_hoc/ONT/SourceCode/dorado/1.2.0/models/dna_r10.4.1_e8.2_400bps_sup@v5.2.0_5mCG_5hmCG@v2"
model="/DCEG/Projects/Exome/SequencingData/DAATeam/Xin/ad_hoc/ONT/SourceCode/dorado/1.2.0/models/dna_r10.4.1_e8.2_400bps_sup@v5.2.0"
reference="/DCEG/CGF/Sequencing/ONT/Prom24/Resources/References/T2T/UCSC/hs1.fa"

samplesheet="/DCEG/Projects/Exome/SequencingData/DAATeam/Xin/ad_hoc/ONT/Run/dorado/v1.2.0/SD386619/samplesheet.csv"

input="/DCEG/Projects/Exome/SequencingData/DAATeam/ad_hoc/ONT/Run/dorado/v1.2.0/SD386619"
EXPERIMENTNAME="20251007_1416_2E_PBE95329_69e83be9"
KITNAME="SQK-NBD114-96"

#################################################
# Run dorado (basecaller)
#################################################
date
output=./OUTPUT_BASECALLED_Customized/${EXPERIMENTNAME}
echo $input
echo $output
mkdir -p $output

echo "Step1: Run Dorado Basecaller --->"
SECONDS=0
${dorado} basecaller ${model} ${input} \
    --reference ${reference} \
    --modified-bases-models ${modifiedBaseModel} \
    --no-trim --min-qscore 10 --recursive --device cuda:all \
    --kit-name ${KITNAME} \
    --output-dir ${output}

duration=$SECONDS
echo "Running Time: $(($duration / 3600))hrs $((($duration / 60) % 60))min $(($duration % 60))sec"
echo

#################################################
# Run dorado (summary)
#################################################
echo "Step2: Create a sequencing summary file for QC --->"
BASECALLER_BAM=$(find ${output} -mindepth 3 -type d -iname "bam_pass" -exec find {} -type f -iname "*.bam" \;)
echo "BASECALLER_BAM: ${BASECALLER_BAM}"

SECONDS=0
$dorado summary ${BASECALLER_BAM} > ${output}/${EXPERIMENTNAME}\_summary.tsv

duration=$SECONDS
echo "Running Time: $(($duration / 3600))hrs $((($duration / 60) % 60))min $(($duration % 60))sec"
echo 

#################################################
# Run dorado (demux)
#################################################
# output demultiplexed bam files
echo "Step3: dorado demultiplex --->"
DIRDEMUX="$output/demux"
mkdir -p ${DIRDEMUX}
SECONDS=0
$dorado demux \
        --emit-summary \
        --sample-sheet ${samplesheet} \
        --output-dir ${DIRDEMUX} \
        --kit-name ${KITNAME} \
	      --no-trim \
        --sort-bam \
       	${BASECALLER_BAM}

duration=$SECONDS
echo "Running Time: $(($duration / 3600))hrs $((($duration / 60) % 60))min $(($duration % 60))sec"
```

## Running Results 
1. Demultiplexed results
```
/DCEG/Projects/Exome/SequencingData/DAATeam/Xin/ad_hoc/ONT/Run/dorado/v1.2.0/20251007_1416_2E_PBE95329_69e83be9/OUTPUT_BASECALLED_Customized/20251007_1416_2E_PBE95329_69e83be9/demux/10072025_AS_chrX_T2T/20251007_1816_0_PBE95329_69e83be9/bam_pass
```
2. Running results folder structure (Example)
```
lix33@nci-cgr:~/DAATeam_Xin/ad_hoc/ONT/Run/dorado/v1.2.0/20251007_1416_2E_PBE95329_69e83be9$ tree ./OUTPUT_BASECALLED_Customized/
./OUTPUT_BASECALLED_Customized/
└── 20251007_1416_2E_PBE95329_69e83be9
    ├── 10072025_AS_chrX_Test2_NBD114-96
    │   └── 10072025_AS_chrX_T2T
    │       └── 20251007_1816_2E_PBE95329_69e83be9
    │           ├── bam_fail
    │           │   ├── PBE95329_fail_69e83be9_82cba154_0.bam
    │           │   └── PBE95329_fail_69e83be9_82cba154_0.bam.bai
    │           └── bam_pass
    │               ├── PBE95329_pass_69e83be9_82cba154_0.bam
    │               └── PBE95329_pass_69e83be9_82cba154_0.bam.bai
    ├── 20251007_1416_2E_PBE95329_69e83be9_summary.tsv
    └── demux
        ├── 10072025_AS_chrX_T2T
        │   └── 20251007_1816_0_PBE95329_69e83be9
        │       └── bam_pass
        │           ├── SD386619
        │           │   ├── PBE95329_pass_SD386619_69e83be9_00000000_0.bam
        │           │   ├── PBE95329_pass_SD386619_69e83be9_00000000_0.bam.bai
        │           ├── SD407538
        │           │   ├── PBE95329_pass_SD407538_69e83be9_00000000_0.bam
        │           │   ├── PBE95329_pass_SD407538_69e83be9_00000000_0.bam.bai
        │           └── unclassified
        │               ├── PBE95329_pass_unclassified_69e83be9_00000000_0.bam
        │               └── PBE95329_pass_unclassified_69e83be9_00000000_0.bam.bai
        └── barcoding_summary.txt
```
3. Performance (Example)
```
Step1: Run Dorado Basecaller
Running Time: 9hrs 6min 19sec

Step2: Create a sequencing summary file for QC
Running Time: 0hrs 24min 4sec

Step3: dorado demultiplex
Running Time: 2hrs 48min 42sec
```
