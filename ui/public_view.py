from PyQt5.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from components.score import ScoreWidget
from components.period import PeriodeWidget
from components.chrono import ChronoWidget
from components.faults import FaultsWidget
from components.exclusion import ExclusionWidget
from components.time_possession import TimePossessionWidget

class PublicView(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: black;")
        grid = QGridLayout()
        grid.setContentsMargins(16, 16, 16, 16)
        grid.setSpacing(10)

        # Titres équipes
        # ... (peut se faire avec QLabel stylisé)

        # Score principal gauche/droite
        score_home = ScoreWidget()
        score_home.setStyleSheet("color: white;")
        grid.addWidget(score_home, 1, 0, 2, 1, Qt.AlignLeft)

        score_away = ScoreWidget()
        score_away.setStyleSheet("color: #59a7fc;")
        grid.addWidget(score_away, 1, 4, 2, 1, Qt.AlignRight)

        # Période
        periode = PeriodeWidget()
        grid.addWidget(periode, 0, 2, 1, 2, Qt.AlignCenter)

        # Chronomètre central gros
        chrono = ChronoWidget()
        grid.addWidget(chrono, 2, 1, 1, 3, Qt.AlignCenter)

        # Temps de possession
        possession = TimePossessionWidget()
        grid.addWidget(possession, 3, 2, 1, 2, Qt.AlignCenter)

        # Widgets de fautes
        faults_g = FaultsWidget()  # Joueurs gauche/équipe 1
        grid.addWidget(faults_g, 4, 0, 1, 2, Qt.AlignLeft)
        faults_d = FaultsWidget()  # Joueurs droite/équipe 2 (tu peux dupliquer ou adapter si besoin)
        grid.addWidget(faults_d, 4, 4, 1, 2, Qt.AlignRight)

        # Exclusion (peut être placé sous le chrono ou à côté, selon logique terrain)
        exclusion = ExclusionWidget()
        grid.addWidget(exclusion, 4, 2, 1, 2, Qt.AlignCenter)

        self.setLayout(grid)
        self.setWindowTitle("Tableau Spectateur - Scoreboard Public View")

# Lancement direct pour test
if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)
    window = PublicView()
    window.show()
    sys.exit(app.exec_())
