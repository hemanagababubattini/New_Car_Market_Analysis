# 🚗 New Car Market Analysis

## 📌 Project Overview

This project analyzes new car market data collected from CarWale using web scraping techniques.

The project focuses on collecting car specifications, cleaning and transforming the data, performing exploratory data analysis, and generating business insights and recommendations.

---

## 🎯 Project Objectives

- Scrape new car information from CarWale
- Clean and preprocess the collected data
- Perform data extraction using Regular Expressions
- Create meaningful features from existing data
- Perform Exploratory Data Analysis (EDA)
- Answer important business questions
- Generate business insights
- Provide actionable recommendations

---

## 🛠️ Technologies Used

- Python
- Requests
- BeautifulSoup
- Pandas
- Regular Expressions (Regex)
- Matplotlib
- CSV
- Web Scraping

---

## 📂 Project Structure

```text
New_Car_Market_Analysis/
│
├── 01_scraping.py
├── 02_data_cleaning.py
├── 03_feature_engineering.py
├── 04_eda.py
├── 05_business_analysis.py
├── 06_business_insights.py
├── 07_recommendations.py
│
├── data/
│   ├── raw_cars.csv
│   ├── cleaned_cars.csv
│   └── feature_engineered_cars.csv
│
├── visualizations/
│   ├── 01_price_distribution.png
│   ├── 02_mileage_distribution.png
│   ├── 03_fuel_distribution.png
│   ├── 04_transmission_distribution.png
│   ├── 05_model_price.png
│   ├── 06_fuel_price.png
│   ├── 07_transmission_price.png
│   ├── 08_mileage_price.png
│   ├── 09_engine_price.png
│   ├── 10_rating_price.png
│   ├── 11_multivariate.png
│   └── 12_correlation_heatmap.png
│
└── README.md
```

---

# 🌐 1. Web Scraping

Car information was collected from CarWale using:

- `Requests`
- `BeautifulSoup`
- HTTP headers
- Dynamic car URLs

The scraped information includes:

- Car Name
- Brand
- Minimum Price
- Maximum Price
- Fuel Type
- Transmission
- Engine Capacity
- Mileage
- Seating Capacity
- User Rating

The raw data was stored in:

```text
data/raw_cars.csv
```

---

# 🧹 2. Data Cleaning

The scraped data was cleaned using Pandas.

The following cleaning operations were performed:

### Missing Values

Missing values were identified and handled using appropriate techniques such as:

- Median imputation for numerical variables
- Appropriate handling of unavailable values
- Explicit handling of non-applicable engine capacity for electric vehicles

### Duplicate Values

Duplicate records were checked and removed where necessary.

### Data Types

Numerical columns were converted into appropriate numerical data types.

---

# 🔎 3. Regular Expression (Regex)

Regular Expressions were used for multiple data-cleaning and extraction tasks.

Examples include:

1. Removing extra whitespace
2. Extracting brand names
3. Extracting model names
4. Cleaning price strings
5. Removing unwanted special characters

---

# ⚙️ 4. Feature Engineering

New features were created from the existing data.

### New Features

1. **Average_Price_Lakh**
   - Average of minimum and maximum car price.

2. **Price_Category**
   - Budget
   - Mid-Range
   - Premium

3. **Engine_Category**
   - Small Engine
   - Medium Engine
   - Large Engine

4. **Average_Mileage_KMPL**
   - Average of minimum and maximum mileage.

5. **Mileage_Category**
   - Categorizes cars based on mileage.

---

# 📊 5. Exploratory Data Analysis

EDA was performed using Matplotlib.

The analysis includes:

## Univariate Analysis

- Price Distribution
- Mileage Distribution
- Fuel Type Distribution
- Transmission Distribution

## Bivariate Analysis

- Model vs Price
- Fuel Type vs Price
- Transmission vs Price
- Mileage vs Price
- Engine Capacity vs Price
- User Rating vs Price

## Multivariate Analysis

- Engine Capacity vs Price by Fuel Type
- Correlation Heatmap

A total of **12 visualizations** were created.

---

# ❓ 6. Business Questions

The project answers the following questions:

1. Which car models have the highest average price?
2. Which car models have the lowest average price?
3. Which fuel type has the highest average price?
4. Which transmission type has the highest average price?
5. Which car models have the best mileage?
6. Does higher engine capacity generally mean higher price?
7. Which car models have the highest user ratings?
8. Which seating capacity is most common?
9. How many cars fall into each price category?
10. Which factors are strongly related to car price?

---

# 💡 7. Business Insights

The analysis provides insights into:

- Price differences between car models
- Budget and mid-range segments
- Fuel-type distribution
- Mileage performance
- Relationship between engine capacity and price
- Customer seating preferences
- User ratings
- Transmission preferences

---

# 📈 8. Business Recommendations

Based on the analysis, the following recommendations were developed:

1. Strengthen the budget car segment.
2. Promote fuel-efficient models to mileage-conscious customers.
3. Consider expanding automatic transmission options.
4. Use highly rated models in promotional campaigns.
5. Maintain a balanced product portfolio across different price segments.

---

# 🏁 9. Conclusion

This project demonstrates an end-to-end data analytics workflow starting from web scraping and continuing through data cleaning, feature engineering, exploratory data analysis, business analysis, insights, and recommendations.

The analysis helps understand pricing, mileage, engine capacity, fuel types, transmission types, seating capacity, and customer ratings across the analyzed car models.

---

## 👩‍💻 Skills Demonstrated

- Web Scraping
- Python
- Pandas
- BeautifulSoup
- Requests
- Regular Expressions
- Data Cleaning
- Feature Engineering
- Exploratory Data Analysis
- Data Visualization
- Business Analysis
- Business Insights
- Business Recommendations