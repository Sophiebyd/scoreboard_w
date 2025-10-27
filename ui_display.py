# Importation des modules nécessaires de PyQt5
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QGridLayout
from PyQt5.QtCore import Qt

# Importation des constantes de style (polices, tailles, couleurs, etc.)
from settings import *


# Classe principale pour la fenêtre d'affichage du score et des informations du match
class DisplayWindow(QWidget):
    def __init__(self):
        super().__init__()  # Appel du constructeur de QWidget

        # Configuration de la fenêtre
        self.setWindowTitle("Affichage Water-Polo")       # Titre de la fenêtre
        self.setStyleSheet("background-color: black;")    # Fond noir
        self.setGeometry(300, 100, 1600, 900)             # Taille et position de la fenêtre

        # Création du layout principal (grille)
        main = QGridLayout()

        # --- NOMS DES ÉQUIPES ---
        self.lbl_team1 = QLabel("LE MANS")  # Équipe blanche (locale)
        self.lbl_team1.setFont(FONT_TEAM)
        self.lbl_team1.setStyleSheet("color:white")  # Texte blanc

        self.lbl_team2 = QLabel("VISITEURS")  # Équipe bleue (adverse)
        self.lbl_team2.setFont(FONT_TEAM)
        self.lbl_team2.setStyleSheet("color:#53aaff")  # Texte bleu clair

        # Ajout des labels d'équipes à la grille
        main.addWidget(self.lbl_team1, 0, 0, 1, 2, Qt.AlignLeft)
        main.addWidget(self.lbl_team2, 0, 6, 1, 2, Qt.AlignRight)


        # --- TEMPS MORT ÉQUIPE BLANCHE ---
        layout_tm1 = QVBoxLayout()  # Disposition verticale
        self.lbl_tm1_txt = QLabel("Temps\nmort")  # Texte "Temps mort"
        self.lbl_tm1_txt.setFont(FONT_TM)
        self.lbl_tm1_txt.setStyleSheet("color:white")

        self.lbl_tm1_nb = QLabel("0")  # Nombre de temps morts
        self.lbl_tm1_nb.setFont(FONT_TM)
        self.lbl_tm1_nb.setStyleSheet("color:white")

        # Centrage du texte
        self.lbl_tm1_txt.setAlignment(Qt.AlignCenter)
        self.lbl_tm1_nb.setAlignment(Qt.AlignCenter)

        # Ajout des éléments au layout
        layout_tm1.addWidget(self.lbl_tm1_txt)
        layout_tm1.addWidget(self.lbl_tm1_nb)
        main.addLayout(layout_tm1, 0, 2)  # Placement dans la grille principale


        # --- TEMPS MORT ÉQUIPE BLEUE ---
        layout_tm2 = QVBoxLayout()
        self.lbl_tm2_txt = QLabel("Temps\nmort")
        self.lbl_tm2_txt.setFont(FONT_TM)
        self.lbl_tm2_txt.setStyleSheet("color:#53aaff")

        self.lbl_tm2_nb = QLabel("0")
        self.lbl_tm2_nb.setFont(FONT_TM)
        self.lbl_tm2_nb.setStyleSheet("color:#53aaff")

        self.lbl_tm2_txt.setAlignment(Qt.AlignCenter)
        self.lbl_tm2_nb.setAlignment(Qt.AlignCenter)

        layout_tm2.addWidget(self.lbl_tm2_txt)
        layout_tm2.addWidget(self.lbl_tm2_nb)
        main.addLayout(layout_tm2, 0, 5)


        # --- SCORES DES DEUX ÉQUIPES ---
        self.lbl_score1 = QLabel("00")  # Score équipe blanche
        self.lbl_score1.setFont(FONT_SCORE)
        self.lbl_score1.setStyleSheet("color:white")

        self.lbl_score2 = QLabel("00")  # Score équipe bleue
        self.lbl_score2.setFont(FONT_SCORE)
        self.lbl_score2.setStyleSheet("color:#53aaff")

        # Placement des scores dans la grille
        main.addWidget(self.lbl_score1, 1, 0, 2, 2, Qt.AlignCenter)
        main.addWidget(self.lbl_score2, 1, 6, 2, 2, Qt.AlignCenter)


        # --- PÉRIODE DU MATCH ---
        self.lbl_periode_txt = QLabel("Période")
        self.lbl_periode_txt.setFont(FONT_PERIODE)
        self.lbl_periode_txt.setStyleSheet("color:#99ff66")

        self.lbl_periode = QLabel("1")  # Période actuelle
        self.lbl_periode.setFont(FONT_PERIODE)
        self.lbl_periode.setStyleSheet("color:#99ff66")

        main.addWidget(self.lbl_periode_txt, 0, 3, 1, 2, Qt.AlignCenter)
        main.addWidget(self.lbl_periode, 1, 3, 1, 2, Qt.AlignCenter)


        # --- CHRONOMÈTRE PRINCIPAL ---
        self.lbl_chrono = QLabel("08:00")  # Chrono initial
        self.lbl_chrono.setFont(FONT_CHRONO)
        self.lbl_chrono.setStyleSheet("color:red")

        # Ajout du chrono au centre
        main.addWidget(self.lbl_chrono, 2, 2, 2, 4, Qt.AlignCenter)


        # --- TEMPS DE POSSESSION ---
        self.lbl_control = QLabel("28")  # 28 secondes par défaut
        self.lbl_control.setFont(FONT_CONTROL)
        self.lbl_control.setStyleSheet("color:yellow")
        main.addWidget(self.lbl_control, 6, 3, 1, 2, Qt.AlignCenter)


        # --- FAUTES JOUEURS BLANCS ---
        grid_joueurs_blanc = QGridLayout()
        grid_joueurs_blanc.setHorizontalSpacing(0)
        grid_joueurs_blanc.setContentsMargins(0, 0, 0, 0)

        # Création des lignes pour chaque joueur (14 au total)
        for idx in range(7):
            lbl_a = QLabel(str(idx+1))  # Numéro du joueur
            lbl_a.setFont(FONT_NUM)
            lbl_a.setStyleSheet("color:white")
            grid_joueurs_blanc.addWidget(lbl_a, idx, 0, Qt.AlignLeft)

            # Ajout des 3 ronds représentant les fautes
            for pt in range(3):
                rond = QLabel("O")
                rond.setFont(FONT_NUM)
                rond.setStyleSheet("color:white")
                grid_joueurs_blanc.addWidget(rond, idx, pt+1, Qt.AlignCenter)

        for idx in range(7,14):
            lbl_b = QLabel(str(idx+1))
            lbl_b.setFont(FONT_NUM)
            lbl_b.setStyleSheet("color:white")
            grid_joueurs_blanc.addWidget(lbl_b, idx-7, 4, Qt.AlignLeft)

            for pt in range(3):
                rond = QLabel("O")
                rond.setFont(FONT_NUM)
                rond.setStyleSheet("color:white")
                grid_joueurs_blanc.addWidget(rond, idx-7, pt+5, Qt.AlignCenter)

        grid_joueurs_blanc.setVerticalSpacing(18)
        main.addLayout(grid_joueurs_blanc, 5, 0, 2, 4)


        # --- FAUTES JOUEURS BLEUS ---
        grid_joueurs_bleu = QGridLayout()
        grid_joueurs_bleu.setHorizontalSpacing(0)
        grid_joueurs_bleu.setContentsMargins(0, 0, 0, 0)

        for idx in range(7):
            lbl_a = QLabel(str(idx+1))
            lbl_a.setFont(FONT_NUM)
            lbl_a.setStyleSheet("color:#53aaff")
            grid_joueurs_bleu.addWidget(lbl_a, idx, 0, Qt.AlignLeft)

            for pt in range(3):
                rond = QLabel("O")
                rond.setFont(FONT_NUM)
                rond.setStyleSheet("color:#53aaff")
                grid_joueurs_bleu.addWidget(rond, idx, pt+1, Qt.AlignCenter)

        for idx in range(7,14):
            lbl_b = QLabel(str(idx+1))
            lbl_b.setFont(FONT_NUM)
            lbl_b.setStyleSheet("color:#53aaff")
            grid_joueurs_bleu.addWidget(lbl_b, idx-7, 4, Qt.AlignLeft)

            for pt in range(3):
                rond = QLabel("O")
                rond.setFont(FONT_NUM)
                rond.setStyleSheet("color:#53aaff")
                grid_joueurs_bleu.addWidget(rond, idx-7, pt+5, Qt.AlignCenter)

        grid_joueurs_bleu.setVerticalSpacing(18)
        main.addLayout(grid_joueurs_bleu, 5, 5, 2, 4)


        # Application du layout principal à la fenêtre
        self.setLayout(main)


    # --- MISE À JOUR DES DONNÉES AFFICHÉES ---
    # Cette méthode est appelée depuis la fenêtre de contrôle
    def update_affichage(self, scores1, scores2, periode, tm1, tm2, chrono_mins, chrono_secs, possession):
        # Mise à jour des scores
        self.lbl_score1.setText(str(scores1).zfill(2))
        self.lbl_score2.setText(str(scores2).zfill(2))

        # Mise à jour de la période
        self.lbl_periode.setText(str(periode))

        # Mise à jour des temps morts
        self.lbl_tm1_nb.setText(str(tm1))
        self.lbl_tm2_nb.setText(str(tm2))

        # Mise à jour du chronomètre au format mm:ss
        self.lbl_chrono.setText(f"{chrono_mins:02d}:{chrono_secs:02d}")

        # Mise à jour du temps de possession
        self.lbl_control.setText(str(possession))
