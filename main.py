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
    .button-container {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        justify-content: center;
        gap: 20px;
        margin: auto;
        width: 60%; /* Adjust the width of the container for alignment */
        max-width: 400px; /* Prevent it from being too wide */
        margin-top: 100px; /* Space the buttons down the screen */
    }

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

    /* Logo placement */
    .logo {
        position: absolute;
        top: 20px;
        left: 20px;
        width: 300px;
        height: auto;
    }
    </style>
"""
st.markdown(page_bg_color, unsafe_allow_html=True)

# Logo in the top-left corner
logo_url = "https://raw.githubusercontent.com/Bayr-Harrison/vocational_assessment_reporting/main/arx_logo.png"
st.markdown(f'<img class="logo" src="{logo_url}" alt="ARX Logo">', unsafe_allow_html=True)

# Title and subtitle
st.markdown('<p class="title">Welcome to the Vocational Assessment Portal</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Your one-stop solution for exam reporting and coversheet generation</p>', unsafe_allow_html=True)

# Button container for alignment and descriptions
st.markdown('<div class="button-container">', unsafe_allow_html=True)

# Pass/Fail Reports Button
if st.button("Generate Pass/Fail Reports"):
    st.experimental_set_query_params(page="pass_fail")
st.write("✔ **Generate a comprehensive report** that shows pass and fail statistics for theory exams within a selected period.")

# Query Exam Results Button
if st.button("Query Exam Results"):
    st.experimental_set_query_params(page="query_results")
st.write("✔ **Query detailed exam results**, including scores and attendance, for a specific date range.")

# Coversheets Button
if st.button("Generate Coversheets"):
    st.experimental_set_query_params(page="coversheets")
st.write("✔ **Generate individualized coversheets** summarizing each student's exam performance.")

st.markdown('</div>', unsafe_allow_html=True)
