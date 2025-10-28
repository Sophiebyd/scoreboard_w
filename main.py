import sys
from PyQt5.QtWidgets import QApplication
from ui.public_view import PublicView
from ui.referee_view import RefereeView

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Fenêtre de 
    display = PublicView()
    display.show()

    # Fenêtre de arbitre_view
    control = RefereeView(display)
    control.show()

    sys.exit(app.exec())
