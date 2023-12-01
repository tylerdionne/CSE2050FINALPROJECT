from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QRadioButton
from ChoiceQuestion import ChoiceQuestion
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QComboBox, QTextBrowser
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtCore import Qt


class DMVDriverTestUI(QWidget):
    def __init__(self, questions, choiceimagequestions, choicequestions):
        super().__init__()
        self.questions = questions
        self.choiceimagequestions = choiceimagequestions
        self.choicequestions = choicequestions
        self.current_question_index = 0
        self.correct_answers = 0
        self.grid_layout = QGridLayout(self)
        self.setup_ui()

    def setup_ui(self):
        self.setStyleSheet("background-color: white; color: black;")
        self.setWindowTitle("CSE 2050 DMV Driver's Test")
        self.setFixedSize(800, 600)

        # grid_layout = QGridLayout(self)
        # self.grid_layout = QGridLayout(self)

        question = self.questions[self.current_question_index]
        questiontext = question.question_text
        choiceimagequestion = self.choiceimagequestions[self.current_question_index]
        choicequestion = self.choicequestions[self.current_question_index]

        choiceimagequestion.display(self.grid_layout, 0)

        bold_label = QLabel(questiontext)
        bold_label.setWordWrap(True)
        bold_label.setStyleSheet("font-weight: bold; font-size: 20px;")
        self.grid_layout.addWidget(bold_label, 1, 0, 1, 3)

        choicequestion.display(self.grid_layout, 2)

        question_label = QLabel("Question {} of 40     | Correct: {} / 40".format(self.current_question_index + 1,
                                                                                  self.correct_answers))
        self.grid_layout.addWidget(question_label, 7, 0, 1, 3)

        next_button = QPushButton("Next Question", self)
        next_button.setMinimumSize(150, 30)
        next_button.clicked.connect(self.next_question)
        self.grid_layout.addWidget(next_button, 7, 2)

        quit_button = QPushButton("Quit Quiz", self)
        quit_button.setMinimumSize(150, 30)
        quit_button.clicked.connect(QApplication.quit)
        self.grid_layout.addWidget(quit_button, 7, 3)

        self.grid_layout.setRowStretch(8, 0)
        self.grid_layout.setColumnStretch(3, 0)

    def present_question(self):
        self.display(self.grid.layout)
        # response = input("Your answer: ")
        # print(q.check_answer(response))

    def next_question(self):
        current_question = self.questions[self.current_question_index]
        current_choice_question = self.choicequestions[self.current_question_index]
        select = current_choice_question.selected_choice
        if select == current_question.answer:
            self.correct_answers += 1

        if self.current_question_index < 39:
            self.current_question_index = self.current_question_index + 1
            self.clear()
            self.setup_ui()
        else:
            print("Quiz Completed!")

    def clear(self):
        layout = self.layout()
        if layout is not None:
            for i in reversed(range(layout.count())):
                widget_to_remove = layout.itemAt(i).widget()
                layout.removeWidget(widget_to_remove)


                widget_to_remove.setParent(None)
