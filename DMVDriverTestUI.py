from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QRadioButton
from ChoiceQuestion import ChoiceQuestion
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QComboBox, QTextBrowser


class DMVDriverTestUI(QWidget):
    def __init__(self, questions, choiceimagequestions, choicequestions):
        super().__init__()
        self.questions = questions
        self.choiceimagequestions = choiceimagequestions
        self.choicequestions = choicequestions
        self.current_question_index = 0
        self.correct_answers = 0
        self.setup_ui()
    def setup_ui(self):
        self.setStyleSheet("background-color: white; color: black;")
        self.setGeometry(100, 100, 750, 700)
        self.setWindowTitle("CSE 2050 DMV Driver's Test")
        question = self.questions[self.current_question_index]
        questiontext = question.question_text
        choiceimagequestion = self.choiceimagequestions[self.current_question_index]
        choicequestion = self.choicequestions[self.current_question_index]
        self.layout = QVBoxLayout(self)
        choiceimagequestion.display(self.layout)
        #first the image then the question
        #self.present_question(choicequestion)


        self.select_button = QPushButton("Next Question", self)
        self.select_button.setGeometry(560, 620, 100, 20)
        #self.select_button.clicked(self.next_question)
        self.select_button.setStyleSheet("background-color: darkgrey;")

        self.exit_button = QPushButton("Quit Quiz", self)
        self.exit_button.setGeometry(610, 620, 100, 20)
        self.exit_button.clicked.connect(QApplication.quit)
        self.exit_button.setStyleSheet("background-color: darkgrey;")

    def present_question(q):
        q.display()  # update this display to use the GUI.
        response = input("Your answer: ")
        print(q.check_answer(response))

    def next_question (self):
        self.current_question_index =  self.current_question_index + 1
        self.clear()

        def clear(self):
            item = self.layout.itemAt(1)  # locate your widget number
            if item is not None:
                widget = item.widget()
            if widget is not None:
                self.layout.removeWidget(widget)
            # delete the reference in memory as well
            widget.deleteLater()