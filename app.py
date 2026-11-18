import streamlit as st
from groq import Groq
st.set_page_config(page_title="STUDENT PROFILE", layout="centered")
st.title("Student_Information")
st.caption("HANAMANTRAYA D G")
try:
  client=Groq(api_key=st.secrets["GROQ_API_KEY"])
except (keyError, FileNotFoundError):
  st.error("API key is missing. addit in advanced settings")
  st.stop()
name=st.text_area("Student Name","Enter Your Name")
usn=st.text_area("Student_USN.","Enter your USN")
dept=st.text_area("Department","Enter Your Department")
year=st.radio("Year",["1st year","2nd Year","3rd Year","4th Year"])
btn=st.button(" Profile Detail")
if btn:
    st.success("Profile Submitted Successfully!")

    st.subheader("Student Details")

    st.write("**Student_Name:**", name)
    st.write("**USN:**", usn)
    st.write("**Year:**", year)
    st.write("**Department:**", dept)
    
