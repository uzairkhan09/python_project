import streamlit as st

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

# Display the user's order
st.write(f"You ordered a {food_order[1]} {food_order[0]} with the following extra toppings/requests: {food_order[2]}")
