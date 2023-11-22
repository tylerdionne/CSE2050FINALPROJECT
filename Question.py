# question.py

class Question:
    def __init__(self):
        self.question_text = ""
        self.image_path = ""
        self.answers = []
        self.correct_answer = ""
        self.comments = ""

    def set_text(self, question_text):
        self.question_text = question_text

    def set_image_path(self, image_path):
        self.image_path = image_path

    def add_answer(self, answer_text, is_correct):
        answer = {"text": answer_text, "correct": is_correct}
        self.answers.append(answer)
        if is_correct:
            self.correct_answer = answer_text

    def set_comments(self, comments):
        self.comments = comments

    def display(self, layout):
        label = QLabel(self.question_text)
        layout.addWidget(label)
