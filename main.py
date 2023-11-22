from PyQt5.QtWidgets import QApplication
from DMVDriverTestUI import DMVDriverTestUI
from XMLParser import XMLParser

def main():
    app = QApplication([])
    xml_parser = XMLParser()
    result = xml_parser.parse("florida_drivers_test.xml")
    questions = result[0]
    choiceimagequestions = result[1]
    choicequestions = result[2]
    ui = DMVDriverTestUI(questions, choiceimagequestions, choicequestions)
    ui.show()
    app.exec_()

main()