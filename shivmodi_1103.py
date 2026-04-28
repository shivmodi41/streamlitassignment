import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

st.title(":rainbow[File management]")
st.sidebar.title("Settings")
st.toast("This is file management website")
# Step 1: Upload File
st.header("1. Upload Data")
uploaded_file = st.file_uploader("Upload your CSV file here", type=['csv'])

if uploaded_file is not None:
    # Read the file
    df = pd.read_csv(uploaded_file)
    
    st.success("File uploaded successfully!")
    
    st.write("Data Preview:")
    st.dataframe(df.head(10)) # Just showing 10 rows to keep it simple

    # Step 2: Column Mapping
    st.header("2. Map Your Columns")
    st.write("Select which columns from your file match the required fields.")
    
    # Get a list of columns to put in the dropdowns
    file_columns = ["--Select--"] + df.columns.tolist()
    
    col_user = st.selectbox("Which column is the User ID?", file_columns)
    col_date = st.selectbox("Which column is the Transaction Date?", file_columns)
    col_amount = st.selectbox("Which column is the Amount?", file_columns)

    # Only show the next steps if all dropdowns are filled
    if col_user != "--Select--" and col_date != "--Select--" and col_amount != "--Select--":
        
        # Step 3: Transformation
        st.header("3. Transform Data")
        
        # Create a new blank dataframe for the final data
        final_df = pd.DataFrame()
        
        # Bring over the mapped columns and rename them
        final_df["User_ID"] = df[col_user]
        final_df["Transaction_Date"] = df[col_date]
        
        # Validation: Make sure amount is a number. If it has text, turn it to NaN (null)
        final_df["Amount"] = pd.to_numeric(df[col_amount], errors='coerce')
        
        # Show a warning if any amounts were turned into nulls (meaning they were text)
        if final_df["Amount"].isnull().sum() > 0:
            st.warning("Some amounts were not numbers and were converted to missing values (NaN).")

        # Transformation Options
        remove_dups = st.checkbox("Remove Duplicate Rows")
        if remove_dups:
            final_df = final_df.drop_duplicates()
            
        fill_nulls = st.checkbox("Fill missing amounts with 0")
        if fill_nulls:
            final_df["Amount"] = final_df["Amount"].fillna(0)
            
        # Scaling calculation
        st.write("Add Tax Multiplier")
        tax_multiplier = st.number_input("Enter multiplier (e.g., 1.05 for 5% tax)", value=1.0)
        final_df["Adjusted_Amount"] = final_df["Amount"] * tax_multiplier

        st.write("Final Processed Data:")
        st.dataframe(final_df.head(100))

        # Step 4: Export
        st.header("4. Download Result")
        
        # Convert the dataframe back to a CSV format
        csv_data = final_df.to_csv(index=False).encode('utf-8')
        
        st.download_button(
            label="Download Final CSV",
            data=csv_data,
            file_name="cleaned_vendor_data.csv",
            mime="text/csv"
        )
        