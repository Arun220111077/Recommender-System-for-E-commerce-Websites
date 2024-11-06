import streamlit as st
import pickle
import pandas as pd

def recommend(items):
    try:
        product_index = product[product['Name'] == items].index[0]  # Get the index of the selected product
        distances = similarity[product_index]  # Get similarity scores for the selected product
        product_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        recommended_product = []
        recommended_product_post = []
        recommended_product_url = []  # To store the product URLs

        # Ensure we don't exceed the available number of products
        for i in product_list:
            recommended_product.append(product.iloc[i[0]].Name)
            recommended_product_post.append(product.iloc[i[0]].URL_image)
            recommended_product_url.append(product.iloc[i[0]].Product_URL)  # Assuming 'Product_URL' column contains the product's link

        return recommended_product, recommended_product_post, recommended_product_url
    except Exception as e:
        return [], [], []  # Return empty lists in case of any error (e.g., product not found)
        print(f"Error: {e}")

# Load the product dictionary
product_dict = pickle.load(open('Ajio_Recommender.pkl', 'rb'))
product = pd.DataFrame(product_dict)

# Load the similarity matrix
similarity = pickle.load(open('Ajio_Similarity.pkl', 'rb'))

# Ensure the index is reset correctly
product.reset_index(drop=True, inplace=True)

# Set the title of the app
st.title('E-Commerce Website Recommender System')

# Create a select box for product selection
selected_product_name = st.selectbox(
    'Select a Product',  # Label for the select box
    product['Name'].values  # Options for the select box
)

# Display recommendations when the button is clicked
if st.button('Recommend'):
    names, posters, urls = recommend(selected_product_name)

    # Check if recommendations exist
    if names:
        # Create columns for displaying each recommended product
        col1, col2, col3, col4, col5 = st.columns(5)

        # Add clickable images with URLs
        with col1:
            st.markdown(f"[![{names[0]}]({posters[0]})]({urls[0]})")
            st.write(names[0])  # Using st.write for better handling of longer text

        with col2:
            st.markdown(f"[![{names[1]}]({posters[1]})]({urls[1]})")
            st.write(names[1])  # Using st.write for better handling of longer text

        with col3:
            st.markdown(f"[![{names[2]}]({posters[2]})]({urls[2]})")
            st.write(names[2])  # Using st.write for better handling of longer text

        with col4:
            st.markdown(f"[![{names[3]}]({posters[3]})]({urls[3]})")
            st.write(names[3])  # Using st.write for better handling of longer text

        with col5:
            st.markdown(f"[![{names[4]}]({posters[4]})]({urls[4]})")
            st.write(names[4])  # Using st.write for better handling of longer text
    else:
        st.error("No recommendations found. Please try again with a different product.")