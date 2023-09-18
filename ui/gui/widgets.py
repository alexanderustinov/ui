from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QTextEdit

class Window(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)

        container = QHBoxLayout(self)

        exit_button = QPushButton("Выйти")
        container.addWidget(exit_button)


