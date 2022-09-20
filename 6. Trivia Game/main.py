from question_model import Question
from data import  question_data
from quiz_brain import  QuizzBrain
question_bank = []

for questions in question_data:
    question_text = questions["question"]
    question_answer = questions["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quizz = QuizzBrain(question_bank)

while quizz.still_has_questions():
    quizz.next_question()

print("You've Completed the quizz")
print(f"Your Final score is: {quizz.score} / {quizz.question_number}\n")

