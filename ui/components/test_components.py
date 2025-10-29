import sys
from PyQt5.QtWidgets import QApplication
#from time_possession import TimePossessionWidget
from faults import FaultsWidget
#from score import ScoreWidget
#from chrono import ChronoWidget
#from period import PeriodeWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #chrono = ChronoWidget()
    #chrono.show()
    #tp = TimePossessionWidget()
    #tp.show()
    F = FaultsWidget()
    F.show()
    #S = ScoreWidget()
    #S.show()
    #P = PeriodeWidget()
    #P.show()
    sys.exit(app.exec_())
