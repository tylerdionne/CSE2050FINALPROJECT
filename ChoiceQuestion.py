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

    def display(self, layout):
        bold_label = QLabel("")
        bold_label.setStyleSheet("font-weight: bold; font-size: 20px;")
        layout.addWidget(bold_label)
        '''
        for choice_data in self.choices:
            choice_radio = QRadioButton(choice_data[0])
            layout.addWidget(choice_radio)

        layout.addWidget(QLabel(self.answer_comments))
        '''
        for choice_data in self.choices:
            choice_radio = QRadioButton(choice_data[0])
            choice_radio.toggled.connect(lambda state, choice=choice_data[0]: self.choice_selected(choice, state) if state else None)
            layout.addWidget(choice_radio)

        self.answer_label = QLabel(self.answer_comments)
        layout.addWidget(self.answer_label)
        self.answer_label.hide()

    def choice_selected(self, choice, state):
        if state:
            self.selected_choice = choice
            self.answer_label.show()

