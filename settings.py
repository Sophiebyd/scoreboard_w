# On importe QFont depuis PyQt5.QtGui
# QFont permet de définir le style (nom, taille, épaisseur...) d'une police de texte
from PyQt5.QtGui import QFont


# --- Définition des polices utilisées dans l'application ---

# Police pour l'affichage du score principal (très grande et en gras)
FONT_SCORE = QFont("Arial Black", 200)

# Police pour le nom des équipes (grande et bien visible)
FONT_TEAM = QFont("Arial Black", 70)

# Police pour le texte de l'équipe pendant les temps morts (time-out)
FONT_TM = QFont("Arial", 30)

# Police pour le chronomètre principal du match
FONT_CHRONO = QFont("Arial Black", 200)

# Police pour les boutons ou les contrôles (par ex. "START", "STOP", etc.)
FONT_CONTROL = QFont("Arial", 160)

# Police pour indiquer la période du match (ex : "1er quart-temps", "2e période", etc.)
FONT_PERIODE = QFont("Arial Black", 70)

# Police pour les numéros des joueurs (plus petite mais toujours lisible)
FONT_NUM = QFont("Arial", 28)
