from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QFont

class ExclusionWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.sec = 18

        # Label pour l'affichage (toujours 2 chiffres)
        self.lbl = QLabel(f"{self.sec:02d}")
        layout = QHBoxLayout(self)
        layout.addWidget(self.lbl)
        self.setStyleSheet("background-color: black;")
        self.lbl.setStyleSheet("color: white; background-color: black;")
        font = QFont("Arial Black", 84)
        self.lbl.setFont(font)

        # Timer 1000ms
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.tick)
        self.timer.start(1000)

    def tick(self):
        if self.sec > 0:
            self.sec -= 1
            self.lbl.setText(f"{self.sec:02d}")
        else:
            self.hide()  # Le chrono disparaît visuellement
