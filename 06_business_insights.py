import pandas as pd


# =========================================================
# STEP 1: LOAD DATASET
# =========================================================

df = pd.read_csv("data/feature_engineered_cars.csv")

print("Dataset Shape:")
print(df.shape)


# =========================================================
# INSIGHT 1
# Highest and Lowest Priced Cars
# =========================================================

highest_price_car = df.loc[
    df["Average_Price_Lakh"].idxmax()
]

lowest_price_car = df.loc[
    df["Average_Price_Lakh"].idxmin()
]

print("\n" + "=" * 70)
print("INSIGHT 1: PRICE RANGE")
print("=" * 70)

print(
    f"{highest_price_car['Model_Name']} has the highest "
    f"average price of ₹{highest_price_car['Average_Price_Lakh']:.2f} lakh."
)

print(
    f"{lowest_price_car['Model_Name']} has the lowest "
    f"average price of ₹{lowest_price_car['Average_Price_Lakh']:.2f} lakh."
)


# =========================================================
# INSIGHT 2
# Budget Cars
# =========================================================

budget_count = (
    df["Price_Category"] == "Budget"
).sum()

total_cars = len(df)

budget_percentage = (
    budget_count / total_cars
) * 100

print("\n" + "=" * 70)
print("INSIGHT 2: BUDGET SEGMENT")
print("=" * 70)

print(
    f"{budget_count} out of {total_cars} cars "
    f"({budget_percentage:.1f}%) belong to the Budget category."
)


# =========================================================
# INSIGHT 3
# Best Mileage
# =========================================================

best_mileage_car = df.loc[
    df["Average_Mileage_KMPL"].idxmax()
]

print("\n" + "=" * 70)
print("INSIGHT 3: MILEAGE")
print("=" * 70)

print(
    f"{best_mileage_car['Model_Name']} has the highest "
    f"average mileage of "
    f"{best_mileage_car['Average_Mileage_KMPL']:.2f} KMPL."
)


# =========================================================
# INSIGHT 4
# Fuel Type Dominance
# =========================================================

fuel_counts = df["Fuel_Type"].value_counts()

most_common_fuel = fuel_counts.idxmax()

most_common_fuel_count = fuel_counts.max()

print("\n" + "=" * 70)
print("INSIGHT 4: FUEL TYPE")
print("=" * 70)

print(
    f"{most_common_fuel} is the most common fuel type "
    f"with {most_common_fuel_count} car models."
)


# =========================================================
# INSIGHT 5
# Engine Capacity and Price Relationship
# =========================================================

engine_price_corr = df[
    ["Engine_CC", "Average_Price_Lakh"]
].corr().iloc[0, 1]

print("\n" + "=" * 70)
print("INSIGHT 5: ENGINE VS PRICE")
print("=" * 70)

print(
    f"The correlation between engine capacity and price "
    f"is {engine_price_corr:.3f}."
)

if engine_price_corr > 0:
    print(
        "This indicates a positive relationship: "
        "higher engine capacity generally tends to be "
        "associated with higher prices in this dataset."
    )
else:
    print(
        "The dataset shows a negative relationship between "
        "engine capacity and price."
    )


# =========================================================
# INSIGHT 6
# Seating Capacity
# =========================================================

seating_counts = (
    df["Seating_Capacity"]
    .value_counts()
)

most_common_seating = seating_counts.idxmax()

seating_count = seating_counts.max()

print("\n" + "=" * 70)
print("INSIGHT 6: SEATING CAPACITY")
print("=" * 70)

print(
    f"{most_common_seating}-seater cars are the most common, "
    f"with {seating_count} models."
)


# =========================================================
# INSIGHT 7
# User Ratings
# =========================================================

high_rating_count = (
    df["User_Rating"] >= 4.0
).sum()

rating_percentage = (
    high_rating_count / total_cars
) * 100

highest_rating_car = df.loc[
    df["User_Rating"].idxmax()
]

print("\n" + "=" * 70)
print("INSIGHT 7: USER RATINGS")
print("=" * 70)

print(
    f"{high_rating_count} out of {total_cars} models "
    f"({rating_percentage:.1f}%) have a user rating of 4.0 or above."
)

print(
    f"{highest_rating_car['Model_Name']} has the highest "
    f"user rating of {highest_rating_car['User_Rating']:.1f}."
)


# =========================================================
# INSIGHT 8
# Transmission Distribution
# =========================================================

transmission_counts = (
    df["Transmission"]
    .fillna("Unknown")
    .value_counts()
)

most_common_transmission = (
    transmission_counts.idxmax()
)

transmission_count = (
    transmission_counts.max()
)

print("\n" + "=" * 70)
print("INSIGHT 8: TRANSMISSION")
print("=" * 70)

print(
    f"{most_common_transmission} transmission is the most common "
    f"with {transmission_count} models."
)


# =========================================================
# FINAL SUMMARY
# =========================================================

print("\n" + "=" * 70)
print("8 BUSINESS INSIGHTS COMPLETED")
print("=" * 70)