import streamlit as st
import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('food_orders.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create the table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS orders
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   food_item TEXT,
                   size TEXT,
                   extra_toppings TEXT,
                   timestamp TEXT)''')

# Define a function to take food orders
def take_order():
    food_options = ["Pizza", "Burger", "Pasta", "Salad"]
    food_choice = st.selectbox("What would you like to order?", food_options)
    size_options = ["Small", "Medium", "Large"]
    size_choice = st.selectbox("What size would you like?", size_options)
    extra_toppings = st.text_input("Any extra toppings or requests?")
    return food_choice, size_choice, extra_toppings

# Display a welcome message
st.write("Welcome to the Food Ordering App!")

# Take the user's order
food_order = take_order()

# Save the order to the database
timestamp = st.timestamp('YYYY-MM-DD HH:mm:ss')
order_data = (food_order[0], food_order[1], food_order[2], timestamp)
cursor.execute("INSERT INTO orders (food_item, size, extra_toppings, timestamp) VALUES (?, ?, ?, ?)", order_data)
conn.commit()

# Display the user's order
st.write(f"You ordered a {food_order[1]} {food_order[0]} with the following extra toppings/requests: {food_order[2]}")

# Display a list of all orders
st.write("All orders:")
orders = cursor.execute("SELECT * FROM orders").fetchall()
for order in orders:
    st.write(f"{order[0]}: {order[1]} {order[2]} ({order[4]})")