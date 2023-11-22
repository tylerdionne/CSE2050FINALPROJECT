# XMLParser.py

from xml.etree import ElementTree as ET
from Question import Question

class XMLParser:
    @staticmethod
    def parse(xml_path):
        tree = ET.parse(xml_path)
        root = tree.getroot()

        questions = []

        for question_elem in root.findall("question"):
            question = Question()

            # Parse question text
            question.set_text(question_elem.find("questionText").text)

            # Parse image path
            image_elem = question_elem.find("questionImage")
            if image_elem is not None:
                question.set_image_path(image_elem.attrib.get("path", ""))

            # Parse answers
            for answer_elem in question_elem.findall("answer"):
                is_correct = answer_elem.attrib.get("correct", "").lower() == "true"
                question.add_answer(answer_elem.text, is_correct)

            # Parse comments
            comments_elem = question_elem.find("answerComments")
            if comments_elem is not None:
                question.set_comments(comments_elem.text)

            questions.append(question)

        return questions
