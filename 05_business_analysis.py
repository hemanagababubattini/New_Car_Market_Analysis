import pandas as pd


# =========================================================
# STEP 1: LOAD DATASET
# =========================================================

df = pd.read_csv("data/feature_engineered_cars.csv")

print("Dataset Shape:")
print(df.shape)


# =========================================================
# BUSINESS QUESTION 1
# Which car models have the highest average price?
# =========================================================

q1 = df[
    ["Model_Name", "Average_Price_Lakh"]
].sort_values(
    by="Average_Price_Lakh",
    ascending=False
)

print("\n" + "=" * 60)
print("Q1: Car Models by Average Price")
print("=" * 60)

print(q1.to_string(index=False))


# =========================================================
# BUSINESS QUESTION 2
# Which car models have the lowest average price?
# =========================================================

q2 = df[
    ["Model_Name", "Average_Price_Lakh"]
].sort_values(
    by="Average_Price_Lakh",
    ascending=True
)

print("\n" + "=" * 60)
print("Q2: Car Models by Lowest Average Price")
print("=" * 60)

print(q2.to_string(index=False))


# =========================================================
# BUSINESS QUESTION 3
# Which fuel type has the highest average price?
# =========================================================

q3 = (
    df.groupby("Fuel_Type")["Average_Price_Lakh"]
    .mean()
    .sort_values(ascending=False)
)

print("\n" + "=" * 60)
print("Q3: Average Price by Fuel Type")
print("=" * 60)

print(q3)


# =========================================================
# BUSINESS QUESTION 4
# Which transmission type has the highest average price?
# =========================================================

q4 = (
    df.assign(
        Transmission=df["Transmission"].fillna("Unknown")
    )
    .groupby("Transmission")["Average_Price_Lakh"]
    .mean()
    .sort_values(ascending=False)
)

print("\n" + "=" * 60)
print("Q4: Average Price by Transmission")
print("=" * 60)

print(q4)


# =========================================================
# BUSINESS QUESTION 5
# Which car models have the best mileage?
# =========================================================

q5 = df[
    ["Model_Name", "Average_Mileage_KMPL"]
].sort_values(
    by="Average_Mileage_KMPL",
    ascending=False
)

print("\n" + "=" * 60)
print("Q5: Car Models by Mileage")
print("=" * 60)

print(q5.to_string(index=False))


# =========================================================
# BUSINESS QUESTION 6
# Does higher engine capacity generally mean higher price?
# =========================================================

q6 = df[
    ["Model_Name", "Engine_CC", "Average_Price_Lakh"]
].sort_values(
    by="Engine_CC",
    ascending=False
)

print("\n" + "=" * 60)
print("Q6: Engine Capacity vs Price")
print("=" * 60)

print(q6.to_string(index=False))

engine_price_correlation = df[
    ["Engine_CC", "Average_Price_Lakh"]
].corr().iloc[0, 1]

print("\nEngine-Price Correlation:")
print(round(engine_price_correlation, 3))


# =========================================================
# BUSINESS QUESTION 7
# Which car models have the highest user ratings?
# =========================================================

q7 = df[
    ["Model_Name", "User_Rating"]
].sort_values(
    by="User_Rating",
    ascending=False
)

print("\n" + "=" * 60)
print("Q7: Car Models by User Rating")
print("=" * 60)

print(q7.to_string(index=False))


# =========================================================
# BUSINESS QUESTION 8
# Which seating capacity is most common?
# =========================================================

q8 = (
    df["Seating_Capacity"]
    .value_counts()
    .sort_values(ascending=False)
)

print("\n" + "=" * 60)
print("Q8: Seating Capacity Distribution")
print("=" * 60)

print(q8)

most_common_seating = q8.idxmax()

print("\nMost Common Seating Capacity:")
print(most_common_seating)


# =========================================================
# BUSINESS QUESTION 9
# How many cars fall into each price category?
# =========================================================

q9 = (
    df["Price_Category"]
    .value_counts()
)

print("\n" + "=" * 60)
print("Q9: Cars by Price Category")
print("=" * 60)

print(q9)


# =========================================================
# BUSINESS QUESTION 10
# Which factors are strongly related to car price?
# =========================================================

numeric_columns = [
    "Average_Price_Lakh",
    "Engine_CC",
    "Average_Mileage_KMPL",
    "Seating_Capacity",
    "User_Rating"
]

q10 = df[numeric_columns].corr()["Average_Price_Lakh"].sort_values(
    ascending=False
)

print("\n" + "=" * 60)
print("Q10: Factors Related to Average Price")
print("=" * 60)

print(q10)


# =========================================================
# ADDITIONAL SUMMARY
# =========================================================

print("\n" + "=" * 60)
print("OVERALL BUSINESS SUMMARY")
print("=" * 60)

print("\nTotal Car Models:")
print(len(df))

print("\nAverage Market Price:")
print(round(df["Average_Price_Lakh"].mean(), 2), "Lakh")

print("\nMinimum Average Price:")
print(round(df["Average_Price_Lakh"].min(), 2), "Lakh")

print("\nMaximum Average Price:")
print(round(df["Average_Price_Lakh"].max(), 2), "Lakh")

print("\nAverage Mileage:")
print(round(df["Average_Mileage_KMPL"].mean(), 2), "KMPL")

print("\nAverage User Rating:")
print(round(df["User_Rating"].mean(), 2))


# =========================================================
# COMPLETED
# =========================================================

print("\n" + "=" * 60)
print("BUSINESS ANALYSIS COMPLETED!")
print("=" * 60)