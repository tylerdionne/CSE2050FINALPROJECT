from Question import Question
class ChoiceQuestion(Question):
    def __init__(self):
        super().__init__()
        self.choices = []
        self.answer_comments = ""

    def add_choice(self, choice, correct):
        self.choices.append({"choice": choice, "correct": correct})

    def set_answer_comments(self, comments):
        self.answer_comments = comments

    def display(self, layout):
        super().display(layout)
        for choice_data in self.choices:
            choice_radio = QRadioButton(choice_data["choice"])
            layout.addWidget(choice_radio)

        layout.addWidget(QLabel(self.answer_comments))

