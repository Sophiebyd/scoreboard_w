from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QSpacerItem, QSizePolicy
from tkinter import Canvas
import ttkbootstrap as ttk

class FaultsWidget(QWidget):
    def __init__(self):
        super().__init__()
        font_num = QFont("Arial", 20)
        font_round = QFont("Arial", 22, QFont.Bold)

        grid = QGridLayout()
        grid.setVerticalSpacing(10)
        grid.setHorizontalSpacing(5)
        grid.setContentsMargins(0,0,0,0)

        for idx in range(14):
            # Label du joueur (numéro)
            lb_joueur = QLabel(str(idx+1))
            lb_joueur.setFont(font_num)
            lb_joueur.setStyleSheet("color:blue;")
            if idx < 7:
                row, col = idx, 0
            else:
                row, col = idx-7, 4

            grid.addWidget(lb_joueur, row, col)

            # Les trois ronds de faute
            for f in range(3):
                rond = Canvas(self, width=26, height=26, bg="black", highlightthickness=0)
                rond.create_oval(2, 2, 24, 24, outline="blue", width=3)
                rond.grid(row=row, column=col+f+1, padx=2, pady=3)
                rond.setFont(font_round)
                rond.setStyleSheet("color:blue;")
                grid.addWidget(rond, row, col+f+1)

        self.setLayout(grid)
