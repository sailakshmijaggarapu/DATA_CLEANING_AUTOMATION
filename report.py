import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cleaned_data.csv")

# summary statistics
summary = df.describe()
summary.to_csv("summary_report.csv")
print("Summary Report:")
print(summary)

# Chart 1 - Survival count
plt.figure(figsize=(6, 4))
df["Survived"].value_counts().plot(kind="bar", color=["red", "green"], edgecolor="black")
plt.title("Survival Count (0 = No, 1 = Yes)")
plt.xlabel("Survived")
plt.ylabel("Number of Passengers")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("survival_count.png")
plt.close()

# Chart 2 - Passengers by class
plt.figure(figsize=(6, 4))
df["Passenger_Class"].value_counts().sort_index().plot(kind="bar", color=["blue", "purple", "orange"], edgecolor="black")
plt.title("Passengers by Class")
plt.xlabel("Passenger Class")
plt.ylabel("Count")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("passengers_by_class.png")
plt.close()

# Chart 3 - Age distribution
plt.figure(figsize=(7, 4))
df["Age"].plot(kind="hist", bins=20, color="blue", edgecolor="black")
plt.title("Age Distribution of Passengers")
plt.xlabel("Age")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("age_distribution.png")
plt.close()

# Chart 4 - Survival rate by gender
plt.figure(figsize=(6, 4))
df.groupby("Sex")["Survived"].mean().plot(kind="bar", color=["red", "blue"], edgecolor="black")
plt.title("Survival Rate by Gender")
plt.xlabel("Gender")
plt.ylabel("Survival Rate")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("survival_by_gender.png")
plt.close()

print("All charts and report saved!")