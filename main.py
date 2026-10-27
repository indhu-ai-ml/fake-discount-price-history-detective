import pandas as pd

print("===== FAKE DISCOUNT DETECTIVE =====")

# Load product price history
data = pd.read_csv("products.csv")

print("\nProduct Price History:")
print(data)

# Analyse product prices
print("\n===== PRICE ANALYSIS =====")

for product in data["product_name"].unique():

    product_data = data[data["product_name"] == product]

    oldest_price = product_data.iloc[0]["price"]
    latest_price = product_data.iloc[-1]["price"]

    price_drop = oldest_price - latest_price

    percentage_drop = (price_drop / oldest_price) * 100

    print("\nProduct:", product)
    print("Oldest Price: Rs.", oldest_price)
    print("Latest Price: Rs.", latest_price)
    print("Price Decrease:", round(percentage_drop, 2), "%")
    # Suspicious Discount Detection

print("\n===== SUSPICIOUS DISCOUNT DETECTION =====")

for product in data["product_name"].unique():

    product_data = data[data["product_name"] == product]

    oldest_price = product_data.iloc[0]["price"]
    latest_price = product_data.iloc[-1]["price"]

    discount_percentage = (
        (oldest_price - latest_price) / oldest_price
    ) * 100

    print("\nProduct:", product)

    if discount_percentage >= 40:
        print("Status: Suspicious Discount - Please Investigate!")
    else:
        print("Status: No Major Price Drop Detected")
        # Date-by-Date Price Change Analysis

print("\n===== PRICE CHANGE HISTORY =====")

for product in data["product_name"].unique():

    product_data = data[data["product_name"] == product].copy()

    product_data["recorded_date"] = pd.to_datetime(
        product_data["recorded_date"]
    )

    product_data = product_data.sort_values("recorded_date")

    print("\nProduct:", product)

    previous_price = None

    for _, row in product_data.iterrows():

        current_price = row["price"]
        date = row["recorded_date"].strftime("%Y-%m-%d")

        print("\nDate:", date)
        print("Price: Rs.", current_price)

        if previous_price is not None:

            price_change = current_price - previous_price

            if price_change < 0:
                print("Price Decreased: Rs.", abs(price_change))

            elif price_change > 0:
                print("Price Increased: Rs.", price_change)

            else:
                print("Price Unchanged")

        previous_price = current_price
        # Price History Graph

import matplotlib.pyplot as plt

print("\n===== GENERATING PRICE HISTORY GRAPHS =====")

for product in data["product_name"].unique():

    product_data = data[data["product_name"] == product].copy()

    product_data["recorded_date"] = pd.to_datetime(
        product_data["recorded_date"]
    )

    product_data = product_data.sort_values("recorded_date")

    plt.figure(figsize=(8, 5))

    plt.plot(
        product_data["recorded_date"],
        product_data["price"],
        marker="o"
    )

    plt.title(f"Price History - {product}")
    plt.xlabel("Date")
    plt.ylabel("Price (Rs.)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()

    filename = product.replace(" ", "_").lower() + "_price_history.png"

    plt.savefig(filename)

    plt.show()

    print(f"Graph saved: {filename}")
# Latest Price Comparison Chart using Seaborn

import seaborn as sns

print("\n===== GENERATING LATEST PRICE COMPARISON =====")

latest_prices = data.copy()

latest_prices["recorded_date"] = pd.to_datetime(
    latest_prices["recorded_date"]
)

latest_prices = latest_prices.sort_values("recorded_date")

latest_prices = latest_prices.groupby(
    "product_name", as_index=False
).tail(1)

plt.figure(figsize=(9, 5))

sns.barplot(
    data=latest_prices,
    x="product_name",
    y="price"
)

plt.title("Latest Price Comparison")
plt.xlabel("Product")
plt.ylabel("Latest Price (Rs.)")

plt.xticks(rotation=15)
plt.tight_layout()

plt.savefig("latest_price_comparison.png")
plt.show()

print("Graph saved: latest_price_comparison.png")

