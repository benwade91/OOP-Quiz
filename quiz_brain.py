class QuizBrain:
    def __init__(self, questions):
        self.question_number = 0
        self.question_list = questions
        self.score = 0

    def next_question(self):
        answer = input(f"Q.{self.question_number + 1} "
                       f"{self.question_list[self.question_number].question} (True / False)? ").lower()

        self.check_answer(answer, self.question_list[self.question_number].answer)
        self.question_number += 1

    def still_has_question(self):
        return len(self.question_list) > self.question_number

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Thats Right!")
            self.score += 1
        else:
            print("wrong")
