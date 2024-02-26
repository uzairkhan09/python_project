import streamlit as st

# You can import other libraries here as needed
st.title("Food Ordering App")
st.subheader("Welcome to our delicious food ordering app!")
user_name = st.text_input("What's your name?")
cuisines = ["Italian", "Chinese", "Indian", "Mexican", "Thai"]
cuisine_choice = st.selectbox("Choose your favorite cuisine", cuisines)
dishes = {
    "Italian": ["Pizza", "Pasta", "Lasagna"],
    "Chinese": ["Fried Rice", "Noodles", "Dumplings"],
    "Indian": ["Biryani", "Curry", "Naan"],
    "Mexican": ["Tacos", "Burritos", "Quesadillas"],
    "Thai": ["Pad Thai", "Curry", "Spring Rolls"],
}

selected_dishes = st.multiselect(f"Select dishes from {cuisine_choice}", dishes[cuisine_choice])
order = {
    "name": user_name,
    "cuisine": cuisine_choice,
    "dishes": selected_dishes,
}

order_summary = f"Name: {order['name']}\nCuisine: {order['cuisine']}\nDishes: {', '.join(order['dishes'])}\n"
st.write(order_summary)

# You can calculate the total price based on your pricing for each dish
# For simplicity, let's assume each dish costs $10
total_price = len(order["dishes"]) * 10
st.write(f"Total price: ${total_price}")
if st.button("Submit Order"):
    st.write("Thank you for your order! Our team will prepare your food and notify you when it's ready.")
  
