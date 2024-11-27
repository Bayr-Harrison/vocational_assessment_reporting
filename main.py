import streamlit as st

# Customizing the page
st.set_page_config(
    page_title="Vocational Assessment Portal",
    page_icon="📘",
    layout="wide"
)

# Inline CSS to apply background image
background_style = """
    <style>
    .stApp {
        background: url("https://raw.githubusercontent.com/Bayr-Harrison/vocational_assessment_reporting/main/background.png");
        background-size: cover;
        background-position: center;
    }
    .title {
        color: #2b2b2b;
        font-size: 42px;
        font-weight: bold;
        text-align: center;
        font-family: 'Arial', sans-serif;
        margin-top: 20px;
    }
    .subtitle {
        color: #595959;
        font-size: 24px;
        text-align: center;
        font-family: 'Arial', sans-serif;
        margin-bottom: 40px;
    }
    .stButton>button {
        background-color: #ffffff;
        border: none;
        border-radius: 12px;
        box-shadow: 4px 4px 6px #bebebe, -4px -4px 6px #ffffff;
        font-size: 16px;
        padding: 10px 20px;
        color: #2b2b2b;
        cursor: pointer;
    }
    .stButton>button:hover {
        box-shadow: inset 2px 2px 4px #bebebe, inset -2px -2px 4px #ffffff;
    }
    </style>
"""
st.markdown(background_style, unsafe_allow_html=True)

# Content
st.markdown('<p class="title">Welcome to the Vocational Assessment Portal</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Your one-stop solution for exam reporting and coversheet generation</p>', unsafe_allow_html=True)

if st.button("Generate Pass/Fail Reports"):
    st.write("Pass/Fail Report generation!")
