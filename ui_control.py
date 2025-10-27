from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QGridLayout, QPushButton
from PyQt5.QtCore import Qt
from settings import *
from fault_button import FaultButton

class ControlWindow(QWidget):
    def __init__(self, display):
        super().__init__()
        self.display = display
        self.setWindowTitle("Panneau de gestion Water-Polo")
        self.setStyleSheet("background-color: #111;")
        self.setGeometry(100, 100, 1600, 900)

        # Variables
        self.scores1 = 0
        self.scores2 = 0
        self.periode = 1
        self.chrono_mins = 8
        self.chrono_secs = 0
        self.tm1 = 0
        self.tm2 = 0
        self.possession = 28

        main = QGridLayout()

        # Nom des équipes
        lbl_team1 = QLabel("LE MANS")
        lbl_team1.setFont(FONT_TEAM)
        lbl_team1.setStyleSheet("color:white")
        lbl_team2 = QLabel("VISITEURS")
        lbl_team2.setFont(FONT_TEAM)
        lbl_team2.setStyleSheet("color:#53aaff")
        main.addWidget(lbl_team1, 0, 0, 1, 2, Qt.AlignLeft)
        main.addWidget(lbl_team2, 0, 6, 1, 2, Qt.AlignRight)

        # Temps morts équipe 1
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

        # Temps morts équipe 2
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

        self.setLayout(main)

    def change(self, attr, val):
        setattr(self, attr, getattr(self, attr) + val)
        if attr == 'tm1':
            self.lbl_tm1_nb.setText(str(self.tm1))
        elif attr == 'tm2':
            self.lbl_tm2_nb.setText(str(self.tm2))
        self.display.update_affichage(
            self.scores1, self.scores2, self.periode,
            self.tm1, self.tm2, self.chrono_mins, self.chrono_secs, self.possession
        )
