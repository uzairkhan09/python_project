import streamlit as st
import sqlite3

# Initialize SQLite3 connection
conn = sqlite3.connect("orders.db")
cursor = conn.cursor()

# Create orders table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY,
    item TEXT,
    quantity INTEGER,
    timestamp TEXT
)
""")
conn.commit()

def add_order(item, quantity):
    cursor.execute("""
    INSERT INTO orders (item, quantity, timestamp) VALUES (?, ?, datetime('now'))
    """, (item, quantity))
    conn.commit()

def get_order_history():
    cursor.execute("""
    SELECT * FROM orders ORDER BY timestamp DESC
    """)
    return cursor.fetchall()

st.set_page_config(page_title="Food Ordering App", page_icon=":hamburger:", layout="wide")

st.title("Food Ordering App")

item_selection = st.selectbox("Select an item", ["Pizza", "Burger", "Salad"])
quantity_input = st.number_input("Enter quantity", min_value=1, value=1)

if st.button("Order", key=f"order_{item_selection}"):
    add_order(item_selection, quantity_input)
    st.success(f"Successfully ordered {quantity_input} {item_selection}!")

order_history_button = st.button("Order History", key="order_history")
if order_history_button:
    history = get_order_history()
    if not history:
        st.write("No orders yet.")
    else:
        st.write("## Order History")
        for idx, (order_id, item, quantity, timestamp) in enumerate(history):
            st.write(f"{idx + 1}. {quantity} {item} - {timestamp}")

# Close SQLite3 connection
conn.close()
