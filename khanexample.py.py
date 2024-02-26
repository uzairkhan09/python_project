import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('food_ordering_app.db')

# Define a function to create the menu table
def create_menu_table():
    conn.execute('''CREATE TABLE IF NOT EXISTS menu (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        description TEXT NOT NULL,
                        price REAL NOT NULL)''')

# Define a function to create the orders table
def create_orders_table():
    conn.execute('''CREATE TABLE IF NOT EXISTS orders (
                        id INTEGER PRIMARY KEY,
                        menu_id INTEGER NOT NULL,
                        quantity INTEGER NOT NULL,
                        FOREIGN KEY(menu_id) REFERENCES menu(id))''')

# Create the tables
create_menu_table()
create_orders_table()
import streamlit as st

# Define a function to add a new menu item
def add_menu_item():
    name = st.text_input('Name')
    description = st.text_input('Description')
    price = st.number_input('Price', format='%.2f')
    if st.button('Add Menu Item'):
        conn.execute('INSERT INTO menu (name, description, price) VALUES (?, ?, ?)', (name, description, price))
        conn.commit()
        st.success('Menu item added!')

# Define a function to display the current menu
def display_menu():
    menu_items = conn.execute('SELECT * FROM menu').fetchall()
    for item in menu_items:
        st.write(f'{item[1]} - ${item[3]}')
        st.write(item[2])
        st.write('---')

# Define a function to take a new order
def take_order():
    menu_options = conn.execute('SELECT id, name FROM menu').fetchall()
    menu_id = st.selectbox('Select a menu item', [(item[0], item[1]) for item in menu_options])
    quantity = st.number_input('Quantity', min_value=1)
    if st.button('Place Order'):
        conn.execute('INSERT INTO orders (menu_id, quantity) VALUES (?, ?)', (menu_id, quantity))
        conn.commit()
        st.success('Order placed!')

# Define the main app function
def main():
    st.title('Food Ordering App')
    st.write('Welcome to our food ordering app! Use the buttons below to add new menu items or place an order.')
    st.write('---')
    add_menu_item()
    st.write('---')
    display_menu()
    st.write('---')
    take_order()
    st.write('---')
    st.write('Thank you for using our app!')

# Run the app
if __name__ == '__main__':
    main()
