import pandas as pd

# Load dataset
df = pd.read_csv("dataset/superstore.csv", encoding="latin1")

print("DATASET INSPECTION")

# Check missing values
print("\nMISSING VALUES")
print(df.isnull().sum())

# Check duplicate records
print("\nDUPLICATE RECORDS")
print(df.duplicated().sum())

# Check data types
print("\nDATA TYPES")
print(df.dtypes)

# Check dataset size
print("\nDATASET SIZE")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# Unique values
print("\nUNIQUE VALUES")
print(df.nunique())
