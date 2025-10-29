from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class PeriodeWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.value = 1  # Démarre à 1
        self.label = QLabel(str(self.value))
        self.label.setStyleSheet("color:#92d050; background: black;")
        self.label.setFont(QFont("Arial Black", 120))
        self.label.setAlignment(Qt.AlignCenter)

        layout = QHBoxLayout(self)
        layout.addWidget(self.label)
        layout.setContentsMargins(0,0,0,0)

    def set_periode(self, value):
        self.value = value
        self.label.setText(str(self.value))

    def get_periode(self):
        return self.value
