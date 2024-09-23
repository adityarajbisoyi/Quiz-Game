from brain import QuizBrain
from ui import QuizUserInterface

# creating a quiz_1 object from QuizBrain class
quiz_1 = QuizBrain()

# creating an ui object from QuizUserInterface class and passing the quiz_1 object as a parameter
ui = QuizUserInterface(quiz_1)
