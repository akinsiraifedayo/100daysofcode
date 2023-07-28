from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import random

question_bank = []
random.shuffle(question_data)

for data in question_data:
    question_text = data["question"]
    question_answer = data["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.max_questions()
while quiz.still_has_questions():
    quiz.next_question()
print("You have completed the Quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
