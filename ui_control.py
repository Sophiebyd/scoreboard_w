# Importation des modules nécessaires de PyQt5
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QGridLayout, QPushButton
from PyQt5.QtCore import Qt

# Importation des constantes de style et polices
from settings import *
# Importation du bouton personnalisé pour gérer les fautes
from fault_button import FaultButton


# Classe principale pour la fenêtre de contrôle du match
class ControlWindow(QWidget):
    def __init__(self, display):
        super().__init__()  # Appel du constructeur parent QWidget

        # Référence vers la fenêtre d’affichage principale (écran)
        self.display = display

        # Configuration de la fenêtre principale
        self.setWindowTitle("Panneau de gestion Water-Polo")
        self.setStyleSheet("background-color: #111;")  # Fond noir
        self.setGeometry(100, 100, 1600, 900)  # Taille et position

        # --- Variables de suivi du match ---
        self.scores1 = 0        # Score équipe blanche (LE MANS)
        self.scores2 = 0        # Score équipe bleue (VISITEURS)
        self.periode = 1        # Période actuelle du match
        self.chrono_mins = 8    # Minutes du chronomètre
        self.chrono_secs = 0    # Secondes du chronomètre
        self.tm1 = 0            # Temps morts équipe blanche
        self.tm2 = 0            # Temps morts équipe bleue
        self.possession = 28    # Temps de possession

        # Tableaux pour enregistrer les fautes de chaque joueur
        # 14 joueurs par équipe, avec 3 fautes possibles par joueur
        self.fautes_blancs = [[0,0,0] for _ in range(14)]
        self.fautes_bleus = [[0,0,0] for _ in range(14)]

        # Layout principal de la fenêtre (grille)
        main = QGridLayout()

        # --- TITRES DES ÉQUIPES ---
        lbl_team1 = QLabel("LE MANS")
        lbl_team1.setFont(FONT_TEAM)
        lbl_team1.setStyleSheet("color:white")  # Texte blanc

        lbl_team2 = QLabel("VISITEURS")
        lbl_team2.setFont(FONT_TEAM)
        lbl_team2.setStyleSheet("color:#53aaff")  # Texte bleu clair

        # Ajout des labels dans la grille
        main.addWidget(lbl_team1, 0, 0, 1, 2, Qt.AlignLeft)
        main.addWidget(lbl_team2, 0, 6, 1, 2, Qt.AlignRight)


        # --- TEMPS MORT ÉQUIPE BLANCHE ---
        layout_tm1 = QVBoxLayout()  # Disposition verticale

        # Texte "Temps mort"
        lbl_tm1_txt = QLabel("Temps\nmort")
        lbl_tm1_txt.setFont(FONT_TM)
        lbl_tm1_txt.setStyleSheet("color:white")

        # Label affichant le nombre de temps morts restants
        self.lbl_tm1_nb = QLabel(str(self.tm1))
        self.lbl_tm1_nb.setFont(FONT_TM)
        self.lbl_tm1_nb.setStyleSheet("color:white")

        # Boutons pour ajouter / retirer un temps mort
        btn_tm1p = QPushButton("+")
        btn_tm1m = QPushButton("-")
        btn_tm1p.clicked.connect(lambda: self.change('tm1', 1))
        btn_tm1m.clicked.connect(lambda: self.change('tm1', -1))

        # Ajout des éléments au layout vertical
        layout_tm1.addWidget(lbl_tm1_txt)
        layout_tm1.addWidget(self.lbl_tm1_nb)
        layout_tm1.addWidget(btn_tm1p)
        layout_tm1.addWidget(btn_tm1m)
        main.addLayout(layout_tm1, 0, 2)  # Ajout à la grille principale


        # --- TEMPS MORT ÉQUIPE BLEUE ---
        layout_tm2 = QVBoxLayout()
        lbl_tm2_txt = QLabel("Temps\nmort")
        lbl_tm2_txt.setFont(FONT_TM)
        lbl_tm2_txt.setStyleSheet("color:#53aaff")
        self.lbl_tm2_nb = QLabel(str(self.tm2))
        self.lbl_tm2_nb.setFont(FONT_TM)
        self.lbl_tm2_nb.setStyleSheet("color:#53aaff")
        btn_tm2p = QPushButton("+")
        btn_tm2m = QPushButton("-")
        btn_tm2p.clicked.connect(lambda: self.change('tm2', 1))
        btn_tm2m.clicked.connect(lambda: self.change('tm2', -1))
        layout_tm2.addWidget(lbl_tm2_txt)
        layout_tm2.addWidget(self.lbl_tm2_nb)
        layout_tm2.addWidget(btn_tm2p)
        layout_tm2.addWidget(btn_tm2m)
        main.addLayout(layout_tm2, 0, 5)


        # --- SCORE ÉQUIPE BLANCHE ---
        self.lbl_score1 = QLabel(str(self.scores1).zfill(2))  # Format 2 chiffres
        self.lbl_score1.setFont(FONT_SCORE)
        self.lbl_score1.setStyleSheet("color:white")

        # Boutons + et - pour modifier le score
        btn_score1p = QPushButton("+")
        btn_score1m = QPushButton("-")
        btn_score1p.clicked.connect(lambda: self.change('score1', 1))
        btn_score1m.clicked.connect(lambda: self.change('score1', -1))

        main.addWidget(self.lbl_score1, 1, 0, 2, 2, Qt.AlignCenter)
        main.addWidget(btn_score1p, 3, 0)
        main.addWidget(btn_score1m, 3, 1)


        # --- SCORE ÉQUIPE BLEUE ---
        self.lbl_score2 = QLabel(str(self.scores2).zfill(2))
        self.lbl_score2.setFont(FONT_SCORE)
        self.lbl_score2.setStyleSheet("color:#53aaff")
        btn_score2p = QPushButton("+")
        btn_score2m = QPushButton("-")
        btn_score2p.clicked.connect(lambda: self.change('score2', 1))
        btn_score2m.clicked.connect(lambda: self.change('score2', -1))
        main.addWidget(self.lbl_score2, 1, 6, 2, 2, Qt.AlignCenter)
        main.addWidget(btn_score2p, 3, 6)
        main.addWidget(btn_score2m, 3, 7)


        # --- PÉRIODE DU MATCH ---
        lbl_periode_txt = QLabel("Période")
        lbl_periode_txt.setFont(FONT_PERIODE)
        lbl_periode_txt.setStyleSheet("color:#99ff66")
        self.lbl_periode = QLabel(str(self.periode))
        self.lbl_periode.setFont(FONT_PERIODE)
        self.lbl_periode.setStyleSheet("color:#99ff66")

        btn_periodep = QPushButton("+")
        btn_periodem = QPushButton("-")
        btn_periodep.clicked.connect(lambda: self.change('periode', 1))
        btn_periodem.clicked.connect(lambda: self.change('periode', -1))

        main.addWidget(lbl_periode_txt, 0, 3, 1, 2, Qt.AlignCenter)
        main.addWidget(self.lbl_periode, 1, 3, 1, 2, Qt.AlignCenter)
        main.addWidget(btn_periodep, 2, 3)
        main.addWidget(btn_periodem, 2, 4)


        # --- CHRONOMÈTRE PRINCIPAL ---
        self.lbl_chrono = QLabel(self.chrono_str())  # Format mm:ss
        self.lbl_chrono.setFont(FONT_CHRONO)
        self.lbl_chrono.setStyleSheet("color:red")

        btn_chrono_p = QPushButton("+")  # Ajoute des secondes
        btn_chrono_m = QPushButton("-")  # Retire des secondes
        btn_chrono_p.clicked.connect(lambda: self.change('chrono', 1))
        btn_chrono_m.clicked.connect(lambda: self.change('chrono', -1))

        main.addWidget(self.lbl_chrono, 2, 2, 2, 4, Qt.AlignCenter)
        main.addWidget(btn_chrono_p, 4, 2)
        main.addWidget(btn_chrono_m, 4, 3)


        # --- POSSESSION ---
        self.lbl_control = QLabel(str(self.possession))
        self.lbl_control.setFont(FONT_CONTROL)
        self.lbl_control.setStyleSheet("color:yellow")
        btn_control_p = QPushButton("+")
        btn_control_m = QPushButton("-")
        btn_control_p.clicked.connect(lambda: self.change('control', 1))
        btn_control_m.clicked.connect(lambda: self.change('control', -1))
        main.addWidget(self.lbl_control, 6, 3, 1, 2, Qt.AlignCenter)
        main.addWidget(btn_control_p, 7, 3)
        main.addWidget(btn_control_m, 7, 4)


        # --- FAUTES JOUEURS BLANCS ---
        grid_joueurs_blanc = QGridLayout()
        grid_joueurs_blanc.setHorizontalSpacing(0)
        grid_joueurs_blanc.setContentsMargins(0,0,0,0)

        # Fonction pour créer un callback pour chaque joueur
        def make_cb_b(row, col):
            def cb(level):
                self.fautes_blancs[row][col] = level
            return cb

        # 14 joueurs répartis sur 2 colonnes
        for idx in range(7):  # Première moitié
            lbl_a = QLabel(str(idx+1))
            lbl_a.setFont(FONT_NUM)
            lbl_a.setStyleSheet("color:white")
            grid_joueurs_blanc.addWidget(lbl_a, idx, 0, Qt.AlignLeft)
            for pt in range(3):  # 3 boutons de faute
                btn = FaultButton(make_cb_b(idx, pt))
                grid_joueurs_blanc.addWidget(btn, idx, pt+1, Qt.AlignCenter)
        for idx in range(7,14):  # Seconde moitié
            lbl_b = QLabel(str(idx+1))
            lbl_b.setFont(FONT_NUM)
            lbl_b.setStyleSheet("color:white")
            grid_joueurs_blanc.addWidget(lbl_b, idx-7, 4, Qt.AlignLeft)
            for pt in range(3):
                btn = FaultButton(make_cb_b(idx, pt))
                grid_joueurs_blanc.addWidget(btn, idx-7, pt+5, Qt.AlignCenter)
        grid_joueurs_blanc.setVerticalSpacing(18)
        main.addLayout(grid_joueurs_blanc, 5, 0, 2, 4)


        # --- FAUTES JOUEURS BLEUS ---
        grid_joueurs_bleu = QGridLayout()
        grid_joueurs_bleu.setHorizontalSpacing(0)
        grid_joueurs_bleu.setContentsMargins(0,0,0,0)
        def make_cb_bl(row, col):
            def cb(level):
                self.fautes_bleus[row][col] = level
            return cb
        for idx in range(7):
            lbl_a = QLabel(str(idx+1))
            lbl_a.setFont(FONT_NUM)
            lbl_a.setStyleSheet("color:#53aaff")
            grid_joueurs_bleu.addWidget(lbl_a, idx, 0, Qt.AlignLeft)
            for pt in range(3):
                btn = FaultButton(make_cb_bl(idx, pt))
                grid_joueurs_bleu.addWidget(btn, idx, pt+1, Qt.AlignCenter)
        for idx in range(7,14):
            lbl_b = QLabel(str(idx+1))
            lbl_b.setFont(FONT_NUM)
            lbl_b.setStyleSheet("color:#53aaff")
            grid_joueurs_bleu.addWidget(lbl_b, idx-7, 4, Qt.AlignLeft)
            for pt in range(3):
                btn = FaultButton(make_cb_bl(idx, pt))
                grid_joueurs_bleu.addWidget(btn, idx-7, pt+5, Qt.AlignCenter)
        grid_joueurs_bleu.setVerticalSpacing(18)
        main.addLayout(grid_joueurs_bleu, 5, 5, 2, 4)


        # Application du layout principal et mise à jour de l’affichage
        self.setLayout(main)
        self.refresh()


    # --- Retourne le chrono sous forme "mm:ss" ---
    def chrono_str(self):
        return f"{self.chrono_mins:02d}:{self.chrono_secs:02d}"


    # --- Fonction pour gérer les modifications (scores, chrono, etc.) ---
    def change(self, field, val):
        if field == 'score1':
            self.scores1 = max(0, self.scores1 + val)
        elif field == 'score2':
            self.scores2 = max(0, self.scores2 + val)
        elif field == 'periode':
            self.periode = max(1, min(4, self.periode + val))
        elif field == 'tm1':
            self.tm1 = max(0, self.tm1 + val)
        elif field == 'tm2':
            self.tm2 = max(0, self.tm2 + val)
        elif field == 'chrono':
            # Ajustement du chronomètre (minutes et secondes)
            m, s = self.chrono_mins, self.chrono_secs
            s += val
            if s >= 60:
                m += 1
                s = 0
            elif s < 0:
                if m > 0:
                    m -= 1
                    s = 59
                else:
                    s = 0
            self.chrono_mins = max(0, m)
            self.chrono_secs = max(0, s)
        elif field == 'control':
            self.possession = max(0, self.possession + val)

        self.refresh()  # Mise à jour après chaque changement


    # --- Mise à jour complète de l’affichage ---
    def refresh(self):
        # Actualise toutes les étiquettes avec les nouvelles valeurs
        self.lbl_score1.setText(str(self.scores1).zfill(2))
        self.lbl_score2.setText(str(self.scores2).zfill(2))
        self.lbl_periode.setText(str(self.periode))
        self.lbl_tm1_nb.setText(str(self.tm1))
        self.lbl_tm2_nb.setText(str(self.tm2))
        self.lbl_chrono.setText(self.chrono_str())
        self.lbl_control.setText(str(self.possession))

        # Envoie les nouvelles données à la fenêtre d’affichage principale
        self.display.update_affichage(
            self.scores1, self.scores2, self.periode,
            self.tm1, self.tm2, self.chrono_mins, self.chrono_secs, self.possession
        )
