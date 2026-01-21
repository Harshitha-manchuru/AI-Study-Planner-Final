import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import json
import urllib.parse
from PyPDF2 import PdfReader
from agent.mock_agent import generate_study_plan

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="AI Study Planner",
    page_icon="📚",
    layout="centered"
)

st.title("📚 AI Study Planner Agent")
st.subheader("Smart daily planning for exam success")
st.markdown("---")

# -------------------------------
# Load data files
# -------------------------------
with open("data/presets.json", "r") as f:
    presets = json.load(f)

with open("data/subjects_map.json", "r") as f:
    subject_map = json.load(f)

# Reliable W3Schools subject-level links
w3_links = {
    "python": "https://www.w3schools.com/python/",
    "java": "https://www.w3schools.com/java/",
    "dbms": "https://www.w3schools.com/sql/",
    "aptitude": "https://www.w3schools.com/"
}

# -------------------------------
# Helper: Extract text from PDF
# -------------------------------
def extract_text_from_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + " "
    return text.lower()

# -------------------------------
# Helper: Infer topics from text
# -------------------------------
def infer_subject_and_topics(text):
    for subject, topics in subject_map.items():
        found = [t for t in topics if t.lower() in text]
        if found:
            return subject, found
    return None, []

# -------------------------------
# INPUT MODE
# -------------------------------
st.markdown("## 🧠 How do you want to start?")

input_mode = st.radio(
    "Choose input method",
    ["Select Preset Syllabus", "Type Subject Name", "Upload PDF Syllabus"]
)

data = None

# -------------------------------
# Preset syllabus mode
# -------------------------------
if input_mode == "Select Preset Syllabus":
    selected = st.selectbox(
        "Choose a syllabus",
        options=["Select"] + list(presets.keys())
    )

    if selected != "Select":
        data = presets[selected]
        st.success(f"{selected} syllabus loaded")

# -------------------------------
# Subject-only input mode
# -------------------------------
if input_mode == "Type Subject Name":
    subject = st.text_input(
        "Enter subject name (e.g., Python, Java, DBMS)"
    ).lower()

    if subject:
        if subject in subject_map:
            data = {
                "subjects": {subject.upper(): subject_map[subject]},
                "weak_topics": [],
                "daily_study_hours": 2
            }
            st.success(f"Topics auto-generated for {subject.upper()}")
        else:
            st.warning("Subject not found. Try Python, Java, DBMS, or Aptitude.")

# -------------------------------
# PDF Upload mode
# -------------------------------
if input_mode == "Upload PDF Syllabus":
    uploaded_pdf = st.file_uploader("Upload syllabus PDF", type=["pdf"])

    if uploaded_pdf:
        text = extract_text_from_pdf(uploaded_pdf)
        subject, topics = infer_subject_and_topics(text)

        if subject and topics:
            data = {
                "subjects": {subject.upper(): topics},
                "weak_topics": [],
                "daily_study_hours": 2
            }
            st.success(f"Syllabus detected as {subject.upper()}")
        else:
            st.warning("Could not detect subject/topics from PDF.")

# -------------------------------
# Generate Study Plan
# -------------------------------
if data and st.button("🚀 Generate Today’s Study Plan"):
    plan, explanation = generate_study_plan(data)
    st.session_state["plan"] = plan
    st.session_state["explanation"] = explanation
    st.session_state["data"] = data

# -------------------------------
# Display Study Plan + References
# -------------------------------
if "plan" in st.session_state:
    st.markdown("### 🗓️ Today’s Study Plan")

    subject_key = list(st.session_state["data"]["subjects"].keys())[0].lower()
    w3_link = w3_links.get(subject_key, "https://www.w3schools.com/")

    for i, item in enumerate(st.session_state["plan"]):
        col1, col2, col3 = st.columns([4, 1, 1])

        with col1:
            st.checkbox(item, key=f"task_{i}")

        topic_text = item.split("-")[1].split("(")[0].strip()
        yt_query = urllib.parse.quote_plus(f"{topic_text} tutorial")
        youtube_link = f"https://www.youtube.com/results?search_query={yt_query}"

        with col2:
            st.markdown(f"[📘 W3Schools]({w3_link})")

        with col3:
            st.markdown(f"[🎥 YouTube]({youtube_link})")

    st.markdown("### 🧠 AI Reasoning")
    st.info(st.session_state["explanation"])

st.markdown("---")
st.caption("AI Study Planner • PDF Upload • Subject Inference • Learning References • Mock Mode")
