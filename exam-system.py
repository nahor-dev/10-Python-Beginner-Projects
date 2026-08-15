class Question:
    def __init__(self,question,options,answer):
        self.question = question
        self.options = options
        self.answer = answer
        
        
        
class Quiz:
    def __init__(self):
        self.questions = []
        
    def add_question(self,question):
        self.questions.append(question)
    def take_quiz(self):
        if self.questions:
            for i in enumerate( self.questions, start=1):
                print(i)
        if not self.questions:
            print("No questions available.")   
 
 
 
        
question1 = Question(
    "What is 2 + 2?",
    ["3", "4", "5", "6"],
    "4"
)
quiz = Quiz()
quiz.add_question(question1)


print(len(quiz.add_question()))
