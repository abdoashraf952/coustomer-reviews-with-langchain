import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

# =========================
# Google Sheet Connection
# =========================

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_file(
    "credentials.json",
    scopes=SCOPES
)

client = gspread.authorize(creds)

SHEET_URL = "https://docs.google.com/spreadsheets/d/19_axzwI81tKb3vZazRHy8KQnTAZeQajal6MKhOl6zr4/edit?gid=0#gid=0"
sheet = client.open_by_url(SHEET_URL).sheet1

# =========================
# Streamlit UI
# =========================

st.set_page_config(page_title="Customer Feedback", page_icon="📝", layout="centered")

st.title("📝 Customer Feedback Form")
st.write("Please share your feedback with us.")

with st.form("feedback_form"):
    name = st.text_input("Your name (optional)")
    email = st.text_input("Your email (optional)")
    feedback = st.text_area("Your feedback", height=150)

    submitted = st.form_submit_button("Submit Feedback")

    if submitted:
        if feedback.strip() == "":
            st.warning("⚠️ Please write your feedback before submitting.")
        else:
            row = [
                feedback,
                name,
                email
            ]

            sheet.append_row(row, value_input_option="USER_ENTERED")

            st.success("✅ Thank you! Your feedback has been submitted.")
            st.balloons()
