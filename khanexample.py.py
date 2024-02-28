import streamlit as st

# Function to display available menu items
def display_menu():
    st.header("Menu")
    st.subheader("Select items to order:")
    
    menu_items = {
        "Pizza": 10,
        "Burger": 8,
        "Salad": 6,
        "Pasta": 12
    }
    
    selected_items = {}
    for item, price in menu_items.items():
        quantity = st.number_input(f"{item} (${price})", min_value=0, step=1, value=0)
        if quantity > 0:
            selected_items[item] = quantity
            
    return selected_items

# Function to calculate total order price
def calculate_total(selected_items):
    total = sum([quantity * price for item, quantity in selected_items.items()])
    return total

# Function to handle order placement
def place_order(selected_items, total):
    st.write("Your order has been placed successfully!")
    st.write("Order Details:")
    for item, quantity in selected_items.items():
        st.write(f"- {item}: {quantity}")
    st.write(f"Total Price: ${total}")

# Function to display contact us section
def contact_us():
    st.header("Contact Us")
    st.write("If you have any questions, concerns, or feedback, please fill out the following form:")
    name = st.text_input("Name:")
    email = st.text_input("Email:")
    message = st.text_area("Message:")
    
    if st.button("Submit"):
        st.write("\nThank you for your message! We will get back to you as soon as possible.\n")

# Function to display order history (dummy data)
def order_history():
    st.header("Order History")
    st.write("You have no recent orders.")

# Main function to run the Streamlit app
def main():
    st.title("Food Ordering System")
    st.sidebar.title("Navigation")
    
    menu_options = ["Menu", "Contact Us", "Order History"]
    choice = st.sidebar.selectbox("Go to", menu_options)
    
    if choice == "Menu":
        selected_items = display_menu()
        if selected_items:
            total = calculate_total(selected_items)
            if st.button("Place Order"):
                place_order(selected_items, total)
    elif choice == "Contact Us":
        contact_us()
    elif choice == "Order History":
        order_history()

if __name__ == "__main__":
    main()
