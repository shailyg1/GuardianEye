import streamlit as st
from modules import email_scanner
from modules import url_analyzer, media_leak_checker
import json
import os

st.set_page_config(page_title="GuardianEye", page_icon="🛡️", layout="wide")

st.sidebar.title("GuardianEye 🛡️")
module = st.sidebar.radio("Select Module", ["Email Scanner", "URL Analyzer", "Media Leak Checker"])
st.title("GuardianEye: Cybersecurity Detection")

if module == "Email Scanner":
    st.header("Email Phishing Scanner")
    email_data = st.text_area("Paste email headers/text here:")
    if st.button("Scan Email"):
        result = email_scanner.scan_email(email_data)
        st.write(result)

elif module == "URL Analyzer":
    st.header("Suspicious URL Analyzer")
    url = st.text_input("Enter URL to check:")
    if st.button("Analyze URL"):
        result = url_analyzer.analyze_url(url)
        st.write(result)

elif module == "Media Leak Checker":
    st.header("Image Leak/Duplicate Detector")
    uploaded_image = st.file_uploader("Upload image file", type=["jpg", "png", "jpeg"])
    if uploaded_image:
        result = media_leak_checker.scan_image(uploaded_image)
        st.write(result)

# Simple Logging
def log_event(event_type, input_data):
    log_entry = {"event": event_type, "input": input_data}
    logs_dir = "logs"
    os.makedirs(logs_dir, exist_ok=True)
    log_path = os.path.join(logs_dir, "app_logs.json")
    with open(log_path, "a") as f:
        f.write(json.dumps(log_entry) + "\n")

# Example usage: log_event(module, str(input_data))

st.markdown("""
<style>
    .reportview-container {
        background: #232526;
        color: #f9fafb;
    }
    .sidebar .sidebar-content {
        background: #373737;
        color: #fff;
    }
    .stButton>button {
        color: #fff;
        background-color: #238636;
        margin-bottom: 1em;
    }
</style>
""", unsafe_allow_html=True)
