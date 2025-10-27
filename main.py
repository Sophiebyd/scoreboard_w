import sys
from PyQt5.QtWidgets import QApplication
from ui_display import DisplayWindow
from ui_control import ControlWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    display = DisplayWindow()
    control = ControlWindow(display)
    display.show()
    control.show()
    sys.exit(app.exec_())
