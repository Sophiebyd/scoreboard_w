# On importe QPushButton depuis PyQt5 pour créer un bouton cliquable
from PyQt5.QtWidgets import QPushButton


# --- Classe personnalisée : FaultButton ---
# Ce bouton change de couleur à chaque clic, pour représenter un "niveau de faute"
class FaultButton(QPushButton):
    def __init__(self, update_callback):
        # Appel du constructeur parent de QPushButton
        super().__init__()

        # Niveau de faute (0 à 3)
        # 0 = aucun / 1 = rouge / 2 = orange / 3 = noir
        self.fault_level = 0

        # Fonction de rappel (callback) passée par le parent
        # Elle sera appelée à chaque fois que le niveau change
        self.update_callback = update_callback

        # Taille fixe du bouton : petit rond
        self.setFixedSize(16, 16)  # taille en pixels

        # On applique le style initial selon le niveau de faute
        self.update_style()

        # Quand le bouton est cliqué → appelle la fonction increment_fault()
        self.clicked.connect(self.increment_fault)


    # --- Fonction appelée à chaque clic sur le bouton ---
    def increment_fault(self):
        # Incrémente le niveau de faute (de 0 à 3 en boucle)
        self.fault_level = (self.fault_level + 1) % 4

        # Met à jour la couleur du bouton selon le niveau
        self.update_style()

        # Si une fonction de callback a été définie → on l'appelle
        # Cela permet à une autre partie du programme d’être avertie du changement
        if self.update_callback:
            self.update_callback(self.fault_level)


    # --- Met à jour l'apparence du bouton ---
    def update_style(self):
        # Liste des couleurs de fond selon le niveau
        color = ["transparent", "red", "orange", "black"][self.fault_level]
        # Liste des couleurs de bordure selon le niveau
        border_color = ["gray", "red", "orange", "black"][self.fault_level]

        # On applique un style CSS (Qt StyleSheet)
        # border-radius: 8px → rend le bouton rond
        # border: 2px solid ... → bordure colorée
        # background-color → couleur du fond selon le niveau
        # padding et margin à 0 pour coller les boutons les uns aux autres
        self.setStyleSheet(
            f"border-radius:8px;"
            f"border:2px solid {border_color};"
            f"background-color:{color};"
            f"padding:0px;margin:0px;"
        )
