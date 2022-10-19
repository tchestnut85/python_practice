from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

QUESTION_KEY = "question"
ANSWER_KEY = "correct_answer"

def start_quiz():
    question_bank = []

    for question in question_data:
        new_entry = Question(question[QUESTION_KEY], question[ANSWER_KEY])
        question_bank.append(new_entry)

    quiz = QuizBrain(question_bank)
    quiz.next_question()

    while quiz.still_has_questions():
        quiz.next_question()

    print(f"""
    You've completed the quiz.
    Your final score is: {quiz.score}/{len(question_bank)}
    """)

start_quiz()
