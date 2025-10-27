# --- Import de PyQt5 ---
# On importe le widget QPushButton depuis PyQt5 (c’est le bouton classique de Qt)
from PyQt5.QtWidgets import QPushButton


# --- Définition d’une classe personnalisée ---
# Cette classe hérite de QPushButton et permet de gérer un bouton qui change de couleur selon un "niveau de faute"
class FaultButton(QPushButton):

    # Constructeur (initialisation du bouton)
    def __init__(self, update_callback):
        # Appel du constructeur de la classe parente (QPushButton)
        super().__init__()

        # Niveau actuel de "faute" (0 = aucun, 1 = rouge, 2 = orange, 3 = noir)
        self.fault_level = 0

        # Fonction de rappel (callback) à appeler quand le niveau change
        # Cela permet de mettre à jour une autre partie de ton interface (par exemple un compteur ou une base)
        self.update_callback = update_callback

        # Définit une taille fixe du bouton (ici un petit rond de 16x16 pixels)
        self.setFixedSize(16, 16)

        # Met à jour le style visuel du bouton (couleur, bordure, forme)
        self.update_style()

        # Connecte le clic du bouton à la fonction increment_fault
        self.clicked.connect(self.increment_fault)


    # --- Fonction appelée à chaque clic ---
    def increment_fault(self):
        # À chaque clic, on augmente le niveau de faute de 1
        # et on revient à 0 après 3 (grâce au % 4)
        self.fault_level = (self.fault_level + 1) % 4

        # On met à jour le style du bouton selon le nouveau niveau
        self.update_style()

        # Si une fonction de mise à jour externe est fournie, on l'appelle
        # (cela permet à d'autres parties du programme de réagir au changement)
        if self.update_callback:
            self.update_callback(self.fault_level)


    # --- Mise à jour du style visuel du bouton ---
    def update_style(self):
        # Liste des couleurs de fond selon le niveau
        color = ["transparent", "red", "orange", "black"][self.fault_level]

        # Liste des couleurs de bordure selon le niveau
        border_color = ["gray", "red", "orange", "black"][self.fault_level]

        self.setStyleSheet(
            f"border-radius:8px;border:2px solid {border_color};background-color:{color};padding:0px;margin:0px;"
        )
