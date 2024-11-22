# src/main.py

import sys
from PyQt6.QtWidgets import QApplication
from gui.gnb_config_window import GNBConfigWindow

class SRSConfigGeneratorApp(QApplication):
    def __init__(self, args=None):
        super().__init__(args)
        self.init_gui()

    def init_gui(self):
        self.main_window = GNBConfigWindow()
        self.main_window.show()

def main():
    app = SRSConfigGeneratorApp(sys.argv)
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
