from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QFont

class TimePossessionWidget(QWidget):
    def __init__(self):
        super().__init__()
        # Temps de la possession (par défaut ici 12 secondes, adapter pour 30 ou 20 selon règles)
        self.sec = 28
        # Dixième de seconde (utilisé uniquement sous les 10s)
        self.dix = 0
        # Mode d'affichage : False = secondes, True = dixièmes
        self.mode_dixieme = False

        # Création du label pour l'affichage du temps restant
        self.lbl = QLabel(f"{self.sec:02d}") # Initialisé au temps de possession
        layout = QHBoxLayout(self)
        layout.addWidget(self.lbl)

        # Style visuel : fond noir et chiffres jaune
        self.setStyleSheet("background-color: black;")
        self.lbl.setStyleSheet("color:#ffc000; background-color: black;")
        font = QFont("Arial Black", 72) # Police épaisse, très lisible
        self.lbl.setFont(font)

        # Timer PyQt : sert à décrémenter le temps
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.tick)
        self.timer.start(1000) # On commence par des ticks toutes les 1s

    def tick(self):
        # -------------------
        # MODE SECONDES (>9s)
        # -------------------
        if not self.mode_dixieme:
            self.sec -= 1 # Enlève 1 seconde à chaque tick
            # Si on atteint pile 9 secondes, il faut passer au mode dixièmes
            if self.sec == 9:
                self.mode_dixieme = True        # On note qu'on change de mode
                self.dix = 9                    # On commence direct par 9 dixièmes ("9.9")
                self.lbl.setText(f"{self.sec}.{self.dix}") # Affichage typique "9.9"
                self.timer.stop()               # Stoppe le timer
                self.timer.setInterval(100)     # Reconfigure le timer pour déclencher toutes les 0,1s (100ms)
                self.timer.start()              # Relance le timer
            else:
                self.lbl.setText(f"{self.sec:02d}") # Reste en format "ss" normal

        # -------------------
        # MODE DIXIEMES (<10s)
        # -------------------
        else:
            # Si on vient de finir une dizaine de dixièmes
            if self.dix == 0:
                if self.sec == 0:
                    # Timer fini, on affiche 0.0 et stoppe tout
                    self.timer.stop()
                    self.lbl.setText("0.0")
                    return
                else:
                    # On passe à la seconde suivante
                    self.sec -= 1
                    self.dix = 9
            else:
                # On enlève un dixième à chaque tick de 100ms
                self.dix -= 1
            # Affichage au format "s.d"
            self.lbl.setText(f"{self.sec}.{self.dix}")
