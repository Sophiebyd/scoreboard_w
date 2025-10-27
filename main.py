import sys
from PyQt5.QtWidgets import QApplication
from ui_display import DisplayWindow
from ui_control import ControlWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Fenêtre d'affichage
    display = DisplayWindow()
    display.show()

    # Fenêtre de contrôle
    control = ControlWindow(display)
    control.show()

    sys.exit(app.exec())
