
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

        #grid_layout = QGridLayout(self)
        #self.grid_layout = QGridLayout(self)

        question = self.questions[self.current_question_index]
        questiontext = question.question_text
        choiceimagequestion = self.choiceimagequestions[self.current_question_index]
        choicequestion = self.choicequestions[self.current_question_index]

        choiceimagequestion.display(self.grid_layout)

        bold_label = QLabel(questiontext)
        bold_label.setStyleSheet("font-weight: bold; font-size: 20px;")
        self.grid_layout.addWidget(bold_label)

        choicequestion.display(self.grid_layout)

        question_label = QLabel("Question {} of 40     | Correct: {} / 40".format(self.current_question_index,  self.correct_answers))
        self.grid_layout.addWidget(question_label, 8, 0, 1, 1)

        next_button = QPushButton("Next Question", self)
        next_button.clicked.connect(self.next_question)
        self.grid_layout.addWidget(next_button, 8, 1, 1, 1)
        
        quit_button = QPushButton("Quit Quiz", self)
        quit_button.clicked.connect(QApplication.quit)
        self.grid_layout.addWidget(quit_button, 8, 2, 1, 1)

    def present_question(q):
        q.display(self.grid.layout)
        #response = input("Your answer: ")
        #print(q.check_answer(response))

    def next_question(self):
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


