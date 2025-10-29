from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QColor

class CercleWidget(QWidget):
    def __init__(self, couleur="blue", diametre=22, parent=None):
        super().__init__(parent)
        # Stocke la couleur choisie pour le cercle
        self.couleur = couleur
        # Stocke le diamètre du cercle
        self.diam = diametre
        # Fixe la taille du widget pour que le cercle soit parfaitement rond
        self.setFixedSize(diametre, diametre)

    def paintEvent(self, event):
        # paintEvent est appelée automatiquement à chaque fois que le widget doit être affiché/redessiné
        qp = QPainter(self)                         # Crée le "pinceau" PyQt pour dessiner
        qp.setRenderHint(QPainter.Antialiasing)     # Active l'anticrénelage pour des bords plus lisses
        qp.setPen(QColor(self.couleur))             # Définit la couleur du contour du cercle
        qp.setBrush(QColor(self.couleur))           # Définit la couleur de remplissage du cercle
        # Dessine le cercle : ellipse centrée avec un petit "marge" (ici 2 px)
        qp.drawEllipse(2, 2, self.diam-4, self.diam-4)
