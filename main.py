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
    .stApp {
        background-color: #e0e0e0; /* Light grey background */
    }
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
        font-family: 'Arial', sans-serif';
        margin-bottom: 40px;
    }
    .description {
        color: #404040; /* Darker grey */
        font-size: 18px;
        text-align: center;
        font-family: 'Arial', sans-serif';
        line-height: 1.6;
        margin: 0 10%;
    }
    </style>
"""
st.markdown(page_style, unsafe_allow_html=True)

# Title and subtitle
st.markdown('<p class="title">Welcome to the Vocational Assessment Portal</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Your one-stop solution for exam reporting and coversheet generation</p>', unsafe_allow_html=True)

# Explanation of reporting options
st.markdown("""
<p class="description">
This portal provides tools to generate and access various assessment reports, including:
</p>
<ul class="description">
    <li>Pass/Fail Reports: Generate comprehensive reports showing pass and fail statistics for theory exams.</li>
    <li>Query Exam Results: View detailed exam results, including scores and attendance.</li>
    <li>Individualized Coversheets: Generate personalized coversheets summarizing student performance.</li>
</ul>
<p class="description">
Use the tabs on the left to select a reporting option and begin.
</p>
""", unsafe_allow_html=True)
