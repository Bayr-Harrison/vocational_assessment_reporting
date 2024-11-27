import streamlit as st

# Set up page configuration
st.set_page_config(
    page_title="Vocational Assessment Portal",
    page_icon="📘",
    layout="wide"
)

# URL for the background image
background_url = "https://raw.githubusercontent.com/Bayr-Harrison/vocational_assessment_reporting/main/background.jpg"

# CSS for setting the background image
page_style = f"""
    <style>
    .stApp {{
        background-image: url("{background_url}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
    }}
    .title {{
        color: #ffffff;
        font-size: 48px;
        font-weight: bold;
        text-align: center;
        margin-top: 50px;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
    }}
    .subtitle {{
        color: #ffffff;
        font-size: 24px;
        text-align: center;
        margin-bottom: 40px;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.7);
    }}
    .description {{
        color: #ffffff;
        font-size: 18px;
        text-align: center;
        line-height: 1.6;
        margin: 0 15%;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.7);
    }}
    </style>
"""
st.markdown(page_style, unsafe_allow_html=True)

# Title and subtitle
st.markdown('<div class="title">Welcome to the Vocational Assessment Portal</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Your one-stop solution for all assessment-related reports</div>', unsafe_allow_html=True)

# Description
st.markdown("""
<div class="description">
This portal provides tools for generating various reports:
<br><br>
<strong>Pass/Fail Reports:</strong> Access detailed pass and fail statistics for theory exams.
<br>
<strong>Exam Results Query:</strong> View detailed exam results for students.
<br>
<strong>Coversheets:</strong> Generate personalized coversheets for student performance.
<br><br>
Use the navigation bar on the left to select a reporting option and begin.
</div>
""", unsafe_allow_html=True)
