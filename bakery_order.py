# filename: bakery_order.py

import streamlit as st

# Baker's product images (replace with your own URLs or local images)
cakes_img = "https://example.com/cake.jpg"  # Replace with your actual image URL
bread_img = "https://example.com/bread.jpg"  # Replace with your actual image URL
pastry_img = "https://example.com/pastry.jpg"  # Replace with your actual image URL

# Title
st.title("🍰 Baker's Delight - Order Your Favorite Treats!")

# Sidebar for Order Form
st.sidebar.header("Order Form")

def bakery_order_form():
    st.sidebar.text("Choose your item and quantity.")
    
    items = {
        "Cake": 500,  # Price per item
        "Bread": 50,  # Price per item
        "Pastry": 100  # Price per item
    }
    
    # Select product
    item_choice = st.sidebar.selectbox("Select Item", items.keys())
    
    # Select quantity
    quantity = st.sidebar.number_input(f"Quantity of {item_choice}s", 1, 10, 1)
    
    # Get user details
    customer_name = st.sidebar.text_input("Your Name")
    customer_address = st.sidebar.text_area("Your Address")
    customer_phone = st.sidebar.text_input("Your Phone Number")
    
    # Price calculation
    total_price = items[item_choice] * quantity
    
    # Submit Order Button
    if st.sidebar.button("Place Order"):
        st.sidebar.write(f"Your order for {quantity} {item_choice}(s) has been placed!")
        st.sidebar.write(f"Total Price: ₹ {total_price}")
        
        # Display order details in the main area
        st.subheader(f"Order Summary")
        st.write(f"Customer: {customer_name}")
        st.write(f"Address: {customer_address}")
        st.write(f"Phone: {customer_phone}")
        st.write(f"Item Ordered: {item_choice}")
        st.write(f"Quantity: {quantity}")
        st.write(f"Total Price: ₹ {total_price}")
        
        # Display item images
        if item_choice == "Cake":
            st.image(cakes_img, caption="Yummy Cake!")
        elif item_choice == "Bread":
            st.image(bread_img, caption="Fresh Bread!")
        elif item_choice == "Pastry":
            st.image(pastry_img, caption="Delicious Pastry!")
    
# Display order form
bakery_order_form()
