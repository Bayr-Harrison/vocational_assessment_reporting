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
    .centered-buttons .stButton>button {
        background-color: #527ba1;
        color: white;
        border: none;
        font-size: 16px;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
    }

    .centered-buttons .stButton>button:hover {
        background-color: #3b6a9e;
        color: white;
    }

    /* Center the buttons container */
    .centered-buttons {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-top: 40px;
    }

    /* Logo placement */
    .logo {
        position: absolute;
        top: 20px;
        left: 20px;
        width: 150px;
    }
    </style>
"""
st.markdown(page_bg_color, unsafe_allow_html=True)

# Logo image from GitHub repository
logo_url = "https://raw.githubusercontent.com/Bayr-Harrison/vocational_assessment_reporting/main/arx_logo.png"
st.markdown(f'<img class="logo" src="{logo_url}" alt="ARX Logo">', unsafe_allow_html=True)

# Title and subtitle
st.markdown('<p class="title">Welcome to the Vocational Assessment Portal</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Your one-stop solution for exam reporting and coversheet generation</p>', unsafe_allow_html=True)

# Centered navigation buttons
st.markdown('<div class="centered-buttons">', unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 1, 1])  # Adjusted for centering
with col1:
    if st.button("Generate Pass/Fail Reports"):
        st.experimental_set_query_params(page="pass_fail")
with col2:
    if st.button("Query Exam Results"):
        st.experimental_set_query_params(page="query_results")
with col3:
    if st.button("Generate Coversheets"):
        st.experimental_set_query_params(page="coversheets")
st.markdown('</div>', unsafe_allow_html=True)
