import streamlit as st
import pandas as pd

# Function to display available menu items with images
def menu_dispaly():
    st.title("banoqabil 2.0 final project")
    st.header("Menu")
    st.subheader("Select items to order:")
    
    menu_items = {
        "Pizza": ("https://imageurl/pizza.jpg", 500),
        "Burger": ("https://imageurl/burger.jpg", 400),
        "Salad": ("https://imageurl/salad.jpg", 300),
        "Pasta": ("https://imageurl/pasta.jpg", 600)
    }
    
    selected_items = {}
    for item, (image_url, price) in menu_items.items():
        quantity = st.number_input(f"{item} (Rs{price})", min_value=0, step=1, value=0)
        st.image(image_url, caption=item, use_column_width=True)
        if quantity > 0:
            selected_items[item] = (quantity, price)
            
    return selected_items

# Function to calculate total order price
def calculate_total(selected_items):
    total = sum([quantity * price for item, (quantity, price) in selected_items.items()])
    return total

# Function to display contact us section
def contact_us():
    st.header("Contact Us")
    st.write("If you have any questions or concerns, please fill out the form below:")
    
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    
    if st.button("Submit"):
        st.write("Thank you for reaching out to us! We will get back to you as soon as possible.")

# Function to display order history
def display_order_history():
    st.header("Order History")
    # Sample order history data (can be fetched from a database)
    order_history_data = {
        "Order ID": [101, 102, 103],
        "Items": ["Pizza, Burger", "Salad", "Pasta"],
        "Total Price (Rs)": [900, 600, 1200],
        "Date": ["2024-02-01", "2024-02-15", "2024-02-28"]
    }
    order_history_df = pd.DataFrame(order_history_data)
    st.dataframe(order_history_df)

# Main function to run the Streamlit app
def main():
    st.title("Food Ordering System")
    
    selected_items = display_menu()
    
    if selected_items:
        total = calculate_total(selected_items)
        st.write(f"Total Price: ₹{total}")
        if st.button("Order Now"):
            # Placeholder for order placement logic (can be saved to a database)
            st.write("Your order has been placed!")
    
    st.sidebar.title("Navigation")
    nav_option = st.sidebar.radio("Go to", ("Contact Us", "Order History", "Feedback"))
    
    if nav_option == "Contact Us":
        contact_us()
    elif nav_option == "Order History":
        display_order_history()
    elif nav_option == "Feedback":
        st.header("Feedback")
        feedback = st.text_area("Please provide your feedback here:")
        if st.button("Submit Feedback"):
            st.write("Thank you for your feedback!")

if __name__ == "__main__":
    main()
