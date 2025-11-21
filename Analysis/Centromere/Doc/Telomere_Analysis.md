# Telomere Analysis (T2T)
1. Telomere analysis based on T2T BAMs.
2. Whole chromosome X explore.
3. 2 type of plots, including
   * mapq (hist and position-based)
   * coverage (regular and log-based)

## Dependences
### Telomere Bed File (T2T)
1. Directory
```
/DCEG/Projects/Exome/SequencingData/DAATeam/Xin/ad_hoc/ONT/Data/Dependence/telomere_bed/T2T
```
2. Telomere end region in chrX (T2T)
```
T2T.chm13v2.0_telomere.chrX.end.bed

chrX	154256800	154259566
```
3. Telomere start region in chrX (T2T)
```
T2T.chm13v2.0_telomere.chrX.start.bed

chrX    0       2000
```
4. Whole chrX
```
/DCEG/Projects/Exome/SequencingData/DAATeam/Xin/ad_hoc/ONT/Data/Dependence/T2T/wise_region_bed_from_downloaded/chrX.wise.region.bed
```
# Results (T2T-based; mapQ plot(smooth every 5 bps); coverage plot(regular, log))
## 20250701_1804_1C_PBE55027_8e8920e8 (SD386613, based on self-align)
### 1. Telomere start
<img width="3000" height="1500" alt="mapq hist chrX telomere start" src="https://github.com/user-attachments/assets/d98081ce-cfe6-409c-9936-9cfc8e9ff989" />
<img width="3600" height="1200" alt="chrX_mapq per base telomere start" src="https://github.com/user-attachments/assets/d7838f9c-c129-42a3-953f-054a348dd9e9" />
<img width="3600" height="1200" alt="depth_samtools_telomere chrX start" src="https://github.com/user-attachments/assets/a3c03ddd-fd33-40df-8f5d-3f900c73a9fb" />
<img width="3600" height="1200" alt="depth_samtools_telomere chrX start log" src="https://github.com/user-attachments/assets/9e87ffd1-7433-4ee2-83b8-435cdb3b3309" />


### 2. Telomere End
<img width="3000" height="1500" alt="mapq hist chrX telomere end" src="https://github.com/user-attachments/assets/081aba1c-086a-4e3b-91b4-cc2902ac9f3f" />
<img width="3600" height="1200" alt="chrX_mapq per base telomere end" src="https://github.com/user-attachments/assets/998506f7-305b-4704-8bba-f308f37092d9" />
<img width="3600" height="1200" alt="depth_samtools_telomere chrX end" src="https://github.com/user-attachments/assets/ddcd1cab-88cb-48e9-8e4a-b2f94682eda1" />
<img width="3600" height="1200" alt="depth_samtools_telomere chrX end log" src="https://github.com/user-attachments/assets/fc848c53-accf-4b22-8e1e-e6492db4af05" />


### 3. Whole ChrX
<img width="3000" height="1500" alt="mapq hist chrX" src="https://github.com/user-attachments/assets/8543154f-ca7b-4d3f-9787-4dddee87e48f" />
<img width="3600" height="1200" alt="chrX_mapq per base" src="https://github.com/user-attachments/assets/8ea08a76-7f73-46c4-a1ee-119cf2bdf4ab" />
<img width="3600" height="1200" alt="depth_samtools chrX whole" src="https://github.com/user-attachments/assets/6ae1afcd-5f1f-45bd-a957-c699c71c6247" />
<img width="3600" height="1200" alt="depth_samtools chrX whole log" src="https://github.com/user-attachments/assets/a7fecfc7-4382-4b45-9012-3cfb2eb603b6" />


## 20250701_1804_1F_PBE54594_26fb9d5f (SD407538, based on self-align)
### 1. Telomere start
<img width="3000" height="1500" alt="mapq hist chrX telomere start" src="https://github.com/user-attachments/assets/2c977d2f-b26c-40cd-aa1d-10612121872f" />
<img width="3600" height="1200" alt="chrX_mapq per base telomere start" src="https://github.com/user-attachments/assets/99ec78ec-84a3-41c7-b40d-0310dc1fb533" />
<img width="3600" height="1200" alt="depth_samtools_telomere chrX start" src="https://github.com/user-attachments/assets/313744ec-9079-47b8-8172-c336888aee72" />
<img width="3600" height="1200" alt="depth_samtools_telomere chrX start log" src="https://github.com/user-attachments/assets/2eb7cd29-fc3a-410d-b841-cc79f9bf704b" />


  
### 2. Telomere End
<img width="3000" height="1500" alt="mapq hist chrX telomere end" src="https://github.com/user-attachments/assets/e3452f8b-e3c0-4080-8a9c-344932d02ba1" />
<img width="3600" height="1200" alt="chrX_mapq per base telomere end" src="https://github.com/user-attachments/assets/26240652-9dd7-47f4-94f3-990b6735b787" />
<img width="3600" height="1200" alt="depth_samtools_telomere chrX end" src="https://github.com/user-attachments/assets/034689e4-f5f2-4969-8766-488283955b46" />
<img width="3600" height="1200" alt="depth_samtools_telomere chrX end log" src="https://github.com/user-attachments/assets/1bba8912-0379-4352-adda-8d8b25ae31e8" />



### 3. Whole ChrX
<img width="3000" height="1500" alt="mapq hist chrX" src="https://github.com/user-attachments/assets/5739e953-05a9-49f6-93c2-c7bb464fdd3c" />
<img width="3600" height="1200" alt="chrX_mapq per base" src="https://github.com/user-attachments/assets/d6220558-6025-4737-b4ea-21d41c38a813" />
<img width="3600" height="1200" alt="depth_samtools chrX whole" src="https://github.com/user-attachments/assets/d99b7018-9396-44da-94e9-b16011f8efa3" />
<img width="3600" height="1200" alt="depth_samtools chrX whole log" src="https://github.com/user-attachments/assets/50acfec5-14e5-4294-aeb5-865f08467a1f" />


## 20251007_1416_2E_PBE95329_69e83be9 (SD386619, aligned from wetlab)
### 1. Telomere start
<img width="3000" height="1500" alt="mapq hist chrX telomere start" src="https://github.com/user-attachments/assets/aa69e610-af23-4c95-baa1-a2c135bd1ee8" />
<img width="3600" height="1200" alt="chrX_mapq per base telomere start" src="https://github.com/user-attachments/assets/e9bf1977-35d9-4aa9-9482-0254e005a7ca" />
<img width="3600" height="1200" alt="depth_samtools_telomere chrX start" src="https://github.com/user-attachments/assets/478b3e69-8745-430d-8443-c7f007991245" />
<img width="3600" height="1200" alt="depth_samtools_telomere chrX start log" src="https://github.com/user-attachments/assets/cf16c2cf-f2cf-4bf1-863c-aba864788017" />


### 2. Telomere End
<img width="3000" height="1500" alt="mapq hist chrX telomere end" src="https://github.com/user-attachments/assets/b2272ab7-594a-454f-9ed4-de6944bebcc7" />
<img width="3600" height="1200" alt="chrX_mapq per base telomere end" src="https://github.com/user-attachments/assets/c3c9cb94-bb1a-4c0e-adc6-ce0ef42e1871" />
<img width="3600" height="1200" alt="depth_samtools_telomere chrX end" src="https://github.com/user-attachments/assets/66190dc0-dd6f-4583-b41d-1db92ff7d363" />
<img width="3600" height="1200" alt="depth_samtools_telomere chrX end log" src="https://github.com/user-attachments/assets/53473814-83e2-46de-811f-6e8e43c22c72" />


### 3. Whole ChrX
<img width="3000" height="1500" alt="mapq hist chrX" src="https://github.com/user-attachments/assets/687ae707-34b9-40ec-ab67-4c401f24fed7" />
<img width="3600" height="1200" alt="chrX_mapq per base" src="https://github.com/user-attachments/assets/6b14ced4-bc63-4dc9-9b96-1a6f4e43a37e" />
<img width="3600" height="1200" alt="depth_samtools chrX whole" src="https://github.com/user-attachments/assets/953c63c6-2de3-4e3c-82d2-2b96b03486d1" />
<img width="3600" height="1200" alt="depth_samtools chrX whole log" src="https://github.com/user-attachments/assets/0f66c6a1-7728-445a-9ba5-877dc5c3203c" />


## 20251007_1416_2E_PBE95329_69e83be9 (SD407538, aligned from wetlab)
### 1. Telomere start
<img width="3000" height="1500" alt="mapq hist chrX telomere start" src="https://github.com/user-attachments/assets/bb22f5f0-902a-411f-8113-a43a0acdff0e" />
<img width="3600" height="1200" alt="chrX_mapq per base telomere start" src="https://github.com/user-attachments/assets/ce7db231-8a1e-4b98-884c-4cb8fc47a69d" />
<img width="3600" height="1200" alt="depth_samtools_telomere chrX start" src="https://github.com/user-attachments/assets/ab9a9f94-7327-4c3b-9d08-b2a2f7ea640f" />
<img width="3600" height="1200" alt="depth_samtools_telomere chrX start log" src="https://github.com/user-attachments/assets/72a9efb4-2b99-4d66-a6c9-a623d62b2c62" />


### 2. Telomere End
<img width="3000" height="1500" alt="mapq hist chrX telomere end" src="https://github.com/user-attachments/assets/c23d90a5-4914-45b3-a93b-5c98d3be4515" />
<img width="3600" height="1200" alt="chrX_mapq per base telomere end" src="https://github.com/user-attachments/assets/da4c84a6-6bbb-4f1e-94e0-27912b8a84a3" />
<img width="3600" height="1200" alt="depth_samtools_telomere chrX end" src="https://github.com/user-attachments/assets/f58efb03-5a0a-4080-a98e-cf0ab9229dbd" />
<img width="3600" height="1200" alt="depth_samtools_telomere chrX end log" src="https://github.com/user-attachments/assets/cc2ea6bf-419f-4cfb-be0f-b31a9d0cecb7" />


### 3. Whole ChrX
<img width="3000" height="1500" alt="mapq hist chrX" src="https://github.com/user-attachments/assets/0fd5b217-8452-4bec-82b6-2fd3e1906230" />
<img width="3600" height="1200" alt="chrX_mapq per base" src="https://github.com/user-attachments/assets/f9115087-38b4-4b84-a895-b62c38b18728" />
<img width="3600" height="1200" alt="depth_samtools chrX whole" src="https://github.com/user-attachments/assets/1ac0c113-c5f5-4673-b713-c2731dad9af4" />
<img width="3600" height="1200" alt="depth_samtools chrX whole log" src="https://github.com/user-attachments/assets/633ae9c3-dbaa-4124-aae6-73360eb10b35" />
