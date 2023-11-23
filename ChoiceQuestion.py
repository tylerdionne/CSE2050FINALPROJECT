from Question import Question
from PyQt5.QtWidgets import QRadioButton
from PyQt5.QtWidgets import QLabel


# TODO: Layout variable is not used.
class ChoiceQuestion(Question):
    # The constructor for the ChoiceQuestion class.
    def __init__(self, question_text, answer):
        super().__init__(question_text, answer)
        self.choices = []
        self.answer_comments = ""

    # Adds a choice to the question.
    def add_choice(self, choice, correct):
        self.choices.append((choice, correct))

    # Sets the answer comments.
    def set_answer_comments(self, comments):
        self.answer_comments = comments

    # Displays the question.
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
            choice_radio.toggled.connect(lambda state, choice=choice_data[0]: self.choice_selected(
                choice, state, layout))
            layout.addWidget(choice_radio)

        self.answer_label = QLabel(self.answer_comments)
        layout.addWidget(self.answer_label)
        self.answer_label.hide()

    # Checks if the answer is correct.
    def choice_selected(self, choice, state, layout):
        if state:
            self.selected_choice = choice
            self.answer_label.show()

            if self.selected_choice == self.answer:
                print("Correct answer!")
