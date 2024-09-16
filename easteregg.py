"""easteregg.py
Easter eggs for a simple Python-powered clock.  Using PyQt5.

Author: Jesse Phillips <jesse@jessephillips.uk>
"""
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget, QMessageBox
import datetime


class Egg(QWidget):
    clicked = False

    def __init__(self) -> None:
        """ Constructor for the easter egg class.  Starts the egg timers.
        """
        super().__init__()
        eggTimer = QTimer(self)
        eggTimer.setSingleShot(False)
        eggTimer.timeout.connect(self.runEvents)
        eggTimer.start(1000)

    def runEvents(self) -> None:
        """ Run popup events on specific days.
        """
        if (datetime.datetime.now().month == 10 and
                datetime.datetime.now().day == 31):
            self.popup = QMessageBox(self)
            self.popup.setText("Boo!")
            self.popup.exec_()
        elif (datetime.datetime.now().month == 12 and
              datetime.datetime.now().day == 25):
            self.popup = QMessageBox(self)
            self.popup.setText("Ho ho ho!")
            self.popup.exec_()
        elif (datetime.datetime.now().year == 2038 and
              datetime.datetime.now().month == 1 and
              datetime.datetime.now().day == 19):
            self.popup = QMessageBox(self)
            self.popup.setText("Uh oh!")
            self.popup.exec_()
