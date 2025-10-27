import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

FONT_SCORE = QFont("Arial Black", 200)
FONT_TEAM = QFont("Arial Black", 70)
FONT_TM = QFont("Arial", 30)
FONT_CHRONO = QFont("Arial Black", 200)
FONT_CONTROL = QFont("Arial",160)
FONT_PERIODE = QFont("Arial Black", 70)
FONT_NUM = QFont("Arial", 28)

class FaultButton(QPushButton):
    def __init__(self, update_callback):
        super().__init__()
        self.fault_level = 0
        self.update_callback = update_callback
        self.setFixedSize(24, 24)
        self.update_style()
        self.clicked.connect(self.increment_fault)

    def increment_fault(self):
        self.fault_level = (self.fault_level + 1) % 4
        self.update_style()
        if self.update_callback:
            self.update_callback(self.fault_level)

    def update_style(self):
        color = ["transparent", "red", "orange", "black"][self.fault_level]
        border_color = ["gray", "red", "orange", "black"][self.fault_level]
        self.setStyleSheet(
            f"border-radius:12px; border:2px solid {border_color}; background-color: {color};"
        )


class DisplayWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Affichage Water-Polo")
        self.setStyleSheet("background-color: black;")
        self.setGeometry(300, 100, 1600, 900)

        self.main = QGridLayout()

        # Entêtes noms équipes
        self.lbl_team1 = QLabel("LE MANS")
        self.lbl_team1.setFont(FONT_TEAM)
        self.lbl_team1.setStyleSheet("color:white")
        self.lbl_team2 = QLabel("VISITEURS")
        self.lbl_team2.setFont(FONT_TEAM)
        self.lbl_team2.setStyleSheet("color:#53aaff")
        self.main.addWidget(self.lbl_team1, 0, 0, 1, 2, Qt.AlignLeft)
        self.main.addWidget(self.lbl_team2, 0, 6, 1, 2, Qt.AlignRight)

        # Bloc "Temps mort" + nombre pour l'équipe blanche
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
        self.main.addLayout(layout_tm1, 0, 2)

        # Bloc "Temps mort" + nombre pour l'équipe bleue
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
        self.main.addLayout(layout_tm2, 0, 5)

        # Scores
        self.lbl_score1 = QLabel("00")
        self.lbl_score1.setFont(FONT_SCORE)
        self.lbl_score1.setStyleSheet("color:white")
        self.lbl_score2 = QLabel("00")
        self.lbl_score2.setFont(FONT_SCORE)
        self.lbl_score2.setStyleSheet("color:#53aaff")
        self.main.addWidget(self.lbl_score1, 1, 0, 2, 2, Qt.AlignCenter)
        self.main.addWidget(self.lbl_score2, 1, 6, 2, 2, Qt.AlignCenter)

        # Période
        self.lbl_periode_txt = QLabel("Période")
        self.lbl_periode_txt.setFont(FONT_PERIODE)
        self.lbl_periode_txt.setStyleSheet("color:#99ff66")
        self.lbl_periode = QLabel("1")
        self.lbl_periode.setFont(FONT_PERIODE)
        self.lbl_periode.setStyleSheet("color:#99ff66")
        self.main.addWidget(self.lbl_periode_txt, 0, 3, 1, 2, Qt.AlignCenter)
        self.main.addWidget(self.lbl_periode, 1, 3, 1, 2, Qt.AlignCenter)

        # Chrono central
        self.lbl_chrono = QLabel("08:00")
        self.lbl_chrono.setFont(FONT_CHRONO)
        self.lbl_chrono.setStyleSheet("color:red")
        self.main.addWidget(self.lbl_chrono, 2, 2, 2, 4, Qt.AlignCenter)

        # Temps de possession
        self.lbl_control = QLabel("28")
        self.lbl_control.setFont(FONT_CONTROL)
        self.lbl_control.setStyleSheet("color:yellow")
        self.main.addWidget(self.lbl_control, 6, 3, 1, 2, Qt.AlignCenter)

        # Bloc joueurs blancs avec ronds "fautes"
        grid_joueurs_blanc = QGridLayout()
        grid_joueurs_blanc.setHorizontalSpacing(2)
        for idx in range(7):
            lbl_a = QLabel(str(idx+1))
            lbl_a.setFont(FONT_NUM)
            lbl_a.setStyleSheet("color:white")
            grid_joueurs_blanc.addWidget(lbl_a, idx, 0, Qt.AlignLeft)
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
        self.main.addLayout(grid_joueurs_blanc, 5, 0, 2, 4)

        # Bloc joueurs bleus avec ronds "fautes"
        grid_joueurs_bleu = QGridLayout()
        grid_joueurs_bleu.setHorizontalSpacing(2)

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
        self.main.addLayout(grid_joueurs_bleu, 5, 5, 2, 4)

        self.setLayout(self.main)

    def update_affichage(self, scores1, scores2, periode, tm1, tm2, chrono_mins, chrono_secs, possession):
        self.lbl_score1.setText(str(scores1).zfill(2))
        self.lbl_score2.setText(str(scores2).zfill(2))
        self.lbl_periode.setText(str(periode))
        self.lbl_tm1_nb.setText(str(tm1))
        self.lbl_tm2_nb.setText(str(tm2))
        self.lbl_chrono.setText(f"{chrono_mins:02d}:{chrono_secs:02d}")
        self.lbl_control.setText(str(possession))

class ControlWindow(QWidget):
    def __init__(self, display):
        super().__init__()
        self.display = display
        self.setWindowTitle("Panneau de gestion Water-Polo")
        self.setStyleSheet("background-color: #111;")
        self.setGeometry(100, 100, 1600, 900)
        self.scores1 = 0
        self.scores2 = 0
        self.periode = 1
        self.chrono_mins = 8
        self.chrono_secs = 0
        self.tm1 = 0
        self.tm2 = 0
        self.possession = 28
        self.fautes_blancs = [[0,0,0] for _ in range(14)]
        self.fautes_bleus = [[0,0,0] for _ in range(14)]

        main = QGridLayout()

        lbl_team1 = QLabel("LE MANS")
        lbl_team1.setFont(FONT_TEAM)
        lbl_team1.setStyleSheet("color:white")
        lbl_team2 = QLabel("VISITEURS")
        lbl_team2.setFont(FONT_TEAM)
        lbl_team2.setStyleSheet("color:#53aaff")
        main.addWidget(lbl_team1, 0, 0, 1, 2, Qt.AlignLeft)
        main.addWidget(lbl_team2, 0, 6, 1, 2, Qt.AlignRight)

        # Bloc "Temps mort" + nombre + boutons équipe blanche
        layout_tm1 = QVBoxLayout()
        lbl_tm1_txt = QLabel("Temps\nmort")
        lbl_tm1_txt.setFont(FONT_TM)
        lbl_tm1_txt.setStyleSheet("color:white")
        self.lbl_tm1_nb = QLabel(str(self.tm1))
        self.lbl_tm1_nb.setFont(FONT_TM)
        self.lbl_tm1_nb.setStyleSheet("color:white")
        btn_tm1p = QPushButton("+")
        btn_tm1m = QPushButton("-")
        btn_tm1p.clicked.connect(lambda: self.change('tm1', 1))
        btn_tm1m.clicked.connect(lambda: self.change('tm1', -1))
        layout_tm1.addWidget(lbl_tm1_txt)
        layout_tm1.addWidget(self.lbl_tm1_nb)
        layout_tm1.addWidget(btn_tm1p)
        layout_tm1.addWidget(btn_tm1m)
        main.addLayout(layout_tm1, 0, 2)

        # Bloc "Temps mort" + nombre + boutons équipe bleue
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

        # Scores + boutons
        self.lbl_score1 = QLabel(str(self.scores1).zfill(2))
        self.lbl_score1.setFont(FONT_SCORE)
        self.lbl_score1.setStyleSheet("color:white")
        btn_score1p = QPushButton("+")
        btn_score1m = QPushButton("-")
        btn_score1p.clicked.connect(lambda: self.change('score1', 1))
        btn_score1m.clicked.connect(lambda: self.change('score1', -1))
        main.addWidget(self.lbl_score1, 1, 0, 2, 2, Qt.AlignCenter)
        main.addWidget(btn_score1p, 3, 0)
        main.addWidget(btn_score1m, 3, 1)

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

        # Période + boutons
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

        # Chrono + boutons
        self.lbl_chrono = QLabel(self.chrono_str())
        self.lbl_chrono.setFont(FONT_CHRONO)
        self.lbl_chrono.setStyleSheet("color:red")
        btn_chrono_p = QPushButton("+")
        btn_chrono_m = QPushButton("-")
        btn_chrono_p.clicked.connect(lambda: self.change('chrono', 1))
        btn_chrono_m.clicked.connect(lambda: self.change('chrono', -1))
        main.addWidget(self.lbl_chrono, 2, 2, 2, 4, Qt.AlignCenter)
        main.addWidget(btn_chrono_p, 4, 2)
        main.addWidget(btn_chrono_m, 4, 3)

        # Possession + boutons
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

        # Bloc joueurs blancs avec FaultButton
        grid_joueurs_blanc = QGridLayout()
        def make_cb_b(row, col):
            def cb(level):
                self.fautes_blancs[row][col] = level
            return cb
        for idx in range(7):
            lbl_a = QLabel(str(idx+1))
            lbl_a.setFont(FONT_NUM)
            lbl_a.setStyleSheet("color:white")
            grid_joueurs_blanc.addWidget(lbl_a, idx, 0, Qt.AlignLeft)
            for pt in range(3):
                btn = FaultButton(make_cb_b(idx, pt))
                grid_joueurs_blanc.addWidget(btn, idx, pt+1, Qt.AlignCenter)
        for idx in range(7,14):
            lbl_b = QLabel(str(idx+1))
            lbl_b.setFont(FONT_NUM)
            lbl_b.setStyleSheet("color:white")
            grid_joueurs_blanc.addWidget(lbl_b, idx-7, 4, Qt.AlignLeft)
            for pt in range(3):
                btn = FaultButton(make_cb_b(idx, pt))
                grid_joueurs_blanc.addWidget(btn, idx-7, pt+5, Qt.AlignCenter)
        grid_joueurs_blanc.setVerticalSpacing(18)
        main.addLayout(grid_joueurs_blanc, 5, 0, 2, 4)

        # Bloc joueurs bleus avec FaultButton
        grid_joueurs_bleu = QGridLayout()
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

        self.setLayout(main)
        self.refresh()

    def chrono_str(self):
        return f"{self.chrono_mins:02d}:{self.chrono_secs:02d}"

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
        self.refresh()

    def refresh(self):
        self.lbl_score1.setText(str(self.scores1).zfill(2))
        self.lbl_score2.setText(str(self.scores2).zfill(2))
        self.lbl_periode.setText(str(self.periode))
        self.lbl_tm1_nb.setText(str(self.tm1))
        self.lbl_tm2_nb.setText(str(self.tm2))
        self.lbl_chrono.setText(self.chrono_str())
        self.lbl_control.setText(str(self.possession))
        self.display.update_affichage(
            self.scores1, self.scores2, self.periode,
            self.tm1, self.tm2, self.chrono_mins, self.chrono_secs, self.possession
        )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    display = DisplayWindow()
    control = ControlWindow(display)
    display.show()
    control.show()

    sys.exit(app.exec_())
