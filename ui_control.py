from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QGridLayout, QPushButton
from PyQt5.QtCore import Qt
from settings import *
from fault_button import FaultButton

class ControlWindow(QWidget):
    def __init__(self, display):
        super().__init__()
        self.display = display
        # ... toutes tes variables d’état (scores, période, ...)
        # ... création layout général QGridLayout

        # Ajoute les boutons FaultButton pour chaque joueur
        grid_joueurs_blanc = QGridLayout()
        grid_joueurs_blanc.setHorizontalSpacing(0)
        grid_joueurs_blanc.setContentsMargins(0,0,0,0)
        # (boucle sur joueurs et fautes, ajoute FaultButton comme vu précédemment)
        # Même chose pour les joueurs bleus
        
        # ... reste du layout : scores, chrono, boutons de gestion...

        self.setLayout(main)
        self.refresh()

    # ... le reste de la classe (change, refresh, chrono_str)
