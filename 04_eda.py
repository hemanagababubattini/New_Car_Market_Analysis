import pandas as pd
import matplotlib.pyplot as plt


# =========================================================
# STEP 1: Load Dataset
# =========================================================

df = pd.read_csv("data/feature_engineered_cars.csv")

print("Dataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())


# =========================================================
# STEP 2: Create Visualization Folder
# =========================================================

import os

os.makedirs("visualizations", exist_ok=True)


# =========================================================
# UNIVARIATE ANALYSIS
# =========================================================


# ---------------------------------------------------------
# Visualization 1: Average Price Distribution
# ---------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.hist(
    df["Average_Price_Lakh"],
    bins=8,
    edgecolor="black"
)

plt.title("Distribution of Average Car Prices")
plt.xlabel("Average Price (Lakh)")
plt.ylabel("Number of Cars")

plt.tight_layout()

plt.savefig("visualizations/01_price_distribution.png")

plt.show()


# ---------------------------------------------------------
# Visualization 2: Mileage Distribution
# ---------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.hist(
    df["Average_Mileage_KMPL"],
    bins=8,
    edgecolor="black"
)

plt.title("Distribution of Average Mileage")
plt.xlabel("Average Mileage (KMPL)")
plt.ylabel("Number of Cars")

plt.tight_layout()

plt.savefig("visualizations/02_mileage_distribution.png")

plt.show()


# ---------------------------------------------------------
# Visualization 3: Fuel Type Distribution
# ---------------------------------------------------------

fuel_counts = df["Fuel_Type"].value_counts()

plt.figure(figsize=(8, 5))

plt.bar(
    fuel_counts.index,
    fuel_counts.values
)

plt.title("Distribution of Fuel Types")
plt.xlabel("Fuel Type")
plt.ylabel("Number of Cars")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("visualizations/03_fuel_distribution.png")

plt.show()


# ---------------------------------------------------------
# Visualization 4: Transmission Distribution
# ---------------------------------------------------------

transmission_counts = df["Transmission"].fillna("Unknown").value_counts()

plt.figure(figsize=(8, 5))

plt.bar(
    transmission_counts.index,
    transmission_counts.values
)

plt.title("Distribution of Transmission Types")
plt.xlabel("Transmission")
plt.ylabel("Number of Cars")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("visualizations/04_transmission_distribution.png")

plt.show()


# =========================================================
# BIVARIATE ANALYSIS
# =========================================================


# ---------------------------------------------------------
# Visualization 5: Car Model vs Average Price
# ---------------------------------------------------------

plt.figure(figsize=(12, 6))

plt.bar(
    df["Model_Name"],
    df["Average_Price_Lakh"]
)

plt.title("Car Model vs Average Price")
plt.xlabel("Car Model")
plt.ylabel("Average Price (Lakh)")

plt.xticks(rotation=75)

plt.tight_layout()

plt.savefig("visualizations/05_model_price.png")

plt.show()


# ---------------------------------------------------------
# Visualization 6: Fuel Type vs Average Price
# ---------------------------------------------------------

fuel_price = df.groupby("Fuel_Type")["Average_Price_Lakh"].mean()

plt.figure(figsize=(8, 5))

plt.bar(
    fuel_price.index,
    fuel_price.values
)

plt.title("Fuel Type vs Average Price")
plt.xlabel("Fuel Type")
plt.ylabel("Average Price (Lakh)")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("visualizations/06_fuel_price.png")

plt.show()


# ---------------------------------------------------------
# Visualization 7: Transmission vs Average Price
# ---------------------------------------------------------

transmission_price = (
    df.assign(
        Transmission=df["Transmission"].fillna("Unknown")
    )
    .groupby("Transmission")["Average_Price_Lakh"]
    .mean()
)

plt.figure(figsize=(8, 5))

plt.bar(
    transmission_price.index,
    transmission_price.values
)

plt.title("Transmission vs Average Price")
plt.xlabel("Transmission")
plt.ylabel("Average Price (Lakh)")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("visualizations/07_transmission_price.png")

plt.show()


# ---------------------------------------------------------
# Visualization 8: Mileage vs Average Price
# ---------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Average_Mileage_KMPL"],
    df["Average_Price_Lakh"]
)

plt.title("Mileage vs Average Price")
plt.xlabel("Average Mileage (KMPL)")
plt.ylabel("Average Price (Lakh)")

plt.tight_layout()

plt.savefig("visualizations/08_mileage_price.png")

plt.show()


# ---------------------------------------------------------
# Visualization 9: Engine Capacity vs Price
# ---------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Engine_CC"],
    df["Average_Price_Lakh"]
)

plt.title("Engine Capacity vs Average Price")
plt.xlabel("Engine Capacity (CC)")
plt.ylabel("Average Price (Lakh)")

plt.tight_layout()

plt.savefig("visualizations/09_engine_price.png")

plt.show()


# ---------------------------------------------------------
# Visualization 10: User Rating vs Price
# ---------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.scatter(
    df["User_Rating"],
    df["Average_Price_Lakh"]
)

plt.title("User Rating vs Average Price")
plt.xlabel("User Rating")
plt.ylabel("Average Price (Lakh)")

plt.tight_layout()

plt.savefig("visualizations/10_rating_price.png")

plt.show()


# =========================================================
# MULTIVARIATE ANALYSIS
# =========================================================


# ---------------------------------------------------------
# Visualization 11: Engine vs Price by Fuel Type
# ---------------------------------------------------------

fuel_types = df["Fuel_Type"].unique()

plt.figure(figsize=(10, 6))

for fuel in fuel_types:

    subset = df[df["Fuel_Type"] == fuel]

    plt.scatter(
        subset["Engine_CC"],
        subset["Average_Price_Lakh"],
        label=fuel
    )

plt.title("Engine Capacity vs Price by Fuel Type")
plt.xlabel("Engine Capacity (CC)")
plt.ylabel("Average Price (Lakh)")
plt.legend()

plt.tight_layout()

plt.savefig("visualizations/11_multivariate.png")

plt.show()


# ---------------------------------------------------------
# Visualization 12: Correlation Heatmap
# ---------------------------------------------------------

numeric_columns = [
    "Min_Price_Lakh",
    "Max_Price_Lakh",
    "Average_Price_Lakh",
    "Engine_CC",
    "Mileage_Min",
    "Mileage_Max",
    "Average_Mileage_KMPL",
    "Seating_Capacity",
    "User_Rating"
]

correlation = df[numeric_columns].corr()

plt.figure(figsize=(10, 8))

plt.imshow(
    correlation,
    cmap="coolwarm",
    aspect="auto"
)

plt.colorbar(label="Correlation")

plt.xticks(
    range(len(numeric_columns)),
    numeric_columns,
    rotation=75
)

plt.yticks(
    range(len(numeric_columns)),
    numeric_columns
)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig("visualizations/12_correlation_heatmap.png")

plt.show()


# =========================================================
# BASIC STATISTICAL SUMMARY
# =========================================================

print("\n==============================")
print("EDA STATISTICAL SUMMARY")
print("==============================")

print("\nPrice Statistics:")
print(df["Average_Price_Lakh"].describe())

print("\nMileage Statistics:")
print(df["Average_Mileage_KMPL"].describe())

print("\nFuel Type Counts:")
print(df["Fuel_Type"].value_counts())

print("\nTransmission Counts:")
print(df["Transmission"].fillna("Unknown").value_counts())

print("\nPrice Category Counts:")
print(df["Price_Category"].value_counts())

print("\nEngine Category Counts:")
print(df["Engine_Category"].value_counts())


# =========================================================
# FINAL MESSAGE
# =========================================================

print("\n==============================")
print("EDA COMPLETED SUCCESSFULLY!")
print("==============================")

print("\nTotal Visualizations Created: 12")

print("\nVisualization files saved inside:")
print("visualizations/")