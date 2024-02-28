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

# Main function to run the Streamlit app
def main():
    st.title("Food Ordering System")
    
    selected_items = display_menu()
    
    if selected_items:
        total = calculate_total(selected_items)
        st.write(f"Total Price: ${total}")

if __name__ == "__main__":
    main()
