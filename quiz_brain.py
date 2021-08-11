class QuizBrain:
    def __init__(self, questions):
        self.question_number = 0
        self.question_list = questions

    def next_question(self):
        answer = input(f"Q.{self.question_number + 1} "
                       f"{self.question_list[self.question_number].question} (True / False)? ").lower()
        print(answer)
        self.question_number += 1
