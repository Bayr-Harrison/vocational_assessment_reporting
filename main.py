import streamlit as st

# Set up page configuration
st.set_page_config(
    page_title="Vocational Assessment Portal",
    page_icon="📘",
    layout="wide"
)

# URL for the logo image
logo_url = "https://raw.githubusercontent.com/Bayr-Harrison/vocational_assessment_reporting/main/arx_logo.png"

# CSS for dark mode styling
dark_mode_css = f"""
    <style>
    /* General page styling */
    .stApp {{
        background-color: #121212; /* Dark background */
        font-family: 'Arial', sans-serif;
        color: #E0E0E0; /* Primary font color */
    }}

    /* Logo styling */
    .logo {{
        position: absolute;
        top: 20px;
        left: 20px;
        width: 150px;
    }}

    /* Title styling */
    .title {{
        color: #FFFFFF; /* White font for title */
        font-size: 48px;
        font-weight: bold;
        text-align: center;
        margin-top: 50px;
    }}

    /* Subtitle styling */
    .subtitle {{
        color: #B0B0B0; /* Secondary gray for subtitle */
        font-size: 24px;
        text-align: center;
        margin-bottom: 40px;
    }}

    /* Description styling */
    .description {{
        color: #E0E0E0; /* Light gray for description */
        font-size: 18px;
        text-align: center;
        line-height: 1.8;
        margin: 0 15%;
    }}

    /* Footer styling */
    .footer {{
        color: #888888;
        font-size: 14px;
        text-align: center;
        margin-top: 60px;
    }}
    </style>
"""
st.markdown(dark_mode_css, unsafe_allow_html=True)

# Logo
st.markdown(f'<img src="{logo_url}" class="logo" alt="ARX Logo">', unsafe_allow_html=True)

# Title
st.markdown('<div class="title">Welcome to the Vocational Assessment Portal</div>', unsafe_allow_html=True)

# Description
st.markdown("""
<div class="description">
This portal provides tools for generating various reports:
<br><br>
<strong>Pass/Fail Reports:</strong> View Theory Exam Results: Pass Fail Report Portal.
<br>
<strong>Exam Results Query:</strong> View Theory Exams Results: General Reporting Portal.
<br>
<strong>Coversheets:</strong> View Theory Coversheet Generator.
<br><br>
Use the navigation bar on the left to select a reporting option and begin.
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">© 2024 Vocational Assessment Portal. All rights reserved.</div>', unsafe_allow_html=True)
