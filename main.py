import streamlit as st

# Customizing the page
st.set_page_config(
    page_title="Vocational Assessment Portal",
    page_icon="📘",
    layout="wide"
)

# Inline CSS for styling
page_bg_color = """
    <style>
    /* Background color */
    .stApp {
        background-color: #f0f4fa;
    }

    /* Text customization */
    .title {
        color: #2b4c7e;
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
    }

    .subtitle {
        color: #527ba1;
        font-size: 25px;
        text-align: center;
    }

    /* Button styling */
    .stButton>button {
        background-color: #527ba1;
        color: white;
        border: none;
        font-size: 16px;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
    }

    .stButton>button:hover {
        background-color: #3b6a9e;
        color: white;
    }
    </style>
"""
st.markdown(page_bg_color, unsafe_allow_html=True)

# Title and subtitle
st.markdown('<p class="title">Welcome to the Vocational Assessment Portal</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Your one-stop solution for exam reporting and coversheet generation</p>', unsafe_allow_html=True)

# Add a central logo or banner (optional)
st.image("https://via.placeholder.com/800x200.png?text=Your+Banner+Here", use_column_width=True)

# Navigation buttons to other pages
st.write("### Navigate to:")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Generate Pass/Fail Reports"):
        st.experimental_set_query_params(page="pass_fail")
with col2:
    if st.button("Query Exam Results"):
        st.experimental_set_query_params(page="query_results")
with col3:
    if st.button("Generate Coversheets"):
        st.experimental_set_query_params(page="coversheets")

# Optional footer or additional information
st.write("---")
st.write("© 2024 Vocational Assessment Portal. All Rights Reserved.")
