from PyQt5.QtWidgets import QApplication
from DMVDriverTestUI import DMVDriverTestUI
from XMLParser import XMLParser

def main():
    app = QApplication([])
    # Create an instance of the XMLParser and parse the XML file
    xml_parser = XMLParser()
    # Parse the XML file
    questions = xml_parser.parse("florida_drivers_test.xml")
    # Check if questions were successfully loaded
    if not questions:
        print("Error: No questions loaded.")
        return
    # Create an instance of the DMVDriverTestUI with the loaded questions
    ui = DMVDriverTestUI(questions)
    ui.show()
    app.exec_()

main()