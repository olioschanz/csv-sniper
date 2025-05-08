import streamlit as st
import pandas as pd
import difflib

st.title("CSV Sniper")
st.caption("🎯 Locked on target: Scanning for perfect email hits...")

def find_email_column(columns):
    """Find the column name that most closely matches 'email'."""
    columns_lower = [col.lower() for col in columns]
    match = difflib.get_close_matches('email', columns_lower, n=1, cutoff=0.6)
    if match:
        # Return the original column name (case preserved)
        for col in columns:
            if col.lower() == match[0]:
                return col
    return None

file1 = st.file_uploader("Upload First CSV (this is the primary list)", type="csv")
file2 = st.file_uploader("Upload Second CSV (reference list to match against)", type="csv")

if file1 and file2:
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    col1 = find_email_column(df1.columns)
    col2 = find_email_column(df2.columns)

    if not col1 or not col2:
        st.error("Could not find a column similar to 'email' in both files.")
    else:
        df1['email_normalized'] = df1[col1].astype(str).str.strip().str.lower()
        df2['email_normalized'] = df2[col2].astype(str).str.strip().str.lower()

        common_emails = set(df1['email_normalized']).intersection(df2['email_normalized'])
        matched_rows = df1[df1['email_normalized'].isin(common_emails)].drop(columns='email_normalized')

        st.success(f"Found {len(matched_rows)} matching email(s).")
        st.dataframe(matched_rows)

        csv = matched_rows.to_csv(index=False).encode('utf-8')
        st.download_button("Download Matched Rows", csv, "matched_rows.csv", "text/csv")