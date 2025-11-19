import streamlit as st
import pandas as pd

st.title("📊 Business Data Automation Tool (Pro)")
st.write("Upload your CSV or Excel file to clean, filter, summarize and download results.")

uploaded = st.file_uploader("Upload your file", type=["csv", "xlsx"])

if uploaded:
    # Read file
    if uploaded.name.endswith(".csv"):
        df = pd.read_csv(uploaded)
    else:
        df = pd.read_excel(uploaded)

    st.subheader("🔍 Raw Data Preview")
    st.dataframe(df)

    # Cleaning Options
    st.subheader("🧹 Data Cleaning Options")
    remove_duplicates = st.checkbox("Remove Duplicate Rows")
    drop_na = st.checkbox("Remove Empty Rows")
    lower_columns = st.checkbox("Make All Column Names Lowercase")

    cleaned_df = df.copy()

    if remove_duplicates:
        cleaned_df = cleaned_df.drop_duplicates()

    if drop_na:
        cleaned_df = cleaned_df.dropna()

    if lower_columns:
        cleaned_df.columns = cleaned_df.columns.str.lower()

    st.subheader("✨ Cleaned Data Preview")
    st.dataframe(cleaned_df)

    # Summary Statistics
    st.subheader("📈 Summary Report")
    st.write(cleaned_df.describe())

    # Download button
    st.subheader("⬇ Download Cleaned File")
    st.download_button(
        label="Download Excel",
        data=cleaned_df.to_excel(index=False, engine='openpyxl'),
        file_name="cleaned_output.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
