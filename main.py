import streamlit as st

# Customizing the page
st.set_page_config(
    page_title="Vocational Assessment Portal",
    page_icon="📘",
    layout="wide"
)

# Inline CSS for styling
page_style = """
    <style>
    /* Background color */
    .stApp {
        background-color: #e0e0e0; /* Light grey background */
    }

    /* Text customization */
    .title {
        color: #2b2b2b; /* Dark grey */
        font-size: 42px;
        font-weight: bold;
        text-align: center;
        font-family: 'Arial', sans-serif;
        margin-top: 20px;
    }

    .subtitle {
        color: #595959; /* Medium grey */
        font-size: 24px;
        text-align: center;
        font-family: 'Arial', sans-serif;
        margin-bottom: 40px;
    }

    /* Button container styling */
    .button-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 30px;
        margin: auto;
        margin-top: 100px; /* Space the buttons down the screen */
    }

    .button-row {
        display: flex;
        align-items: center;
        gap: 20px; /* Space between button and description */
    }

    /* Neumorphic button styling */
    .stButton>button {
        background: #e0e0e0; /* Match the background for a flat look */
        border: none;
        border-radius: 12px;
        box-shadow: 4px 4px 6px #bebebe, -4px -4px 6px #ffffff;
        font-size: 16px;
        padding: 15px 30px;
        font-family: 'Arial', sans-serif;
        color: #2b2b2b; /* Dark grey text */
        cursor: pointer;
    }

    .stButton>button:hover {
        background: #d6d6d6;
        box-shadow: inset 2px 2px 4px #bebebe, inset -2px -2px 4px #ffffff;
        color: #2b2b2b;
    }

    </style>
"""
st.markdown(page_style, unsafe_allow_html=True)

# Title and subtitle
st.markdown('<p class="title">Welcome to the Vocational Assessment Portal</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Your one-stop solution for exam reporting and coversheet generation</p>', unsafe_allow_html=True)

# Button container
st.markdown('<div class="button-container">', unsafe_allow_html=True)

# Navigation Buttons
if st.button("Generate Pass/Fail Reports"):
    st.experimental_set_query_params(page="pass_fail_report")
    st.experimental_rerun()

if st.button("Query Exam Results"):
    st.experimental_set_query_params(page="query_exam_results")
    st.experimental_rerun()

if st.button("Generate Coversheets"):
    st.experimental_set_query_params(page="generate_coversheets")
    st.experimental_rerun()

st.markdown('</div>', unsafe_allow_html=True)
