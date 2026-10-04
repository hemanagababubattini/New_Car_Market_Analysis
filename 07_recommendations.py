import pandas as pd


# =========================================================
# STEP 1: LOAD DATASET
# =========================================================

df = pd.read_csv("data/feature_engineered_cars.csv")


# =========================================================
# RECOMMENDATION 1
# =========================================================

print("\n" + "=" * 70)
print("RECOMMENDATION 1: STRENGTHEN THE BUDGET SEGMENT")
print("=" * 70)

budget_count = (
    df["Price_Category"] == "Budget"
).sum()

total_cars = len(df)

budget_percentage = (
    budget_count / total_cars
) * 100

print(
    f"{budget_percentage:.1f}% of the analyzed models "
    "are in the Budget segment."
)

print(
    "Recommendation: Continue focusing on affordable models "
    "to attract price-sensitive customers."
)


# =========================================================
# RECOMMENDATION 2
# =========================================================

print("\n" + "=" * 70)
print("RECOMMENDATION 2: PROMOTE FUEL-EFFICIENT MODELS")
print("=" * 70)

best_mileage_car = df.loc[
    df["Average_Mileage_KMPL"].idxmax()
]

print(
    f"{best_mileage_car['Model_Name']} has the highest "
    f"average mileage of "
    f"{best_mileage_car['Average_Mileage_KMPL']:.2f} KMPL."
)

print(
    "Recommendation: Highlight high-mileage models in "
    "marketing campaigns for fuel-conscious customers."
)


# =========================================================
# RECOMMENDATION 3
# =========================================================

print("\n" + "=" * 70)
print("RECOMMENDATION 3: EXPAND AUTOMATIC OPTIONS")
print("=" * 70)

transmission_counts = (
    df["Transmission"]
    .fillna("Unknown")
    .value_counts()
)

print("Transmission distribution:")
print(transmission_counts)

print(
    "Recommendation: Consider increasing automatic "
    "transmission options to serve customers who prefer "
    "convenience and easier city driving."
)


# =========================================================
# RECOMMENDATION 4
# =========================================================

print("\n" + "=" * 70)
print("RECOMMENDATION 4: FOCUS ON HIGH-RATED MODELS")
print("=" * 70)

high_rating_models = df[
    df["User_Rating"] >= 4.0
][
    ["Model_Name", "User_Rating"]
].sort_values(
    by="User_Rating",
    ascending=False
)

print("High-rated models:")
print(high_rating_models.to_string(index=False))

print(
    "Recommendation: Use highly rated models in promotional "
    "campaigns and customer recommendation strategies."
)


# =========================================================
# RECOMMENDATION 5
# =========================================================

print("\n" + "=" * 70)
print("RECOMMENDATION 5: MAINTAIN A BALANCED PRODUCT PORTFOLIO")
print("=" * 70)

price_distribution = (
    df["Price_Category"]
    .value_counts()
)

print("Price category distribution:")
print(price_distribution)

print(
    "Recommendation: Maintain a balanced portfolio covering "
    "Budget, Mid-Range and Premium segments so that different "
    "customer groups can be served."
)


# =========================================================
# FINAL
# =========================================================

print("\n" + "=" * 70)
print("5 BUSINESS RECOMMENDATIONS COMPLETED")
print("=" * 70)