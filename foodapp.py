#designing form of food app 
import streamlit as st
import pandas as pd
import datetime

# st.set_page_config(page_title="Food App", page_icon=":pizza:", layout="wide")
with st.form("my_form"):
    st.set_page_config(page_title="Food App", page_icon=":pizza:", layout="wide")
    st.title("Food App")
    c1,c2=st.columns(2)
    with c1:
        fname = st.text_input("Enter your First name")
    with c2:
        lname = st.text_input("Enter your Last name")
    # c1, c2 = st.columns(2)
    # c1.write(f"First name is: {fname}")
    # c2.write(f"Last name is: {lname}")
    city=st.selectbox("Select your city",["bharuch","surat","vadodara"])
    food_preferance=st.multiselect("Select your food preference",["veg","non-veg","vegan"])
    slider=st.slider("how many time you order",0,100)
    gender=st.radio("select your gender",["male","female","other"])
    dob=st.date_input("select your date of birth")
    audio=st.audio_input("record your voice to give order")
    if audio:
            st.write("audio recorded successfully")
            st.audio(audio)
    comment=st.text_input("write your comment")
    agree=st.checkbox("I agree to the terms and conditions")
    submit=st.form_submit_button("Submit",use_container_width=True)
    if submit:
        if fname == '':
            st.error('Please enter your first name.')
        elif lname == '':
            st.error('Please enter your last name.')
        elif agree == False:
            st.error('Please agree to Our Terms and Conditions.')
        else:
            st.success('Your order is placed successfully!')
            st.balloons()
            st.write('FIRST Name : ', fname)
            st.write('LAST Name : ', lname)
            st.write('City :', city)
            st.write('Food Preference :',', '.join(food_preferance))
            st.write('Order Frequency :', slider)
            st.write('Gender :', gender)
            st.write('Date of Birth :', dob)
            st.write('Comment :', comment)
            st.write("Form submitted successfully!")
          
