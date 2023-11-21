def main():
    app = QApplication([])
    xml_parser = XMLParser("florida_drivers_test.xml")
    questions = xml_parser.parse()
    ui = DMVDriverTestUI(questions)
    ui.show()
    app.exec_()

    main()