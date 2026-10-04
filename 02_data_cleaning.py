# =========================================================
# STEP 14: Load Raw Dataset
# =========================================================

import pandas as pd

df = pd.read_csv("data/raw_cars.csv")

print("Raw Dataset:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)
# =========================================================
# STEP 15: Check Missing Values
# =========================================================

print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())
# =========================================================
# STEP 16: Identify Rows with Missing Values
# =========================================================

missing_rows = df[df.isnull().any(axis=1)]

print("\nRows with Missing Values:")
print(missing_rows)
# =========================================================
# STEP 17: Fix Incorrect Transmission Value
# =========================================================

df.loc[df["Car_Name"] == "Maruti e Vitara", "Transmission"] = None

print("\nTransmission After Fix:")
print(
    df.loc[
        df["Car_Name"] == "Maruti e Vitara",
        ["Car_Name", "Fuel_Type", "Transmission"]
    ]
)
# =========================================================
# STEP 18: Calculate Median Seating Capacity
# =========================================================

seating_median = df["Seating_Capacity"].median()

print("\nMedian Seating Capacity:", seating_median)
# =========================================================
# STEP 18B: Fill Missing Seating Capacity
# =========================================================

df["Seating_Capacity"] = df["Seating_Capacity"].fillna(seating_median)

print("\nMissing Values After Seating Capacity Cleaning:")
print(df["Seating_Capacity"].isnull().sum())
# =========================================================
# STEP 18C: Calculate Mileage Median
# =========================================================

mileage_min_median = df["Mileage_Min"].median()
mileage_max_median = df["Mileage_Max"].median()

print("\nMileage Min Median:", mileage_min_median)
print("Mileage Max Median:", mileage_max_median)
# =========================================================
# STEP 18D: Fill Missing Mileage Values
# =========================================================

df["Mileage_Min"] = df["Mileage_Min"].fillna(mileage_min_median)
df["Mileage_Max"] = df["Mileage_Max"].fillna(mileage_max_median)

print("\nMissing Values After Mileage Cleaning:")
print(df[["Mileage_Min", "Mileage_Max"]].isnull().sum())
# =========================================================
# STEP 18E: Handle Missing Engine Capacity
# =========================================================

df["Engine_CC"] = df["Engine_CC"].fillna(0)

print("\nMissing Engine_CC:")
print(df["Engine_CC"].isnull().sum())
# =========================================================
# STEP 19: Final Missing Values Verification
# =========================================================

print("\nFinal Missing Values:")
print(df.isnull().sum())

print("\nTotal Missing Values:")
print(df.isnull().sum().sum())
# =========================================================
# STEP 20: Check and Remove Duplicates
# =========================================================

print("\nDuplicate Rows Before Cleaning:")
print(df.duplicated().sum())

df = df.drop_duplicates()

print("\nDuplicate Rows After Cleaning:")
print(df.duplicated().sum())
# =========================================================
# STEP 21A: Regex Cleaning - Car Name
# =========================================================

df["Car_Name"] = df["Car_Name"].str.replace(
    r"\s+",
    " ",
    regex=True
).str.strip()

print("\nCar Names After Regex Cleaning:")
print(df["Car_Name"].head())
# =========================================================
# STEP 21B: Regex Extraction - Brand
# =========================================================

df["Brand_Extracted"] = df["Car_Name"].str.extract(
    r"^(\w+)",
    expand=False
)

print("\nBrand Extracted Using Regex:")
print(df[["Car_Name", "Brand_Extracted"]].head())
# =========================================================
# STEP 21C: Regex Extraction - Model Name
# =========================================================

df["Model_Name"] = df["Car_Name"].str.extract(
    r"^\w+\s+(.*)$",
    expand=False
)

print("\nModel Names Extracted Using Regex:")
print(df[["Car_Name", "Model_Name"]].head())
# =========================================================
# STEP 21D: Regex Cleaning - Price
# =========================================================
import re
price_text = "₹7,50,000"

clean_price = re.sub(
    r"[₹,]",
    "",
    price_text
)

print("\nOriginal Price:", price_text)
print("Cleaned Price:", clean_price)
# =========================================================
# STEP 21E: Regex Cleaning - Remove Special Characters
# =========================================================

df["Model_Name"] = df["Model_Name"].str.replace(
    r"[^A-Za-z0-9\s-]",
    "",
    regex=True
)

print("\nModel Names After Regex Cleaning:")
print(df["Model_Name"].head())
# =========================================================
# STEP 22: Correct Data Types
# =========================================================

numeric_columns = [
    "Min_Price_Lakh",
    "Max_Price_Lakh",
    "Engine_CC",
    "Mileage_Min",
    "Mileage_Max",
    "Seating_Capacity",
    "User_Rating"
]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Convert Engine and Seating Capacity to integers
df["Engine_CC"] = df["Engine_CC"].astype(int)
df["Seating_Capacity"] = df["Seating_Capacity"].astype(int)

print("\nData Types After Cleaning:")
print(df.dtypes)
# =========================================================
# STEP 23: Final Cleaning Verification
# =========================================================

print("\nFinal Dataset Shape:")
print(df.shape)

print("\nFinal Missing Values:")
print(df.isnull().sum())

print("\nTotal Missing Values:")
print(df.isnull().sum().sum())

print("\nFinal Duplicate Rows:")
print(df.duplicated().sum())

print("\nFinal Dataset:")
print(df.head())
# =========================================================
# STEP 24: Save Cleaned Dataset
# =========================================================

df.to_csv(
    "data/cleaned_cars.csv",
    index=False
)

print("\nCleaned dataset saved successfully!")