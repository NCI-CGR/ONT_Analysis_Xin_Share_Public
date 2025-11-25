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

## Dorado running script (run.dorado.sh)
1. 
