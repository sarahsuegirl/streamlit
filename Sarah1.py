import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
#start streamlit instructions
#Title
st.title("Registertion Form")

#Input FirstName and LastName
st.text_input("First Name")
st.text_input("Last Name")

#drop down for Mr,Mrs,Ms
st.selectbox("select",["Mr.","Mrs.","Ms."])


#Designation(drop down)
st.selectbox("select",["Software","Hardware","Others"])

#Date_of_birth
st.date_input("Please enter your date of birth")

#Select Gender
rb=st.radio("Select Gender",["Male","Female","Prefer not to say"])
if rb=="Male":
    st.info("Male")
elif rb=="Female":
    st.info("Female")
elif rb=="Prefer not to say":
    st.info("N/A")

#slider(Age)1-100
st.slider("pick a range for age",0,100)

#submit button
st.button("Submit")


