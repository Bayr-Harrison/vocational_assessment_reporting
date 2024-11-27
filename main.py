import streamlit as st

# Set up page configuration
st.set_page_config(
    page_title="Vocational Assessment Portal",
    page_icon="📘",
    layout="wide"
)

# Logo URL
logo_url = "https://raw.githubusercontent.com/Bayr-Harrison/vocational_assessment_reporting/main/arx_logo.png"

# Custom CSS for design
custom_css = f"""
    <style>
    /* General page styling */
    .stApp {{
        background-color: #1E1E2F; /* Deep navy background */
        color: #E0E0E0; /* Light gray text */
        font-family: 'Arial', sans-serif;
    }}

    /* Logo styling */
    .logo {{
        display: block;
        margin: 20px auto;
        width: 180px;
    }}

    /* Title styling */
    .title {{
        color: #FFFFFF;
        font-size: 50px;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 10px;
    }}

    /* Subtitle styling */
    .subtitle {{
        color: #A0A0A0;
        font-size: 22px;
        text-align: center;
        margin-bottom: 40px;
    }}

    /* Card container */
    .card-container {{
        display: flex;
        justify-content: center;
        align-items: flex-start;
        gap: 20px; /* Space between cards */
        margin-top: 40px;
        flex-wrap: nowrap; /* Prevents wrapping of cards */
    }}

    /* Card styling */
    .card {{
        background: #28293E;
        border-radius: 15px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
        padding: 20px;
        width: 300px;
        text-align: center;
    }}

    .card-title {{
        color: #FFFFFF;
        font-size: 20px;
        font-weight: bold;
        margin-bottom: 10px;
    }}

    .card-description {{
        color: #B0B0B0;
        font-size: 16px;
        line-height: 1.6;
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
st.markdown(custom_css, unsafe_allow_html=True)

# Logo
st.markdown(f'<img src="{logo_url}" class="logo" alt="ARX Logo">', unsafe_allow_html=True)

# Title and subtitle
st.markdown('<div class="title">Welcome to the Vocational Assessment Portal</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Streamlined solutions for generating assessment-related reports</div>', unsafe_allow_html=True)

# Card container
st.markdown("""
<div class="card-container">
    <div class="card">
        <div class="card-title">Pass/Fail Reports</div>
        <div class="card-description">
            Generate detailed reports showing pass/fail statistics for theory exams, categorized by curriculum and date.
        </div>
    </div>
</div>
        """, unsafe_allow_html=True)
# Footer
st.markdown('<div class="footer">© 2024 Vocational Assessment Portal. All rights reserved.</div>', unsafe_allow_html=True)
