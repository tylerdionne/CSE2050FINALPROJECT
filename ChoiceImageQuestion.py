from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtCore import QRect
class ChoiceImageQuestion():
    def __init__(self):
        super().__init__()
        self.image = bytes()

    def set_image(self, image_path):
        with open(image_path, "rb") as file:
            self.image = file.read()

    def display(self, layout):
        image_label = QLabel()
        pixmap = QPixmap()
        pixmap.loadFromData(self.image)
        image_label.setPixmap(pixmap)
        layout.addWidget(image_label)