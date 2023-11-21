### XMLParser.py
import xml.etree.ElementTree as ET

class XMLParser:
    def __init__(self, xml_file):
        self.xml_file = xml_file

    def parse(self):
        tree = ET.parse(self.xml_file)
        root = tree.getroot()

        questions = []

        for question_elem in root.findall("question"):
            question_type = question_elem.get("type")

            if question_type == "choice":
                question = ChoiceQuestion()
                for choice_elem in question_elem.findall("choice"):
                    choice_text = choice_elem.text
                    is_correct = choice_elem.get("correct") == "True"
                    question.add_choice(choice_text, is_correct)
                question.set_answer_comments(question_elem.find("answer_comments").text)
            elif question_type == "image_choice":
                question = ChoiceImageQuestion()
                question.set_image(question_elem.find("image_path").text)
                for choice_elem in question_elem.findall("choice"):
                    choice_text = choice_elem.text
                    is_correct = choice_elem.get("correct") == "True"
                    question.add_choice(choice_text, is_correct)
                question.set_answer_comments(question_elem.find("answer_comments").text)
            else:
                question = Question()

            question.set_text(question_elem.find("question_text").text)
            question.set_answer(question_elem.find("answer").text)

            questions.append(question)

        return questions

