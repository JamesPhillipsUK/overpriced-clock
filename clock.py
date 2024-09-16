"""clock.py
A simple Python-powered clock for my Raspberry Pi.  Using PyQt5.

Author: Jesse Phillips <jesse@jessephillips.uk>
"""
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import datetime
import sys


class MainWindow(QMainWindow):
    greeting = ""
    time = ""
    font = QFont()
    largeFont = QFont()

    def __init__(self):
        """ Constructor for the clock's main window. Executed when clock opens.
        """
        super().__init__()

        self.setWindowTitle("Clock")
        self.setStyleSheet("background-color: #212121; color:#FFBF00;")

        self.setContents()

        timer = QTimer(self)
        timer.setSingleShot(False)
        timer.timeout.connect(self.updateContents)
        timer.start(1000)

    def setContents(self):
        """ Method to set the contents of the clock.
        """
        self.font.setFamily("Ubuntu")
        self.font.setBold(True)
        self.font.setPointSize(64)

        self.largeFont.setFamily("Ubuntu")
        self.largeFont.setBold(True)
        self.largeFont.setPointSize(128)

        self.introLabel = QLabel(self)
        self.introLabel.setFont(self.font)
        self.timeLabel = QLabel(self)
        self.timeLabel.setFont(self.largeFont)
        self.greetingLabel = QLabel(self)
        self.greetingLabel.setFont(self.font)

    def updateContents(self):
        """ Method to update the contents of the clock.  Called every second.
        """
        self.time = datetime.datetime.now().strftime('%H:%M:%S')
        now = datetime.datetime.now().time()
        if now < datetime.time(12) and now >= datetime.time(6):
            self.greeting = "Good morning"
        elif now >= datetime.time(12) and now < datetime.time(18):
            self.greeting = "Good afternoon"
        elif now >= datetime.time(18) and now < datetime.time(22):
            self.greeting = "Good evening"
        else:
            self.greeting = "Good night"

        self.introLabel.setText("The time is:")
        self.introLabel.adjustSize()
        x = int((self.width() / 2) - (self.introLabel.width() / 2))
        y = int((self.height() / 3) - (self.introLabel.height()))
        self.introLabel.move(x, y)

        self.timeLabel.setText(self.time)
        self.timeLabel.adjustSize()
        x = int((self.width() / 2) - (self.timeLabel.width() / 2))
        y = int((self.height() / 2) - (self.timeLabel.height() / 2))
        self.timeLabel.move(x, y)

        self.greetingLabel.setText(self.greeting)
        self.greetingLabel.adjustSize()
        x = int((self.width() / 2) - (self.greetingLabel.width() / 2))
        y = int(2 * (self.height() / 3))
        self.greetingLabel.move(x, y)


def main():
    """ Main method for the application.
    """
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showFullScreen()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
