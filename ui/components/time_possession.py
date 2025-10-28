from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QFont

class TimePossessionWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.sec = 28
        self.lbl = QLabel(f"{self.sec:02d}")
        layout = QHBoxLayout(self)
        layout.addWidget(self.lbl)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.tick)
        self.timer.start(1000)
        # Couleur du component complet
        self.setStyleSheet("background-color: black;")
        # Couleur du texte et de l'arrière plan du label
        self.lbl.setStyleSheet("color: orange; background-color: black;")
        # Taille police
        font = QFont("Arial Black", 72)
        self.lbl.setFont(font)

    def tick(self):
        if self.sec == 0:
            self.timer.stop()
        else:
            self.sec -= 1
        #format ss
        self.lbl.setText(f"{self.sec:02d}")
