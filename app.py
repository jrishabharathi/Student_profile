import streamlit as st
from groq import Groq
st.set_page_config(page_title="Gnanesh N", layout="centered")
st.title("🎓 Student Profile Application")
st.caption("Developed by: Gnanesh N")
try:
  client=Groq(api_key=st.secrets["GROQ_API_KEY"])
except (keyError, FileNotFoundError):
  st.error("API key is missing. addit in advanced settings")
  st.stop()
name=st.text_area("Student Name","Enter Your Name")
usn=st.text_area("USN / Roll no.","Enter your USN")
dept=st.text_area("Department","Enter Your Department")
year=st.radio("Current Year",["1st year","2nd Year","3rd Year","4th Year"])
btn=st.button("View My Profile")
if btn:
    st.success("Profile Created Successfully!")

    st.subheader("🎓 Student Profile Details")

    st.write("**Student Name:**", name)
    st.write("**USN / Roll No.:**", usn)
    st.write("**Department:**", dept)
    st.write("**Current Year:**", year)
