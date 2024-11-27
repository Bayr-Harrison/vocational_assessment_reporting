import streamlit as st

# Customizing the page
st.set_page_config(
    page_title="Generate Theory Exam Pass/Fail Report",
    page_icon="📘",
    layout="wide"
)

# CSS styling
page_style = """
    <style>
    .stApp {
        background-color: #e0e0e0;
    }
    .title {
        color: #2b2b2b;
        font-size: 42px;
        font-weight: bold;
        text-align: center;
        font-family: 'Arial', sans-serif;
    }
    .subtitle {
        color: #595959;
        font-size: 24px;
        text-align: center;
        font-family: 'Arial', sans-serif;
        margin-bottom: 20px;
    }
    .stButton>button {
        background: #e0e0e0;
        border: none;
        border-radius: 12px;
        box-shadow: 4px 4px 6px #bebebe, -4px -4px 6px #ffffff;
        font-size: 16px;
        padding: 10px 20px;
        font-family: 'Arial', sans-serif;
        color: #2b2b2b;
    }
    </style>
"""
st.markdown(page_style, unsafe_allow_html=True)

# Title
st.markdown('<p class="title">Pass/Fail Reporting Page</p>', unsafe_allow_html=True)

# Return to Main Page Button
if st.button("Return to Main Page"):
    st.query_params(page="main")
    st.stop()

# (Rest of your report generation code goes here)
