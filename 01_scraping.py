import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

# =========================================================
# STEP 1: Base URL
# =========================================================

base_url = "https://www.carwale.com"

url = base_url + "/tata-cars/"

headers = {
    "User-Agent": "Mozilla/5.0"
}


# =========================================================
# STEP 2: Open Tata Cars Page
# =========================================================

response = requests.get(
    url,
    headers=headers
)

print("Status Code:", response.status_code)

soup = BeautifulSoup(
    response.text,
    "html.parser"
)

print(
    "Page Title:",
    soup.title.get_text(strip=True)
)


# =========================================================
# STEP 3: Find Brand URLs
# =========================================================

links = soup.find_all("a")

brand_urls = {}

for link in links:

    name = link.get_text(" ", strip=True)
    href = link.get("href")

    if (
        name
        and href
        and href.endswith("-cars/")
        and not href.startswith("/hi/")
    ):

        full_url = base_url + href

        brand_urls[name] = full_url


print("\n==============================")
print("BRAND URLs")
print("==============================")

for brand, brand_url in brand_urls.items():
    print(brand, "→", brand_url)

print("\nTotal Brands:", len(brand_urls))


# =========================================================
# STEP 4: Open Maruti Suzuki Page
# =========================================================

brand_url = brand_urls.get("Maruti Suzuki")

print("\nMaruti Suzuki URL:")
print(brand_url)

response = requests.get(
    brand_url,
    headers=headers
)

print("\nBrand Status Code:", response.status_code)

soup = BeautifulSoup(
    response.text,
    "html.parser"
)


# =========================================================
# STEP 5: Find Car Links
# =========================================================

car_links = soup.find_all("a")

print(
    "Total links in Maruti page:",
    len(car_links)
)


# =========================================================
# STEP 6: Extract Car URLs
# =========================================================

car_urls = []

for link in car_links:

    name = link.get_text(" ", strip=True)
    href = link.get("href")

    if not href:
        continue

    clean_href = href.split("#")[0]

    parts = clean_href.strip("/").split("/")

    if len(parts) != 2:
        continue

    if parts[0] != "maruti-suzuki-cars":
        continue

    car_name = parts[1]

    excluded_pages = [
        "expert-reviews",
        "news",
        "videos",
        "images"
    ]

    if car_name in excluded_pages:
        continue

    if "old-generation" in car_name:
        continue

    old_years = [
        "1990",
        "1999",
        "2008",
        "2010",
        "2014",
        "2015",
        "2017",
        "2018",
        "2019",
        "2020",
        "2021",
        "2022",
        "2024"
    ]

    if any(year in car_name for year in old_years):
        continue

    full_url = base_url + clean_href

    if full_url not in car_urls:
        car_urls.append(full_url)


print("\n==============================")
print("CAR URLs")
print("==============================")

for url in car_urls:
    print(url)

print("\nTotal Car URLs:", len(car_urls))


# =========================================================
# STEP 7: Select Current Cars
# =========================================================

current_cars = [
    "brezza",
    "swift",
    "dzire",
    "victoris",
    "alto-k10",
    "baleno",
    "fronx",
    "ertiga",
    "wagon-r",
    "s-presso",
    "e-vitara",
    "celerio",
    "xl6",
    "invicto",
    "jimny",
    "eeco"
]

current_car_urls = []

for url in car_urls:

    for car in current_cars:

        if f"/{car}/" in url:

            if url not in current_car_urls:
                current_car_urls.append(url)


print("\n==============================")
print("CURRENT CAR URLs")
print("==============================")

for url in current_car_urls:
    print(url)

print(
    "\nTotal Current Cars:",
    len(current_car_urls)
)


# =========================================================
# STEP 8: Function to Scrape One Car
# =========================================================

def scrape_car(car_url):

    response = requests.get(
        car_url,
        headers=headers
    )

    if response.status_code != 200:

        print(
            "Failed:",
            car_url
        )

        return None

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    page_text = soup.get_text(
        " ",
        strip=True
    )


    # -----------------------------------------------------
    # Car Name
    # -----------------------------------------------------

    car_name = soup.title.get_text(
        strip=True
    )

    car_name = car_name.split(" Price")[0]


    # -----------------------------------------------------
    # User Rating
    # -----------------------------------------------------

    rating_match = re.search(
        r"(\d+(?:\.\d+)?)\s*User Rating",
        page_text
    )

    if rating_match:
        rating = rating_match.group(1)
    else:
        rating = None


    # -----------------------------------------------------
    # Price
    # -----------------------------------------------------

    price_match = re.search(
        r"Rs\.\s*([\d.]+)\s*-\s*([\d.]+)\s*Lakh",
        page_text
    )

    if price_match:

        min_price = price_match.group(1)
        max_price = price_match.group(2)

    else:

        min_price = None
        max_price = None


    # -----------------------------------------------------
    # Engine
    # -----------------------------------------------------

    engine_match = re.search(
        r"Engine\s+(\d+)\s*cc",
        page_text
    )

    if engine_match:
        engine = engine_match.group(1)
    else:
        engine = None


    # -----------------------------------------------------
    # Fuel Type
    # -----------------------------------------------------

    fuel_match = re.search(
        r"Fuel Type\s+([A-Za-z]+)",
        page_text
    )

    if fuel_match:
        fuel_type = fuel_match.group(1)
    else:
        fuel_type = None


    # -----------------------------------------------------
    # Transmission
    # -----------------------------------------------------

    transmission_match = re.search(
        r"Key Specifications:.*?Transmission\s+([A-Za-z]+)",
        page_text
    )

    if transmission_match:
        transmission = transmission_match.group(1)
    else:
        transmission = None


    # -----------------------------------------------------
    # Mileage
    # -----------------------------------------------------

    mileage_match = re.search(
        r"Mileage\s*\(ARAI\)\s*([\d.]+)\s*to\s*([\d.]+)\s*kmpl",
        page_text
    )

    if mileage_match:

        min_mileage = mileage_match.group(1)
        max_mileage = mileage_match.group(2)

    else:

        min_mileage = None
        max_mileage = None


    # -----------------------------------------------------
    # Seating Capacity
    # -----------------------------------------------------

    seats_match = re.search(
        r"is a (\d+)\s*seater car",
        page_text,
        re.IGNORECASE
    )

    if seats_match:
        seating_capacity = seats_match.group(1)
    else:
        seating_capacity = None


    # -----------------------------------------------------
    # Create Car Dictionary
    # -----------------------------------------------------

    car_data = {

        "Car_Name": car_name,

        "Brand": "Maruti Suzuki",

        "Min_Price_Lakh": min_price,

        "Max_Price_Lakh": max_price,

        "Fuel_Type": fuel_type,

        "Transmission": transmission,

        "Engine_CC": engine,

        "Mileage_Min": min_mileage,

        "Mileage_Max": max_mileage,

        "Seating_Capacity": seating_capacity,

        "User_Rating": rating
    }

    return car_data


# =========================================================
# STEP 9: Test with Brezza
# =========================================================

print("\n==============================")
print("TESTING BREZZA")
print("==============================")


test_data = scrape_car(
    "https://www.carwale.com/maruti-suzuki-cars/brezza/"
)


print("\n==============================")
print("TEST RESULT")
print("==============================")

print(test_data)
# =========================================================
# STEP 10: Scrape All Current Cars
# =========================================================

all_cars_data = []

for url in current_car_urls:

    print("\nScraping:", url)

    data = scrape_car(url)

    if data is not None:
        all_cars_data.append(data)


print("\n==============================")
print("SCRAPING COMPLETED")
print("==============================")

print("Total Cars Scraped:", len(all_cars_data))

for car in all_cars_data:
    print(car)
# =========================================================
# STEP 11: Create DataFrame
# =========================================================

df = pd.DataFrame(all_cars_data)

print("\n==============================")
print("DATASET")
print("==============================")

print(df)

print("\nShape:", df.shape)
df.to_csv(
    "data/raw_cars.csv",
    index=False
)

print("\nRaw dataset saved successfully!")
# =========================================================
# STEP 13: Verify Raw Dataset
# =========================================================

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())