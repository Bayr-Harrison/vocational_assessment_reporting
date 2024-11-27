import streamlit as st

# Customizing the page
st.set_page_config(
    page_title="Vocational Assessment Portal",
    page_icon="📘",
    layout="wide"
)

# Logo URL from GitHub
logo_url = "https://raw.githubusercontent.com/Bayr-Harrison/vocational_assessment_reporting/main/arx_logo.png"

# Inline CSS for neumorphic styling
page_style = f"""
    <style>
    /* General page styling */
    .stApp {{
        background-color: #e0e0e0; /* Light grey background */
        font-family: 'Arial', sans-serif;
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
        color: #2b2b2b; /* Dark grey */
        font-size: 48px;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
    }}

    /* Subtitle styling */
    .subtitle {{
        color: #595959; /* Medium grey */
        font-size: 24px;
        text-align: center;
        margin-bottom: 40px;
    }}

    /* Neumorphic container styling */
    .container {{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        margin-top: 50px;
        gap: 30px;
    }}

    /* Neumorphic card styling */
    .card {{
        background: #e0e0e0;
        box-shadow: 10px 10px 20px #bebebe, -10px -10px 20px #ffffff;
        border-radius: 15px;
        padding: 20px 30px;
        width: 80%;
        max-width: 600px;
        text-align: center;
        transition: transform 0.2s ease;
    }}

    .card:hover {{
        transform: scale(1.02);
        box-shadow: inset 5px 5px 10px #bebebe, inset -5px -5px 10px #ffffff;
    }}

    .card-title {{
        color: #2b2b2b;
        font-size: 22px;
        font-weight: bold;
        margin-bottom: 10px;
    }}

    .card-description {{
        color: #404040;
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
st.markdown(page_style, unsafe_allow_html=True)

# Logo
st.markdown(f'<img src="{logo_url}" class="logo" alt="ARX Logo">', unsafe_allow_html=True)

# Title and subtitle
st.markdown('<div class="title">Welcome to the Vocational Assessment Portal</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Your one-stop solution for exam reporting and coversheet generation</div>', unsafe_allow_html=True)

# Reporting options section
st.markdown('<div class="container">', unsafe_allow_html=True)

# Pass/Fail Reports card
st.markdown("""
<div class="card">
    <div class="card-title">Pass/Fail Reports</div>
    <div class="card-description">
        Generate comprehensive reports showing pass and fail statistics for theory exams, categorized by date, curriculum, and more.
    </div>
</div>
""", unsafe_allow_html=True)

# Query Exam Results card
st.markdown("""
<div class="card">
    <div class="card-title">Query Exam Results</div>
    <div class="card-description">
        View detailed exam results, including scores, attendance records, and session details, for selected time periods.
    </div>
</div>
""", unsafe_allow_html=True)

# Individualized Coversheets card
st.markdown("""
<div class="card">
    <div class="card-title">Individualized Coversheets</div>
    <div class="card-description">
        Generate personalized coversheets summarizing each student's exam performance with detailed subject-wise results.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">© 2024 Vocational Assessment Portal. All rights reserved.</div>', unsafe_allow_html=True)
