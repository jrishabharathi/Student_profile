import streamlit as st
from groq import Groq
st.set_page_config(page_title="STUDENT PROFILE", layout="centered")
st.title("student information")
st.caption("J RISHAB BHARATHI 5TH SEM A SEC")
try:
  client=Groq(api_key=st.secrets["GROQ_API_KEY"])
except (keyError, FileNotFoundError):
  st.error("API key is missing. addit in advanced settings")
  st.stop()
name=st.text_area("Student_Name","Enter Your Name")
usn=st.text_area("USN.","Enter your USN")
dept=st.text_area("Department","Enter Your Department")
year=st.radio("Year",["1st year","2nd Year","3rd Year","4th Year"])
sem=st.radio("Sem",["1st sem","2nd sem","3rd sem","4th sem","5th sem","6th sem","7th sem","8th sem"])
btn=st.button(" Profile_Detail")
if btn:
    st.success("Profile Submitted Successfully!")

    st.subheader("Student Details")

    st.write("**Student_Name:**", name)
    st.write("**USN:**", usn)
    st.write("**Year:**", year)
    st.write("**sem:**", sem)
    st.write("**Department:**", dept)
    
