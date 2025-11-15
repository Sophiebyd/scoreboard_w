from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QColor

class CercleWidget(QWidget):
    def __init__(self, couleur="blue", diametre=22, parent=None):
        super().__init__(parent)
        self.couleur = couleur
        self.diam = diametre
        self.plein = False  # État: vide (False) ou plein (True)
        self.setFixedSize(diametre, diametre)

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(QColor(self.couleur))
        if self.plein:
            qp.setBrush(QColor(self.couleur))  # Cercle rempli
        else:
            qp.setBrush(QColor(255,255,255))  # Cercle vide (blanc)
        qp.drawEllipse(2, 2, self.diam-4, self.diam-4)

    def mousePressEvent(self, event):
        self.plein = not self.plein  # Inverse l’état
        self.update()                # Redessine le widget
