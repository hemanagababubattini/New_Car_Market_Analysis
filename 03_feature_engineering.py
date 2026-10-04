# =========================================================
# STEP 1: Load Cleaned Dataset
# =========================================================

import pandas as pd

df = pd.read_csv("data/cleaned_cars.csv")

print("Cleaned Dataset:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)
# =========================================================
# STEP 2: Create Average Price Feature
# =========================================================

df["Average_Price_Lakh"] = (
    df["Min_Price_Lakh"] + df["Max_Price_Lakh"]
) / 2

print("\nAverage Price:")
print(
    df[
        ["Car_Name", "Min_Price_Lakh", "Max_Price_Lakh",
         "Average_Price_Lakh"]
    ].head()
)
# =========================================================
# STEP 3: Create Price Category
# =========================================================

def price_category(price):

    if price < 10:
        return "Budget"

    elif price < 25:
        return "Mid-Range"

    else:
        return "Premium"


df["Price_Category"] = df["Average_Price_Lakh"].apply(
    price_category
)

print("\nPrice Categories:")
print(
    df[
        ["Car_Name", "Average_Price_Lakh", "Price_Category"]
    ].head(10)
)
# =========================================================
# STEP 4: Create Engine Category
# =========================================================

def engine_category(engine):

    if engine < 1200:
        return "Small Engine"

    elif engine < 1800:
        return "Medium Engine"

    else:
        return "Large Engine"


df["Engine_Category"] = df["Engine_CC"].apply(
    engine_category
)

print("\nEngine Categories:")
print(
    df[
        ["Car_Name", "Engine_CC", "Engine_Category"]
    ].head(10)
)
# =========================================================
# STEP 5: Create Average Mileage Feature
# =========================================================

df["Average_Mileage_KMPL"] = (
    df["Mileage_Min"] + df["Mileage_Max"]
) / 2

print("\nAverage Mileage:")
print(
    df[
        ["Car_Name", "Mileage_Min", "Mileage_Max",
         "Average_Mileage_KMPL"]
    ].head()
)
# =========================================================
# STEP 6: Create Mileage Category
# =========================================================

def mileage_category(mileage):

    if mileage >= 20:
        return "High Mileage"

    elif mileage >= 15:
        return "Medium Mileage"

    else:
        return "Low Mileage"


df["Mileage_Category"] = df["Average_Mileage_KMPL"].apply(
    mileage_category
)

print("\nMileage Categories:")
print(
    df[
        ["Car_Name", "Average_Mileage_KMPL", "Mileage_Category"]
    ].head(10)
)
# =========================================================
# STEP 6: Save Feature Engineered Dataset
# =========================================================

df.to_csv(
    "data/feature_engineered_cars.csv",
    index=False
)

print("\nFeature Engineered Dataset saved successfully!")