import json
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

with open("syllabus.json", "r") as file:
    data = json.load(file)

prompt = f"""
You are an AI study planner.

Subjects and topics:
{data["subjects"]}

Weak topics:
{data["weak_topics"]}

Daily study hours: {data["daily_study_hours"]}

Create a study plan for TODAY and explain why you chose each topic.
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}]
)

print("\n🤖 AI STUDY AGENT RESPONSE\n")
print(response.choices[0].message.content)
