import sys
from PyQt5.QtWidgets import QApplication
#from components.chrono import ChronoWidget
from components.time_possession import TimePossessionWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #chrono = ChronoWidget()
    #chrono.show()
    tp = TimePossessionWidget()
    tp.show()
    sys.exit(app.exec_())
