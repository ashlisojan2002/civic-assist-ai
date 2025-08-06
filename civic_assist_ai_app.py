import streamlit as st
import google.generativeai as genai

# Configure Gemini API Key
genai.configure(api_key="AIzaSyDmcFeRic6aFn1CXY3q_iADZFeGQhO6rq8")  # Replace with your key

model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

indian_states = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka",
    "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram",
    "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana",
    "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"
]

# Custom CSS for styling
st.markdown("""
    <style>
        .title {
            color: rgb(8, 115, 102);
            text-align: center;
            font-size: 38px;
            font-weight: bold;
        }
        .stButton button {
            background-color: rgb(8, 115, 102);
            color: white;
            border-radius: 8px;
            padding: 0.6em 1.2em;
            font-size: 16px;
        }
        .stButton button:hover {
            background-color: rgb(6, 90, 80);
        }
        .response-box {
            background-color: #e6f4f2;
            padding: 15px;
            border-radius: 10px;
            border: 1px solid rgb(8, 115, 102);
        }
    </style>
""", unsafe_allow_html=True)

# App Title
st.markdown('<div class="title">Civic Assist AI Agent</div>', unsafe_allow_html=True)
st.write("### Your smart assistant for resolving civic issues in India.")

# Inputs
state = st.selectbox("📍 Select Your State", indian_states)
complaint = st.text_area("🗣️ Describe your civic issue in detail:")

# Submit button
if st.button("Submit Complaint"):
    if complaint.strip():
        st.write("🤖 **Processing your complaint...**")
        prompt = f"""
You are a civic assistant AI for India. The user is from {state}.
Understand their civic complaint and respond in this format:

Issue Type:
Responsible Department:
Suggestion:

Complaint: {complaint}
"""
        response = model.generate_content(prompt)
        st.markdown('<div class="response-box">✅ **AI Response:**<br>' + response.text + '</div>', unsafe_allow_html=True)
    else:
        st.error("❗ Please enter a civic issue.")
