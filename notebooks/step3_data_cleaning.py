import pandas as pd

# Load dataset
df = pd.read_csv("dataset/superstore.csv", encoding="latin1")

print("DATA CLEANING STARTED")

# Remove duplicates
df = df.drop_duplicates()

# Handle missing values
for column in df.columns:
    if df[column].isnull().sum() > 0:
        if df[column].dtype == "object":
            df[column] = df[column].fillna("Unknown")
        else:
            df[column] = df[column].fillna(df[column].median())

# Convert date columns
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors="coerce")

# Save cleaned dataset
df.to_csv("dataset/cleaned_superstore.csv", index=False)

print("\nDATA CLEANING COMPLETED")
print("Final dataset shape:", df.shape)
print("Remaining missing values:", df.isnull().sum().sum())
print("Remaining duplicates:", df.duplicated().sum())
print("\nCleaned dataset saved successfully!")
