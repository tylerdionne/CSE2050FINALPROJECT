from Question import Question
from PyQt5.QtWidgets import QRadioButton
from PyQt5.QtWidgets import QLabel


class ChoiceQuestion(Question):
    selected_choice = None

    def __init__(self, question_text, answer):
        super().__init__(question_text, answer)
        self.choices = []
        self.answer_comments = ""
        self.selected_choice = None

    def add_choice(self, choice, correct):
        self.choices.append((choice, correct))

    def set_answer_comments(self, comments):
        self.answer_comments = comments

    def display(self, layout, start_row):
        bold_label = QLabel(self.question_text)
        bold_label.setStyleSheet("font-weight: bold; font-size: 20px;")
        layout.addWidget(bold_label, start_row, 0, 1, 3)  # Span across 3 columns for the question text

        row = start_row + 1
        for choice_data in self.choices:
            choice_radio = QRadioButton(choice_data[0])
            choice_radio.setStyleSheet("font-size: 16px;")
            choice_radio.toggled.connect(lambda state, choice=choice_data[0]: self.choice_selected(choice, state) if state else None)
            layout.addWidget(choice_radio, row, 0, 1, -1)  # Span across 3 columns for each choice
            row += 1

        self.answer_label = QLabel(self.answer_comments)
        layout.addWidget(self.answer_label, row, 0, 1, 3)  # Span across 3 columns for the answer comments
        self.answer_label.hide()

    def choice_selected(self, choice, state):
        if state:
            self.selected_choice = choice
            self.answer_label.show()

