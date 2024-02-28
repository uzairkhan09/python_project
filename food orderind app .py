import streamlit as st
import sqlite3

# Function to initialize the database
def init_database():
    conn = sqlite3.connect('food_ordering.db')
    c = conn.cursor()

    # Create users table
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL
                )''')

    # Create orders table
    c.execute('''CREATE TABLE IF NOT EXISTS orders (
                    id INTEGER PRIMARY KEY,
                    user_id INTEGER NOT NULL,
                    total FLOAT NOT NULL,
                    order_time TEXT NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES users (id)
                )''')

    conn.commit()
    conn.close()

# Function to display about us information
def about_us():
    st.write("\nWelcome to our Food Ordering App!\n")
    st.write("We are committed to providing you with a seamless and enjoyable food ordering experience.")
    st.write("Our goal is to connect you with the best local restaurants and deliver delicious meals right to your doorstep.")
    st.write("For any inquiries or support, please visit our 'Contact Us' section.\n")

# Function to handle contacting the company
def contact_us():
    st.write("\nIf you have any questions, concerns, or feedback, please fill out the following form:")
    name = st.text_input("Name:")
    email = st.text_input("Email:")
    message = st.text_area("Message:")

    if st.button("Submit"):
        # Insert the contact us message into the database
        conn = sqlite3.connect('food_ordering.db')
        c = conn.cursor()
        c.execute("INSERT INTO users (name, email, password) VALUES (?, ?, 'contact_us')", (name, email))
        order_id = c.lastrowid
        c.execute("INSERT INTO orders (user_id, total, order_time) VALUES (?, 0, datetime('now'))", (order_id,))
        conn.commit()
        conn.close()

        st.write("\nThank you for your message! We will get back to you as soon as possible.\n")

# Main function to run the Streamlit app
def main():
    init_database()
    st.title("Food Ordering App")
    st.sidebar.title("Navigation")
    menu = st.sidebar.radio("Go to", ("About Us", "Contact Us"))

    if menu == "About Us":
        about_us()
    elif menu == "Contact Us":
        contact_us()

if __name__ == "__main__":
    main()
