from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QGridLayout
from PyQt5.QtCore import Qt

class PublicView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Affichage Water-Polo")
        self.setStyleSheet("background-color: black;")
        self.setGeometry(300, 100, 1600, 900)
        main = QGridLayout()

        # Noms des équipes
        self.lbl_team1 = QLabel("LE MANS")
        self.lbl_team1.setFont(FONT_TEAM)
        self.lbl_team1.setStyleSheet("color:white")
        self.lbl_team2 = QLabel("VISITEURS")
        self.lbl_team2.setFont(FONT_TEAM)
        self.lbl_team2.setStyleSheet("color:#53aaff")
        main.addWidget(self.lbl_team1, 0, 0, 1, 2, Qt.AlignLeft)
        main.addWidget(self.lbl_team2, 0, 6, 1, 2, Qt.AlignRight)

        # Temps mort équipe 1
        layout_tm1 = QVBoxLayout()
        self.lbl_tm1_txt = QLabel("Temps\nmort")
        self.lbl_tm1_txt.setFont(FONT_TM)
        self.lbl_tm1_txt.setStyleSheet("color:white")
        self.lbl_tm1_nb = QLabel("0")
        self.lbl_tm1_nb.setFont(FONT_TM)
        self.lbl_tm1_nb.setStyleSheet("color:white")
        self.lbl_tm1_txt.setAlignment(Qt.AlignCenter)
        self.lbl_tm1_nb.setAlignment(Qt.AlignCenter)
        layout_tm1.addWidget(self.lbl_tm1_txt)
        layout_tm1.addWidget(self.lbl_tm1_nb)
        main.addLayout(layout_tm1, 0, 2)

        # Temps mort équipe 2
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

        # Scores
        self.lbl_score1 = QLabel("00")
        self.lbl_score1.setFont(FONT_SCORE)
        self.lbl_score1.setStyleSheet("color:white")
        self.lbl_score2 = QLabel("00")
        self.lbl_score2.setFont(FONT_SCORE)
        self.lbl_score2.setStyleSheet("color:#53aaff")
        main.addWidget(self.lbl_score1, 1, 0, 2, 2, Qt.AlignCenter)
        main.addWidget(self.lbl_score2, 1, 6, 2, 2, Qt.AlignCenter)

        # Période
        self.lbl_periode_txt = QLabel("Période")
        self.lbl_periode_txt.setFont(FONT_PERIODE)
        self.lbl_periode_txt.setStyleSheet("color:#99ff66")
        self.lbl_periode = QLabel("1")
        self.lbl_periode.setFont(FONT_PERIODE)
        self.lbl_periode.setStyleSheet("color:#99ff66")
        main.addWidget(self.lbl_periode_txt, 0, 3, 1, 2, Qt.AlignCenter)
        main.addWidget(self.lbl_periode, 1, 3, 1, 2, Qt.AlignCenter)

        # Chrono
        self.lbl_chrono = QLabel("08:00")
        self.lbl_chrono.setFont(FONT_CHRONO)
        self.lbl_chrono.setStyleSheet("color:red")
        main.addWidget(self.lbl_chrono, 2, 2, 2, 4, Qt.AlignCenter)

        # Possession
        self.lbl_control = QLabel("28")
        self.lbl_control.setFont(FONT_CONTROL)
        self.lbl_control.setStyleSheet("color:yellow")
        main.addWidget(self.lbl_control, 6, 3, 1, 2, Qt.AlignCenter)

        self.setLayout(main)

    def update_affichage(self, scores1, scores2, periode, tm1, tm2, chrono_mins, chrono_secs, possession):
        self.lbl_score1.setText(str(scores1).zfill(2))
        self.lbl_score2.setText(str(scores2).zfill(2))
        self.lbl_periode.setText(str(periode))
        self.lbl_tm1_nb.setText(str(tm1))
        self.lbl_tm2_nb.setText(str(tm2))
        self.lbl_chrono.setText(f"{chrono_mins:02d}:{chrono_secs:02d}")
        self.lbl_control.setText(str(possession))
