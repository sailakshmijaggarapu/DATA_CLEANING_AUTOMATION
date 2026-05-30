import pandas as pd

df = pd.read_csv("train_dataset.csv")

print("=== BEFORE CLEANING ===")
print(f"Shape: {df.shape}")

# fix inconsistent text first so duplicate count is accurate
df["Sex"] = df["Sex"].str.strip().str.lower()
df["Embarked"] = df["Embarked"].str.strip().str.upper()

print(f"Duplicates: {df.duplicated().sum()}")
print(f"\nMissing values:\n{df.isnull().sum()}")

# remove duplicates
df.drop_duplicates(inplace=True)
print(f"\nDuplicates removed. New shape: {df.shape}")

# fill missing values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Cabin"] = df["Cabin"].fillna("Not Assigned")
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# drop columns not needed for analysis
df.drop(columns=["Ticket", "Name"], inplace=True)

# rename columns
df.rename(columns={
    "Pclass": "Passenger_Class",
    "SibSp": "Siblings_Spouses",
    "Parch": "Parents_Children"
}, inplace=True)

print("\n=== AFTER CLEANING ===")
print(f"Shape: {df.shape}")
print(f"\nMissing values remaining:\n{df.isnull().sum()}")
print(f"\nCleaned sample:\n{df.head()}")

df.to_csv("cleaned_data.csv", index=False)
print("cleaned_data.csv saved!")