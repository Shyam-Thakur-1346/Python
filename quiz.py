# Define a Question class (optional but good practice)
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

# List of questions and options
question_prompts = [
    "1) What is the capital of France?\n(a) London\n(b) Paris\n(c) Rome\n\n",
    "2) Which language is used for web apps?\n(a) Python\n(b) Java\n(c) HTML\n\n",
    "3) What does CPU stand for?\n(a) Central Process Unit\n(b) Central Processing Unit\n(c) Computer Personal Unit\n\n"
]

# Create question objects
questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]

# Function to run the quiz
def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer.lower() == question.answer:
            score += 1
    print(f"You got {score} out of {len(questions)} correct!")

# Run it
run_quiz(questions)
