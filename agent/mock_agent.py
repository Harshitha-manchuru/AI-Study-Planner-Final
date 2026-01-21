def generate_study_plan(data):
    subjects = data["subjects"]
    weak_topics = data["weak_topics"]
    daily_hours = data["daily_study_hours"]

    plan = []
    hours_left = daily_hours

    for subject, topics in subjects.items():
        for topic in topics:
            if hours_left <= 0:
                break

            time = 1.5 if topic in weak_topics else 1
            if time <= hours_left:
                plan.append(f"{subject} - {topic} ({time} hrs)")
                hours_left -= time

    explanation = (
        "I prioritized weak topics first to strengthen fundamentals, "
        "then balanced the plan with core subjects for effective revision."
    )

    return plan, explanation
