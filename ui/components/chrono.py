from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QFont

class ChronoWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.min = 8
        self.sec = 0
        self.lbl = QLabel(f"{self.min:02d}:{self.sec:02d}")
        layout = QHBoxLayout(self)
        layout.addWidget(self.lbl)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.tick)
        self.timer.start(1000)
        # Couleur de l'arrière plan du widget complet
        self.setStyleSheet("background-color: black;")
        # Couleur du texte et de l'arrière plan du label
        self.lbl.setStyleSheet("color: red; background-color: black;")
        # Taille et police des chiffres
        font = QFont("Arial Black", 84)
        self.lbl.setFont(font)


    # -1min = +59s
    def tick(self):
        if self.sec == 0:
            if self.min == 0:
                self.timer.stop()
            else:
                self.min -= 1
                self.sec = 59
        else:
            self.sec -= 1

        #format mm:ss
        self.lbl.setText(f"{self.min:02d}:{self.sec:02d}")
