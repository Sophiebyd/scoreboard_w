import sys
from PyQt5.QtWidgets import QApplication
#from components.chrono import ChronoWidget
#from components.time_possession import TimePossessionWidget
#from components.faults import FaultsWidget
from components.score import ScoreWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #chrono = ChronoWidget()
    #chrono.show()
    #tp = TimePossessionWidget()
    #tp.show()
    #F = FaultsWidget()
    #F.show()
    S = ScoreWidget()
    S.show()
    sys.exit(app.exec_())
