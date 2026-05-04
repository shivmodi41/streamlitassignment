import streamlit as st
import pandas as pd
import numpy as np
import datetime

# ==========================================
# Task 1: The Setup & Header
# ==========================================
st.title("🌍 Travel & Investment Planner")
st.write("Welcome to the **Travel and Investment Portal**. Use this *interactive dashboard* to forecast your budget and plan your next big venture.")

# Display a success message that appears when the app starts
st.success("Welcome to the portal! Setup your parameters below to get started.")

# ==========================================
# Task 2: The Sidebar & Input Controls
# ==========================================
st.sidebar.header("User Preferences")

# Radio button for user level
user_level = st.sidebar.radio("User Level", ["Beginner", "Intermediate", "Advanced"])

# Selectbox for Target Continent
continents = ["Africa", "Asia", "Europe", "North America", "South America", "Australia", "Antarctica"]
continent = st.sidebar.selectbox("Target Continent", continents)

# Multiselect for Interests
interests = st.sidebar.multiselect("Interests", ["Tech", "Finance", "Travel", "Food"], default=["Tech"])

# Handling the case where no interest is selected
if not interests:
    st.sidebar.info("💡 Tip: Select at least one interest to better personalize your plan.")

# ==========================================
# Task 5: Refinement & Layout (Columns)
# Task 3: Temporal input
# ==========================================
# Using columns to place Date Input and Slider side-by-side
col1, col2 = st.columns(2)

with col1:
    start_date = st.date_input("Project Start Date", datetime.date.today())
    
with col2:
    # Slider for Investment Budget
    budget = st.slider("Investment Budget", min_value=0, max_value=10000, value=5000, step=100)
    
    # Error Handling for 0 budget
    if budget == 0:
        st.warning("⚠️ Your investment budget is set to 0. Please increase it to generate a valid daily budget.")

# Add a text input to capture the user's name for the final report
user_name = st.text_input("Enter your Name:", value="Shiv")

# ==========================================
# Task 3: Data Handling & Interactive DataFrame
# ==========================================
st.write("### 📊 Mock Financial Data")

# Mock Data Generation
# We include a 'Continent' column to allow for the filtering challenge, 
# but we will only display the 5 requested columns.
np.random.seed(42) # For reproducible mock data
mock_data = {
    "Date": pd.date_range(start=datetime.date.today(), periods=14),
    "Category": np.random.choice(["Tech", "Finance", "Travel", "Food"], 14),
    "Amount": np.random.randint(100, 2000, size=14),
    "Status": np.random.choice(["Pending", "Approved", "Completed"], 14),
    "Growth": [f"+{x}%" for x in np.random.randint(1, 20, size=14)],
    "Continent": np.random.choice(continents, 14)
}

df = pd.DataFrame(mock_data)

# Challenge: Filter the data based on the continent selected in the sidebar
filtered_df = df[df["Continent"] == continent]

# Displaying only the 5 specific columns requested
display_columns = ["Date", "Category", "Amount", "Status", "Growth"]

if filtered_df.empty:
    st.write(f"No mock data generated for {continent} in this random batch. Try selecting another continent!")
else:
    # Make the dataframe interactive
    st.dataframe(filtered_df[display_columns], use_container_width=True)

# ==========================================
# Task 4: Logic & Feedback
# ==========================================
st.write("---")
# Button to process the report
if st.button("Process Report"):
    if budget > 0:
        # Calculate daily budget
        daily_budget = budget / 30
        
        # Display the summary sentence
        st.write(f"### 📋 Report Summary")
        st.write(f"User **{user_name}** wants to travel to **{continent}** starting **{start_date.strftime('%B %d, %Y')}**.")
        st.write(f"With an overall budget of **${budget}**, your estimated daily budget is **${daily_budget:.2f}** for a 30-day period.")
        
        # Trigger balloon animation
        st.balloons()
    else:
        st.error("Cannot process the report with a budget of 0. Please adjust your budget.")