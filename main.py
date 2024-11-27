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
    /* General page styling */
    .stApp {
        background-color: #f4f4f4; /* Light grey background */
        font-family: 'Arial', sans-serif;
    }

    /* Title styling */
    .title {
        color: #333333; /* Dark grey */
        font-size: 48px;
        font-weight: bold;
        text-align: center;
        margin-top: 30px;
    }

    /* Subtitle styling */
    .subtitle {
        color: #555555; /* Medium grey */
        font-size: 24px;
        text-align: center;
        margin-bottom: 40px;
    }

    /* Description styling */
    .description {
        color: #666666; /* Slightly lighter grey */
        font-size: 18px;
        text-align: center;
        line-height: 1.8;
        margin: 0 15%;
    }

    /* Reporting options styling */
    .reporting-options {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        margin-top: 50px;
        gap: 20px;
    }

    /* Reporting option card */
    .option-card {
        background: #ffffff;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        border-radius: 12px;
        padding: 20px 30px;
        width: 80%;
        max-width: 600px;
        text-align: left;
    }

    .option-title {
        color: #333333;
        font-size: 20px;
        font-weight: bold;
        margin-bottom: 10px;
    }

    .option-description {
        color: #666666;
        font-size: 16px;
        line-height: 1.6;
    }

    /* Footer styling */
    .footer {
        color: #888888;
        font-size: 14px;
        text-align: center;
        margin-top: 60px;
    }
    </style>
"""
st.markdown(page_style, unsafe_allow_html=True)

# Title and subtitle
st.markdown('<div class="title">Welcome to the Vocational Assessment Portal</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Your one-stop solution for exam reporting and coversheet generation</div>', unsafe_allow_html=True)

# Explanation of reporting options
st.markdown('<div class="description">This portal provides tools to generate and access various assessment reports. Explore the options below to get started.</div>', unsafe_allow_html=True)

# Reporting options section
st.markdown('<div class="reporting-options">', unsafe_allow_html=True)

# Pass/Fail Reports
st.markdown("""
<div class="option-card">
    <div class="option-title">Pass/Fail Reports</div>
    <div class="option-description">
        Generate comprehensive reports showing pass and fail statistics for theory exams, categorized by date, curriculum, and more.
    </div>
</div>
""", unsafe_allow_html=True)

# Query Exam Results
st.markdown("""
<div class="option-card">
    <div class="option-title">Query Exam Results</div>
    <div class="option-description">
        View detailed exam results, including scores, attendance records, and session details, for selected time periods.
    </div>
</div>
""", unsafe_allow_html=True)

# Individualized Coversheets
st.markdown("""
<div class="option-card">
    <div class="option-title">Individualized Coversheets</div>
    <div class="option-description">
        Generate personalized coversheets summarizing each student's exam performance with detailed subject-wise results.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">© 2024 Vocational Assessment Portal. All rights reserved.</div>', unsafe_allow_html=True)
