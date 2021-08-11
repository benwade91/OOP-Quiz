from question_model import Question
from data import open_tdb_data
from quiz_brain import QuizBrain

question_bank = []

for question in open_tdb_data:
    text = question['question']
    answer = question['correct_answer']
    new_question = Question(text, answer)
    question_bank.append(new_question)

game = QuizBrain(question_bank)

while game.still_has_question():
    game.next_question()

print("Game Over")
print(f"Your final score is {game.score}/{len(question_bank)}")
