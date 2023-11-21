class Question:
    def __init__(self):
        self.question_text = ""
        self.answer = ""

    def set_text(self, question_text):
        self.question_text = question_text

    def set_answer(self, answer_text):
        self.answer = answer_text

    def check_answer(self, answer_text):
        return self.answer == answer_text

    def display(self, layout):
        label = QLabel(self.question_text)
        layout.addWidget(label)

