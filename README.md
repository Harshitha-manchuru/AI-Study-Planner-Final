📚 AI Study Planner Agent

An AI-powered study planner that helps students generate structured daily study plans from minimal input such as a subject name, preset syllabus, or uploaded PDF syllabus.
The system also provides trusted learning references for each topic.

🚀 Features

📌 Preset Syllabus Selection (DBMS, Python, Aptitude)

✍️ Subject-only Input (e.g., Python, Java, DBMS)

📄 PDF Syllabus Upload

🧠 Automatic Topic Inference

🗓️ Daily Study Plan Generation

☑️ Progress Tracking (Checkboxes)

📘 W3Schools References

🎥 YouTube Video References

🔒 Secure & GitHub-safe (No API keys exposed)

🧠 Project Motivation

Many students struggle with:

Planning daily study schedules

Understanding how to break a syllabus into manageable tasks

Finding reliable learning resources

This project solves these problems by acting as a smart study assistant that converts syllabus input into an actionable learning plan with references.

🏗️ Architecture Overview
AI-Study-Planner/
│
├── agent/
│   └── mock_agent.py        # AI agent logic (mock mode)
│
├── ui/
│   └── app.py               # Streamlit UI
│
├── data/
│   ├── presets.json         # Predefined syllabi
│   └── subjects_map.json    # Subject → topics mapping
│
├── main.py
├── requirements.txt
├── syllabus.json
├── .gitignore
└── README.md

⚙️ Tech Stack

Python

Streamlit – UI framework

PyPDF2 – PDF text extraction

JSON – Data storage

Git & GitHub – Version control

▶️ How to Run the Project Locally
1️⃣ Clone the repository
git clone https://github.com/Harshitha-manchuru/AI-Study-Planner-Final.git
cd AI-Study-Planner-Final

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the application
streamlit run ui/app.py

🧪 How the System Works

User selects input method:

Preset syllabus

Subject name

PDF syllabus upload

The system infers relevant topics

An AI-style agent generates a daily study plan

Topic-wise learning references are attached

User tracks progress using checkboxes

🔐 Security & Best Practices

.env file is ignored using .gitignore

No API keys or secrets are committed

Mock AI mode used for safe academic demonstrations

Clean Git history maintained

🎓 Academic Use

Suitable for college seminars

Easy to demonstrate offline

Clear modular architecture

Can be extended with real AI APIs in future

🔮 Future Enhancements

Image syllabus upload (OCR)

Database-backed progress tracking

Personalized difficulty adjustment

Cloud deployment

Real LLM integration

👩‍💻 Author

Harshitha Manchuru
BCA Student
AI Study Planner – Academic Project

📌 License

This project is for educational purposes only