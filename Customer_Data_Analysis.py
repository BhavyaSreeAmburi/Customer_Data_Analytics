import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------
# CUSTOMER DATA ANALYSIS
# -----------------------------------

# Read the customer dataset
data = pd.read_csv("customer_data.csv")

# Display the first 5 rows
print("----- CUSTOMER DATA -----")
print(data.head())

# -----------------------------------
# DATA CLEANING
# -----------------------------------

print("\n----- MISSING VALUES -----")
print(data.isnull().sum())

# Remove duplicate rows if any
data = data.drop_duplicates()

# -----------------------------------
# BASIC DATA ANALYSIS
# -----------------------------------

average_purchase = data["Purchase_Amount"].mean()
total_purchase = data["Purchase_Amount"].sum()
highest_purchase = data["Purchase_Amount"].max()
lowest_purchase = data["Purchase_Amount"].min()

print("\n----- PURCHASE ANALYSIS -----")
print("Average Purchase Amount:", average_purchase)
print("Total Purchase Amount:", total_purchase)
print("Highest Purchase Amount:", highest_purchase)
print("Lowest Purchase Amount:", lowest_purchase)

# -----------------------------------
# PRODUCT-WISE ANALYSIS
# -----------------------------------

product_sales = data.groupby("Product")["Purchase_Amount"].sum()

print("\n----- PRODUCT-WISE SALES -----")
print(product_sales)

# -----------------------------------
# CITY-WISE ANALYSIS
# -----------------------------------

city_sales = data.groupby("City")["Purchase_Amount"].sum()

print("\n----- CITY-WISE SALES -----")
print(city_sales)

# -----------------------------------
# GENDER-WISE ANALYSIS
# -----------------------------------

gender_sales = data.groupby("Gender")["Purchase_Amount"].sum()

print("\n----- GENDER-WISE PURCHASE -----")
print(gender_sales)

# -----------------------------------
# FINAL INSIGHTS
# -----------------------------------

top_product = product_sales.idxmax()
top_city = city_sales.idxmax()
top_customer = data.loc[data["Purchase_Amount"].idxmax(), "Name"]

print("\n----- CUSTOMER DATA ANALYSIS INSIGHTS -----")
print("Top Selling Product:", top_product)
print("Best Performing City:", top_city