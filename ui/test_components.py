import sys
from PyQt5.QtWidgets import QApplication
from components.chrono import ChronoWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    chrono = ChronoWidget()
    chrono.show()
    sys.exit(app.exec_())
