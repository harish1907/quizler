from question_model import *
from data import *
from quiz_brain import *

question_list = []
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    question_list.append(Question(question_text, question_answer))
quiz = QuizBrain(question_list)

while quiz.still_has_question():
    quiz.nextQuestion()
print("You've complete the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")