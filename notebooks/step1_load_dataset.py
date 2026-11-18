import pandas as pd

# Load dataset
df = pd.read_csv("dataset/superstore.csv", encoding="latin1")

# Display first 5 rows
print("FIRST 5 ROWS OF DATASET")
print(df.head())

# Dataset information
print("\nDATASET INFORMATION")
print(df.info())

# Dataset shape
print("\nDATASET SHAPE")
print(df.shape)

# Column names
print("\nCOLUMN NAMES")
print(df.columns.tolist())

# Statistical summary
print("\nSTATISTICAL SUMMARY")
print(df.describe())
