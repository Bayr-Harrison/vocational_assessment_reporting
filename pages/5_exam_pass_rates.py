import streamlit as st
import pg8000
import os
import pandas as pd
import matplotlib.pyplot as plt

# Set page configuration
st.set_page_config(
    page_title="Exam Pass Rate Analysis",
    page_icon="📘",
    layout="wide"
)

# CSS styling
page_style = """
    <style>
    .stApp {
        background-color: #e0e0e0;
    }
    .title {
        color: #2b2b2b;
        font-size: 42px;
        font-weight: bold;
        text-align: center;
        font-family: 'Arial', sans-serif;
    }
    .subtitle {
        color: #595959;
        font-size: 24px;
        text-align: center;
        font-family: 'Arial', sans-serif';
        margin-bottom: 40px;
    }
    </style>
"""
st.markdown(page_style, unsafe_allow_html=True)

# Title and subtitle
st.markdown('<p class="title">Exam Pass Rate Analysis</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Visualize Pass Rates for Different Exams</p>', unsafe_allow_html=True)

# Authentication
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    password = st.text_input("Enter Password", type="password")
    if password:
        if password == os.environ["APP_PASSWORD5"]:
            st.session_state["authenticated"] = True
            st.success("Authenticated successfully!")
        else:
            st.error("Incorrect password. Please try again.")

if st.session_state["authenticated"]:
    st.write("Select a date range and an exam qualification to analyze pass rates.")

    # Date inputs
    start_date = st.date_input("Start Date")
    end_date = st.date_input("End Date")

    # Qualification selection
    exam_qualification = st.selectbox(
        "Select Exam Qualification",
        [
            "GACA ASSOCIATE DIPLOMA", "GACA DIPLOMA", "EASA ASSOCIATE DIPLOMA",
            "EASA DIPLOMA B1", "EASA DIPLOMA B2", "UAS ASSOCIATE DIPLOMA",
            "UAS DIPLOMA SHARED", "UAS DIPLOMA MECHANICAL", 
            "UAS DIPLOMA COMMUNICATIONS", "UAS DIPLOMA AVIONICS"
        ]
    )

    # Connect to Supabase database
    def connect_to_supabase():
        return pg8000.connect(
            database=os.environ["SUPABASE_DB_NAME"],
            user=os.environ["SUPABASE_USER"],
            password=os.environ["SUPABASE_PASSWORD"],
            host=os.environ["SUPABASE_HOST"],
            port=os.environ["SUPABASE_PORT"]
        )

    # Query the database
    def query_database(start_date, end_date, exam_qualification):
        db_query = f"""
        SELECT 
            exam_results.exam AS Exam,
            exam_list.qualification AS Qualification, 
            ROUND(1.0 * SUM(CASE WHEN exam_results.result = 'PASS' THEN 1 ELSE 0 END) / COUNT(*), 2) AS PassRate,
            SUM(CASE WHEN exam_results.result = 'PASS' THEN 1 ELSE 0 END) AS Pass,
            SUM(CASE WHEN exam_results.result = 'FAIL' THEN 1 ELSE 0 END) AS Fail,
            COUNT(*) AS Total
        FROM 
            exam_results
        INNER JOIN
            calendar ON exam_results.date = calendar.date
        INNER JOIN
            exam_list ON exam_results.exam = exam_list.exam 
        WHERE 
            exam_results.attempt_index = 1
            AND exam_results.date >= '{start_date}'
            AND exam_results.date <= '{end_date}'
            AND exam_list.qualification = '{exam_qualification}'
        GROUP BY 
            exam_results.exam, 
            exam_list.qualification
        ORDER BY 
            PassRate DESC;
        """
        try:
            connection = connect_to_supabase()
            cursor = connection.cursor()
            cursor.execute(db_query)
            result = cursor.fetchall()
            cursor.close()
            connection.close()
            return result
        except Exception as e:
            st.error(f"Error querying database: {e}")
            return []

    # Button to query and display results
    if st.button("Analyze Pass Rates"):
        if start_date and end_date and exam_qualification:
            st.write("Querying database...")
            data = query_database(start_date, end_date, exam_qualification)
            if data:
                # Convert query result to DataFrame
                df = pd.DataFrame(data, columns=["Exam", "Qualification", "PassRate", "# Pass", "# Fail", "Total"])

                # Update PassRate to percentage format
                df["PassRate"] = (df["PassRate"] * 100).round(0).astype(int).astype(str) + '%'

                # Display DataFrame
                st.write("Query Results:")
                st.dataframe(df)

                # Map qualification to bar color
                if "EASA" in exam_qualification:
                    bar_color = "#E2A583"  # Orange
                elif "GACA" in exam_qualification:
                    bar_color = "#89CFDC"  # Blue
                elif "UAS" in exam_qualification:
                    bar_color = "#9FDEA7"  # Green

                # Plot bar graph
                st.write("Pass Rates by Exam:")
                fig, ax = plt.subplots(figsize=(10, 6))
                df["NumericPassRate"] = df["PassRate"].str.rstrip('%').astype(float)  # For plotting
                bars = ax.bar(df["Exam"], df["NumericPassRate"], color=bar_color)

                # Add percent labels above bars
                for bar in bars:
                    height = bar.get_height()
                    ax.text(
                        bar.get_x() + bar.get_width() / 2, 
                        height, 
                        f"{int(height)}%", 
                        ha="center", 
                        va="bottom", 
                        fontsize=8
                    )

                # Customize the graph
                ax.set_title(f"1st Attempt Exam Pass Rates: {exam_qualification}", fontsize=16)
                ax.set_xlabel("Exam", fontsize=12)
                ax.set_ylabel("Pass Rate (%)", fontsize=12)
                ax.set_xticks(range(len(df["Exam"])))
                ax.set_xticklabels(df["Exam"], rotation=45, ha="right")
                ax.set_ylim(0, 100)  # Always start at 0 and end at 100%
                st.pyplot(fig)
            else:
                st.warning("No data found for the selected criteria.")
        else:
            st.error("Please select all required inputs.")
