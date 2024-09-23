from data import question_bank
import random


class QuizBrain:

    # pick up a random question from the question bank
    # initialize the score as 0,user_answer as empty string, and option as empty dict,also counter as 0,completed_list as an empty list
    def __init__(self):
        self.completed_questions = []
        self.que = random.choice(question_bank)
        self.score = 0
        self.options = {}
        self.user_answer = ""
        self.counter = 0

    def next_question(self):
        """change the current question appends the current question ,checks the que in completed_questions[] attribute , if question is already asked then change the question"""
        self.completed_questions.append(self.que)
        while self.que in self.completed_questions:
            self.que = random.choice(question_bank)
        self.counter += 1

    def display_question(self):
        """returns the current question stored in que attribute"""
        return self.que["question"]

    def check_correct_answer(self):
        """returns true or false, checks for the condition whether correct_answer is equal to the user_answer"""
        return self.que["correct_answer"] == self.user_answer

    def set_answer(self, answer):
        """take a string as an input and  assign to attribute user_answer if answer is correct then increase the score attribute by 1"""
        self.user_answer = answer
        if self.check_correct_answer():
            self.score += 1

    def show_options(self):
        """combine the correct_answer and incorrect_answers key values and add it to a dict, returns the same dict"""
        list_of_answers = [answers for answers in self.que["incorrect_answers"]]
        list_of_answers.append(self.que["correct_answer"])
        random.shuffle(list_of_answers)
        options = {i + 1: list_of_answers[i] for i in range(4)}
        return options

    def returns_score(self):
        """returns the current score to the caller"""
        return self.score

    def give_answer(self):
        """returns the correct answer of the current question viz stored in que"""
        return self.que["correct_answer"]

    def is_game_ended(self) -> bool:
        """check whether the game has ended or not based on the value of counter which increases on each transition of question,return true or false(restricted)"""
        return self.counter == 19
