class QuizBrain:

    def __init__(self,q_list):
        self.question_number = 0
        self.q_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.q_list)
    
    def check_answer(self,answer,correct_answer):
        return answer.lower() == correct_answer.lower()

    def next_question(self):
            current_q = self.q_list[self.question_number].text
            self.question_number +=1
            answer = input(str(self.question_number)+ ". " + current_q + " True/False?")
            correct_answer = self.q_list[self.question_number].answer
            
            if self.check_answer(answer,correct_answer):
                print("Correct")
                self.score += 1
            else:
                print("Wrong")
                print(f'Correct answer was: {correct_answer}')
            print(f'Current score is {self.score}/{self.question_number}')
                     
            while self.still_has_questions() == True:   
                self.next_question()
            
            if self.still_has_questions == False:
                print("You have completed the quiz")
                print(f'Score was: {self.score}/{self.question_number}')