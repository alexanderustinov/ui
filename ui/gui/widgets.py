from PyQt6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QTextEdit,
    QDateTimeEdit,
)
from PyQt6.QtCore import pyqtSignal, pyqtSlot

from datetime import datetime


class MomentWidget(QDateTimeEdit):
    @pyqtSlot(datetime)
    def update_time(self, now):
        self.setDateTime(now)


class ExitButton(QPushButton):
    myclicked = pyqtSignal(int)

    def __init__(self, *args, **kwargs):
        QPushButton.__init__(self, *args, **kwargs)
        self.clicked.connect(self._activate_myclick)

    def _activate_myclick(self):
        self.myclicked.emit(1)


class Window(QWidget):
    input_changed = pyqtSignal(datetime)

    def __init__(self, app, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)

        self.app = app

        container = QHBoxLayout(self)

        label = QLabel()
        container.addWidget(label)
        self.label = label
        # self._label = label
        # self.__label = label

        edit = QTextEdit()
        container.addWidget(edit)
        edit.textChanged.connect(self.update_label)
        self.edit = edit

        exit_button = ExitButton("Выйти")
        exit_button.myclicked.connect(self.app.quit)
        container.addWidget(exit_button)

        moment = MomentWidget()
        container.addWidget(moment)
        self.input_changed.connect(moment.update_time)

    from ui.gui.actions import update_label
