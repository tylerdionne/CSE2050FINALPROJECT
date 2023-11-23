"""
This file contains the Question class.
This class is used to create a question object
that contains the question text
and the answer to the question.
"""


class Question:
    # The constructor for the Question class.
    def __init__(self, question_text, answer):
        self.question_text = question_text
        self.answer = answer

    # Sets the question text.
    def set_text(self, question_text):
        self.question_text = question_text

    # Sets the answer to the question.
    def set_answer(self, answer_text):
        self.answer = answer_text

    # Checks if the answer is correct.
    def check_answer(self, answer_text):
        return self.answer == answer_text

    # Displays the question.
    def display(self, layout):
        label = QLabel(self.question_text)
        layout.addWidget(label)
