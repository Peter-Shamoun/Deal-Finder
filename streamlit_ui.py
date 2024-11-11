import streamlit as st
from gpt_call import call
from PIL import Image
import os
import dotenv
import openai

st.set_page_config(page_title="Food Price Finder", layout="wide")

# Add store selection
st.title("Food Price Finder")
store = st.selectbox("Select Store", ["Valley Foods", "North Park", "Harvest"])

# Get prices based on store selection
prices = call()  # You'll need to modify call() to handle different stores

# Create a search section
st.subheader("Search for Items")
col1, col2 = st.columns([3, 1])

with col1:
    # Text input for search
    search_term = st.text_input("Search for an item", "")
    
    # Filter items based on search
    filtered_items = [key for key in prices.keys() if search_term.lower() in key[1].lower()]
    filtered_names = [i[1] for i in filtered_items]

with col2:
    # Add category filter
    categories = ["All", "Produce", "Meat", "Grocery", "Dairy", "Deli", "Kitchen"]
    category = st.selectbox("Filter by Category", categories)

# Display results in a grid
if filtered_names:
    st.subheader("Results")
    
    # Create columns for grid display
    cols = st.columns(3)
    
    price_dict = {key[1]:val for key,val in prices.items()}
    reversed_dict = {key[1]:key for key,val in prices.items()}
    
    # Display items in grid
    for idx, item in enumerate(filtered_names):
        col = cols[idx % 3]
        with col:
            # Get image path and price
            image_path = reversed_dict[item][0]
            price = price_dict[item]
            
            # Display image
            try:
                image = Image.open(rf'{image_path}')
                st.image(image, caption=item, use_column_width=True)
            except Exception as e:
                st.error(f"Error loading image for {item}")
            
            # Display price
            st.markdown(f"**Price:** {price}")
            
            # Add to shopping list button
            if st.button(f"Add to List", key=f"add_{idx}"):
                if "shopping_list" not in st.session_state:
                    st.session_state.shopping_list = []
                st.session_state.shopping_list.append((item, price))

# Shopping List Sidebar
with st.sidebar:
    st.header("Shopping List")
    if "shopping_list" in st.session_state and st.session_state.shopping_list:
        total = 0
        for item, price in st.session_state.shopping_list:
            st.write(f"{item}: {price}")
            # Extract numeric price value and add to total
            try:
                price_val = float(price.replace('$','').split()[0])
                total += price_val
            except:
                pass
        
        st.markdown("---")
        st.markdown(f"**Total: ${total:.2f}**")
        
        if st.button("Clear List"):
            st.session_state.shopping_list = []
    else:
        st.write("Your shopping list is empty")

