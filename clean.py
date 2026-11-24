# Self Assessment Questions:
#1- Filling missing values feels most difficult because averages may not always be accurate. I would want to know why the data is missing.
#2- My comments explain why I filled, dropped, or kept certain values so someone else can understand my decisions.
#3- I was surprised by the 46 duplicate rows and the number of invalid dates and incorrect quantities in the original dataset.


# Exercise 1:
print("--- Exercise 1 ---")

import pandas as pd

df = pd.read_csv("data/messy_sales.csv")

print(df.info())
print(df.isnull().sum())

# Observations:
#1- Order ID has 31 missing values, so some sales have no order identifier.
#2- Order Date has 25 missing values, so some transactions have no recorded date.
#3- Region has 111 missing values, so some sales have no location information.


# Exercise 2: 
print("--- Exercise 2 ---")

df.columns = df.columns.str.lower().str.replace(" ", "_")
print(df.columns.tolist())


# Exercise 3: 
print("--- Exercise 3 ---")

print("Shape before:", df.shape)

df = df.dropna(subset=["order_id", "order_date"])
df["quantity_sold"] = df["quantity_sold"].fillna(df["quantity_sold"].mean())

print("Shape after:", df.shape)
print(df.isnull().sum())

# Exercise 4:
print("--- Exercise 4 ---")

df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

print("Dates converted to NaT:", df["order_date"].isna().sum())

df["unit_price"] = df["unit_price"].str.replace("$", "", regex=False)
df["unit_price"] = df["unit_price"].str.replace(",", "", regex=False)
df["unit_price"] = df["unit_price"].astype(float)

df["quantity_sold"] = df["quantity_sold"].astype(int)

df["revenue"] = (df["unit_price"] * df["quantity_sold"]).round(2)

print(df.dtypes)

# Exercise 5:
print("--- Exercise 5 ---")

print("Duplicate rows:", df.duplicated().sum())

df = df.drop_duplicates()

print("Shape after removing duplicates:", df.shape)

# Exercise 6:
print("--- Exercise 6 ---")

print(df.describe())

# Comments:
#1- Negative revenue could represent customer returns or refunds. These are real transactions so I'll keep them.
#2- The maximum revenue of $59,994 is higher than the median of $145.49. This could be a large bulk order or a unusual transaction.

df = df[df["quantity_sold"] != 9999]
print("Shape after removing placeholder quantities:", df.shape)

# Exercise 7:
print("--- Exercise 7 ---")

df.to_csv("data/clean_sales.csv", index=False)
cleaned_df = pd.read_csv("data/clean_sales.csv")

print(cleaned_df.info())
cleaned_df = pd.read_csv("data/clean_sales.csv", parse_dates=["order_date"])
print(cleaned_df.info())
