import streamlit as st
import pandas as pd
import requests
import os

BASE_API_URL = os.environ.get(
    "ST_BASE_API_URL"

)

API_STUDENTS = f'{BASE_API_URL}/api/students'
API_REPORT = f"{BASE_API_URL}/api/run-report"

st.set_page_config(page_title= "Managing student", layout="wide")
st.title("Student Data Management")

c1, c2 = st.columns([1,1])
with c1:
    load_btn = st.button("Load Students", use_container_width= True)

with c2:
    report_btn = st.button("Generate CSV Report", use_container_width=True)

st.write("---")

if load_btn:
    try:
        with st.spinner("Loading student from database..."):
            res = requests.get(API_STUDENTS)
            res.raise_for_status()
            data = res.json()
        
        df = pd.DataFrame(data)
        st.session_state["df"] = df

        st.success(f"Loaded {len(df)} students.")

    except Exception as e:
        st.error(f"Error loading students: {e}")

    
if "df" in st.session_state:
    df = st.session_state["df"]

    st.subheader("Filters & Search")

    col_search, col_major, col_gender = st.columns([2,1,1])

    with col_search: 
        search_query = st.text_input("Search (name, ID, major):")

    with col_gender:
        gender_filter = st.selectbox(
            "Major:",
            ["All"] + sorted(df["major"].dropna().unique().tolist())
        )
    
    with col_major:
        major_filter = st.selectbox(
            "Major:",
            ["All"] + sorted(df["Major"].dropa().unique().tolist())
        )
    
    # Apply search
    filtered = df.copy()

    if search_query:
        s = search_query.lower()
        filtered = filtered[
            filtered.apply(
                lambda x:
                    s in str(x["student_id"]).lower()
                    or s in str(x["full_name"]).lower()
                    or s in str(x["major"]).lower(),
                axis=1
            )
        ]

    # Apply major filter
    if major_filter != "All":
        filtered = filtered[filtered["major"] == major_filter]

    # Apply gender filter
    if gender_filter != "All":
        filtered = filtered[filtered["gender"] == gender_filter]

    st.info(f"Showing {len(filtered)} students after filtering.")

    # ------------------------------------------------------
    # Outlier & BMI coloring
    # ------------------------------------------------------
    st.subheader("Student Table")

    def highlight_outliers(row):
        if any(
            row.get(col, False)
            for col in row.index
            if "outlier" in col.lower()
        ):
            return ["background-color: #ffe6e6"] * len(row)
        return [""] * len(row)

    def bmi_style(val):
        if pd.isna(val): return ""
        if val < 18.5: return "background-color:#e0f3ff"
        if val < 25: return "background-color:#e6ffed"
        if val < 30: return "background-color:#fff9db"
        return "background-color:#ffe6e6"

    styled = filtered.style.apply(highlight_outliers, axis=1)

    if "bmi" in filtered.columns:
        styled = styled.applymap(bmi_style, subset=["bmi"])

    st.dataframe(
        styled,
        height=500,
        use_container_width=True
    )

# ------------------------------------------------------------------------------
# Run Report
# ------------------------------------------------------------------------------
if report_btn:
    try:
        with st.spinner("Running full analytics and generating CSV..."):
            res = requests.post(API_REPORT)
            msg = res.json()

        st.success(msg.get("message", "Report generated!"))

    except Exception as e:
        st.error(f"Error generating report: {e}")