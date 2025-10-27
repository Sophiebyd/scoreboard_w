from PyQt5.QtWidgets import QPushButton

# Bouton représentant un "niveau de faute"
class FaultButton(QPushButton):
    def __init__(self, update_callback):
        super().__init__()
        self.fault_level = 0
        self.update_callback = update_callback
        self.setFixedSize(16, 16)  # petit rond
        self.update_style()
        self.clicked.connect(self.increment_fault)

    def increment_fault(self):
        self.fault_level = (self.fault_level + 1) % 4
        self.update_style()
        if self.update_callback:
            self.update_callback(self.fault_level)

    def update_style(self):
        color = ["transparent", "red", "orange", "black"][self.fault_level]
        border_color = ["gray", "red", "orange", "black"][self.fault_level]
        self.setStyleSheet(
            f"border-radius:8px;"
            f"border:2px solid {border_color};"
            f"background-color:{color};"
            f"padding:0px;margin:0px;"
        )
