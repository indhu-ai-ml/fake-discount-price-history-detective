import streamlit as st
import pandas as pd
import sqlite3

# Website configuration
st.set_page_config(
    page_title="Fake Discount Detective",
    page_icon="🛍️",
    layout="wide"
)

# Website title
st.title("🛍️ Fake Discount & Price History Detective")

st.write(
    "Analyse product price history and identify "
    "potentially suspicious discounts."
)

st.divider()

# Load data from SQLite database
connection = sqlite3.connect("price_history.db")

data = pd.read_sql_query(
    "SELECT * FROM product_prices",
    connection
)

connection.close()

# Display product data
st.subheader("📦 Product Price History")

st.dataframe(data, use_container_width=True)

# Display total products
st.metric(
    "Total Price Records",
    len(data)
)
# Interactive Product Selection
st.divider()

st.subheader("🔎 Explore Individual Product")

# Convert recorded dates into date format
data["recorded_date"] = pd.to_datetime(data["recorded_date"])

# Get product names
product_names = sorted(data["product_name"].unique())

# Product selection dropdown
selected_product = st.selectbox(
    "Select a product",
    product_names
)

# Filter selected product data
selected_data = data[
    data["product_name"] == selected_product
].sort_values("recorded_date")

# Display selected product's price history
st.subheader(f"📊 Price History: {selected_product}")

st.dataframe(
    selected_data,
    use_container_width=True
)

# Calculate oldest and latest prices
oldest_price = selected_data.iloc[0]["price"]
latest_price = selected_data.iloc[-1]["price"]

# Calculate percentage decrease
price_decrease = oldest_price - latest_price

percentage_decrease = (
    (price_decrease / oldest_price) * 100
    if oldest_price > 0
    else 0
)

# Display price information
col1, col2, col3 = st.columns(3)

col1.metric(
    "Oldest Price",
    f"₹{oldest_price:,.0f}"
)

col2.metric(
    "Latest Price",
    f"₹{latest_price:,.0f}"
)

col3.metric(
    "Price Decrease",
    f"{percentage_decrease:.2f}%"
)

# Check suspicious price decrease
if percentage_decrease >= 40:
    st.warning(
        "⚠️ Potentially suspicious price drop! "
        "Please investigate further."
    )
else:
    st.success(
        "✅ No major price drop detected."
    )
# Interactive Price History Graph
st.divider()

st.subheader("📈 Interactive Price History Graph")

# Display price changes over time
chart_data = selected_data.set_index("recorded_date")

st.line_chart(
    chart_data["price"],
    x_label="Date",
    y_label="Price (₹)"
)

