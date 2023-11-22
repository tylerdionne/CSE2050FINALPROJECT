from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QRadioButton
from PyQt5.QtGui import QPixmap
from ChoiceImageQuestion import ChoiceImageQuestion
from ChoiceQuestion import ChoiceQuestion

class DMVDriverTestUI(QWidget):
    def __init__(self, question_list):
        super().__init__()
        self.question_list = question_list
        self.current_question_index = 0
        self.correct_answers = 0

        self.setup_ui()

    def setup_ui(self):
        self.layout = QVBoxLayout(self)

        self.question_label = QLabel()
        self.layout.addWidget(self.question_label)

        self.answer_label = QLabel()
        self.layout.addWidget(self.answer_label)

        self.display_current_question()

    def display_current_question(self):
        if self.current_question_index < len(self.question_list):
            question = self.question_list[self.current_question_index]
            self.question_label.setText(question.question_text)

            if isinstance(question, ChoiceImageQuestion):
                image_label = QLabel()
                pixmap = QPixmap()
                pixmap.loadFromData(question.image)
                image_label.setPixmap(pixmap)
                self.layout.addWidget(image_label)

            if isinstance(question, ChoiceQuestion):
                for choice_data in question.choices:
                    choice_radio = QRadioButton(choice_data["choice"])
                    choice_radio.toggled.connect(lambda state, data=choice_data: self.check_answer(data["choice"], state))
                    self.layout.addWidget(choice_radio)

    def check_answer(self, selected_answer, state):
        question = self.question_list[self.current_question_index]

        if state and question.check_answer(selected_answer):
            self.correct_answers += 1

        for i in range(self.layout.count()):
            widget = self.layout.itemAt(i).widget()
            if isinstance(widget, QRadioButton):
                widget.setDisabled(True)

        self.answer_label.setText(question.answer_comments)

    def next_question(self):
        if self.current_question_index < len(self.question_list) - 1:
            self.current_question_index += 1

            for i in reversed(range(self.layout.count())):
                widget = self.layout.itemAt(i).widget()
                if widget:
                    widget.setParent(None)

            self.display_current_question()
        else:
            # Display final results or handle end of questions
            self.layout.addWidget(QLabel("End of questions"))

# Add import statement for QRadioButton
from PyQt5.QtWidgets import QRadioButton
