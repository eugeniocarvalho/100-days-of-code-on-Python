from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
  my_question = Question(question["text"], question["answer"])
  question_bank.append(my_question)


quiz = QuizBrain(question_bank)
is_correct = True

while quiz.still_has_questions():
  is_correct = quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.get_score()}")