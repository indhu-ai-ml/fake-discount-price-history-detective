import sqlite3
import pandas as pd

# Connect to SQLite database
connection = sqlite3.connect("price_history.db")

# Read product data from CSV
data = pd.read_csv("products.csv")

# Save data into database
data.to_sql(
    "product_prices",
    connection,
    if_exists="replace",
    index=False
)

print("Product data saved successfully!")

# Read data using SQL
result = pd.read_sql_query(
    "SELECT * FROM product_prices",
    connection
)

print("\n===== DATA FROM SQL DATABASE =====")
print(result)

# Close database connection
connection.close()
import sqlite3

# Connect to the database
connection = sqlite3.connect("price_history.db")

# Find oldest and latest prices for each product
query = """
SELECT
    product_name,
    MIN(price) AS lowest_price,
    MAX(price) AS highest_price
FROM product_prices
GROUP BY product_name;
"""

result = pd.read_sql_query(query, connection)

print("\n===== SQL PRICE ANALYSIS =====")
print(result)

connection.close()

