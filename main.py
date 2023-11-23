from PyQt5.QtWidgets import QApplication
from DMVDriverTestUI import DMVDriverTestUI
from XMLParser import XMLParser


# Driver code to run the driver test app.
def main():
    app = QApplication([])  # Create the application.
    xml_parser = XMLParser()    # Create the XML parser.

    result = xml_parser.parse("florida_drivers_test.xml")   # Parse the XML file.
    questions = result[0]   # Get the questions.
    choiceimagequestions = result[1]
    choicequestions = result[2]  # Get the choice questions.

    ui = DMVDriverTestUI(questions,
                         choiceimagequestions,
                         choicequestions)   # Create the UI.
    
    ui.show()   # Show the UI.

    app.exec_()    # Run the application.


main()
