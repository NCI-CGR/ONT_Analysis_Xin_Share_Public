import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sequencing_summary.txt", sep="\t", usecols=["start_time"])
df["start_hour"] = df["start_time"] // 3600

hourly_counts = df["start_hour"].value_counts().sort_index()

plt.figure(figsize=(10, 6))
hourly_counts.plot(kind="bar")

df["start_hour"].value_counts().sort_index().plot(kind="bar")
plt.xlabel("Hour since sequencing start")
plt.ylabel("Number of reads")
plt.title("Reads over time (proxy for active pores)")

plt.tight_layout()

plt.savefig("/home/lix33/DAATeam_Xin/ad_hoc/ONT/Run/SD386613/reads_per_hour.png")
