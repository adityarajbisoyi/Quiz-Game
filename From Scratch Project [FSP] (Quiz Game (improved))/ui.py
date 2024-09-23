from tkinter import *
from brain import QuizBrain

BG = "#00246B"
FG = "#CADCFC"
FINISH_BG = "yellow"
FINISH_FG = "red"


class QuizUserInterface:
    def __init__(self, quiz: QuizBrain):
        """ creating a quiz attribute of QuizUserInterface class which is a copy of the quiz object from the QuizBrain class that we created inside the brain module."""
        self.quiz = quiz

        # with the help of the local quiz object we can call the method we declared in brain module, hence using show_options() for getting a dict of options
        self.options = self.quiz.show_options()

        # creating a window object of the Tk class from the tkinter module
        self.windows = Tk()
        self.windows.title("Quiz Game! ")
        self.windows.config(bg="#00246B", padx=20, pady=20)

        # creating a label to get track of the score.
        self.score = Label(text=f"SCORE : {self.quiz.returns_score()}", font=("Arial", 25, "italic"), fg="#CADCFC",
                           bg="#00246B")

        # creating a canvas with appropriate size and dimensions
        self.canvas = Canvas(width=400, height=300, bg="#CADCFC")

        # creating a text item inside the canvas object
        self.question = self.canvas.create_text(200, 100, text=f"Q. {quiz.display_question()}",
                                                font=("Arial", 20, "italic"),
                                                width=350)

        # creating radio buttons and assigning them to the dynamic variable holder radio i.e. an object of class StringVar default value is null
        self.radio = StringVar()
        self.radio.set("option")

        # each radio buttons have a value which onclick assigned to the dynamic string holder object radio from StringVar class
        self.option_1 = Radiobutton(self.windows, text=self.options[1], value=self.options[1], width=100,
                                    variable=self.radio, command=self.move_next, font=("Arial", 15, "italic"),
                                    activebackground="orange", activeforeground="red", selectcolor="yellow",
                                    highlightcolor="blue", background=FG)

        self.option_2 = Radiobutton(self.windows, text=self.options[2], value=self.options[2], width=100,
                                    variable=self.radio, command=self.move_next, font=("Arial", 15, "italic"),
                                    activebackground="orange", activeforeground="red", selectcolor="yellow",
                                    highlightcolor="blue", background=FG)

        self.option_3 = Radiobutton(self.windows, text=self.options[3], value=self.options[3], width=100,
                                    variable=self.radio, command=self.move_next, font=("Arial", 15, "italic"),
                                    activebackground="orange", activeforeground="red", selectcolor="yellow",
                                    highlightcolor="blue", background=FG)

        self.option_4 = Radiobutton(self.windows, text=self.options[4], value=self.options[4], width=100,
                                    variable=self.radio, command=self.move_next, font=("Arial", 15, "italic"),
                                    activebackground="orange", activeforeground="red", selectcolor="yellow",
                                    highlightcolor="blue", background=FG)

        # putting everything on the windows by using grid method
        self.score.grid(row=0, column=1, columnspan=2)
        self.canvas.grid(row=1, column=0, columnspan=4, pady=50)
        self.option_1.grid(row=2, column=1)
        self.option_2.grid(row=3, column=1)
        self.option_3.grid(row=4, column=1)
        self.option_4.grid(row=5, column=1)

        # this is the end of the mainloop for window object of Tk class
        self.windows.mainloop()

    def update_option(self):
        """update the choices for the next questions"""
        ans = self.radio.get()
        self.quiz.set_answer(ans)
        print(f"Your choice = {self.radio.get()}\nCorrect Choice = {self.quiz.give_answer()}")

    def move_next(self):
        """Update the User Interface and display the next question in GUI"""
        if not self.quiz.is_game_ended():
            self.update_option()
            self.quiz.next_question()
            self.options = self.quiz.show_options()
            self.option_1.config(text=self.options[1], value=self.options[1])
            self.option_2.config(text=self.options[2], value=self.options[2])
            self.option_3.config(text=self.options[3], value=self.options[3])
            self.option_4.config(text=self.options[4], value=self.options[4])
            self.canvas.itemconfig(self.question, text=self.quiz.display_question())
            self.score.config(text=f"SCORE : {self.quiz.returns_score()}")
        else:
            self.stop_after_finishing()

    def stop_after_finishing(self):
        """Declared for stopping the program after all questions are completed"""
        self.canvas.itemconfig(self.question,
                               text=f"Congratulations you scored {self.quiz.returns_score()}/20",
                               fill=FINISH_BG, width=500)
        self.canvas.config(bg=BG, width=600, height=400)
        self.windows.config(bg=FG)
        self.windows.minsize(width=800, height=600)
        self.option_1.grid_forget()
        self.option_2.grid_forget()
        self.option_3.grid_forget()
        self.option_4.grid_forget()
        self.score.grid_forget()
        self.canvas.grid_forget()
        self.canvas.pack()
