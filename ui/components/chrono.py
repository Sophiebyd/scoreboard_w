from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QFont

class ChronoWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.min = 1
        self.sec = 5
        self.dix = 0
        self.mode_dixieme = False

        self.lbl = QLabel(f"{self.min:02d}:{self.sec:02d}")
        layout = QHBoxLayout(self)
        layout.addWidget(self.lbl)
        self.setStyleSheet("background-color: black;")
        self.lbl.setStyleSheet("color: red; background-color: black;")
        font = QFont("Arial Black", 84)
        self.lbl.setFont(font)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.tick)
        self.timer.start(1000)

    def tick(self):
        # MODE CLASSIQUE (minutes/secondes)
        if not self.mode_dixieme:
            if self.sec == 0:
                if self.min == 0:
                    self.timer.stop()
                    self.lbl.setText("00:00.0") # Fin de chrono, on affiche 0
                else:
                    self.min -= 1
                    self.sec = 59
            else:
                self.sec -= 1

            # Transition : quand il reste moins d'une minute, passe aux dixièmes
            if self.min == 0 and self.sec == 59:
                self.mode_dixieme = True
                self.dix = 9
                self.lbl.setText(f"{self.sec}.{self.dix}")
                self.timer.stop()
                self.timer.setInterval(100)
                self.timer.start()
            else:
                self.lbl.setText(f"{self.min:02d}:{self.sec:02d}")

        # MODE DIXIEMES (dernière minute)
        else:
            if self.dix == 0:
                if self.min == 0 and self.sec == 0:
                    self.timer.stop()
                    self.lbl.setText("00.0")
                    return
                else:
                    self.sec -= 1
                    self.dix = 9
            else:
                self.dix -= 1
            self.lbl.setText(f"{self.sec}.{self.dix}")
