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
btn=st.button(" Profile_Detail")
if btn:
    st.success("Profile Submitted Successfully!")

    st.subheader("Student Details")

    st.write("**Student_Name:**", name)
    st.write("**USN:**", usn)
    st.write("**Department:**", dept)
    st.write("**Current_Year:**", year)
