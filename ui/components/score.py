from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class ScoreWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.value = 0
        self.label = QLabel(f"{self.value:02d}")
        # Style du label
        self.label.setStyleSheet("color: blue; background: black;")
        # Style de la police
        self.label.setFont(QFont("Arial Black", 120))
        self.label.setAlignment(Qt.AlignCenter)

        layout = QHBoxLayout(self)
        layout.addWidget(self.label)
        layout.setContentsMargins(0,0,0,0)

    def set_score(self, value):
        self.value = value
        #Format 2 digits
        self.label.setText(f"{self.value:02d}")
    #Actualiser le score
    def get_score(self):
        return self.value
