class QuizBrain:

    def __init__(self, q_list) -> None:
        self.q_no = 0
        self.q_list = q_list
        self.score = 0

    def next_question(self):
        current_q = self.q_list[self.q_no]
        self.q_no += 1
        u_answer = input(f"Q.{self.q_no}: {current_q.text} (True/False:) ")
        self.check_answer(u_answer, current_q.answer)

    def still_has_questions(self):
        return self.q_no < len(self.q_list)

    def check_answer(self, u_answer, c_answer):
        if u_answer.lower() == c_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's Wrong.")
        print(f"The correct answer was: {c_answer}")
        print(f"Your score is: {self.score}/{self.q_no}")
        print("\n")
