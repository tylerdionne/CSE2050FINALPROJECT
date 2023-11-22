
from xml.etree import ElementTree as ET
from Question import Question
from ChoiceImageQuestion import ChoiceImageQuestion
from ChoiceQuestion import ChoiceQuestion

class XMLParser:
    def parse(self, xml_path):
        tree = ET.parse(xml_path)
        root = tree.getroot()
        result = []
        questions = []
        choiceimagequestions = []
        choicequestions = []

        for question_elem in root.findall("question"):
            question = Question("", "")
            choicequestion = ChoiceQuestion("", "")
            choiceimagequestion = ChoiceImageQuestion()

            question.set_text(question_elem.find("questionText").text)
            image_elem = question_elem.find("questionImage")
            if image_elem is not None:
                choiceimagequestion.set_image(image_elem.attrib.get("path", ""))

            for answer_elem in question_elem.findall("answer"):
                is_correct = answer_elem.attrib.get("correct", "").lower() == "true"
                if is_correct:
                    question.set_answer(answer_elem.text)
                    choicequestion.add_choice(answer_elem.text, "true")
                else:
                    choicequestion.add_choice(answer_elem.text, "false")

            comments_elem = question_elem.find("answerComments")
            choicequestion.set_answer_comments(comments_elem.text)

            questions.append(question)
            choiceimagequestions.append(choiceimagequestion)
            choicequestions.append(choicequestion)
        result.append(questions)
        result.append(choiceimagequestions)
        result.append(choicequestions)
        return result
