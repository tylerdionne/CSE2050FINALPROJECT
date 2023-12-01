from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtCore import QRect


# This file contains the ChoiceImageQuestion class.
class ChoiceImageQuestion:
    # The constructor for the ChoiceImageQuestion class.
    def __init__(self):
        super().__init__()
        self.image = bytes()

    # Sets the image.The image is read from the
    # file path and converted to bytes.
    def set_image(self, image_path):
        with open(image_path, "rb") as file:
            self.image = file.read()

    # Displays the image in the UI by
    # adding it as a widget.
    def display(self, layout, row):
        image_label = QLabel()
        pixmap = QPixmap()
        pixmap.loadFromData(self.image)
        pixmap = pixmap.scaled(780, 300)  # Scale the image
        image_label.setPixmap(pixmap)
        layout.addWidget(image_label, row, 0, 1, -1)
