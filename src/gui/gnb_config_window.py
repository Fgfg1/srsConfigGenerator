# src/gui/gnb_config_window.py

from PyQt6.QtWidgets import (
    QMainWindow, 
    QVBoxLayout, 
    QWidget, 
    QLabel, 
    QMessageBox , 
    QApplication,
    QFormLayout,
    QLineEdit,
    QGroupBox,
    QMenuBar,
    QMenu,
    QPushButton,
    )

from PyQt6.QtCore import Qt 

from PyQt6.QtGui import (
    QIcon,
    QFont
    )

from gui.collabsible_section import collapsibleSection

class GNBConfigWindow(QMainWindow):
    numInputs = 3
    numRows = 3

    def __init__(self):
        super().__init__()
        self.init_gui()

    def init_gui(self):
        self.main_layout = QVBoxLayout(self)
        self.setStyleSheet("border: 1px solid black")
        self.create_toggleable_list(self.numInputs,self.numRows)
        font = QFont()
        font.setPointSize(16)

        # label = QLabel("Hello, World!", self)

        exit_button = QPushButton("Exit")
        # exit_action = exit_button.addAction("E&xit")
        # exit_action.triggered.connect()

        self.main_layout.addWidget(exit_button)

        # All items will be put into this widget to be shown
        main_widget = QWidget()
        main_widget.setLayout(self.main_layout)
        self.setCentralWidget(main_widget)
        # Initialize GUI layout and widgets
        self.setWindowTitle('SRSDashboard')
        self.expand()
        

    def expand(self):
        #sets the size of the application to the full size of the screen
        screenGeometry = QApplication.screens()[0].geometry()
        width = screenGeometry.width() - 100
        height = screenGeometry.height() - 300

        # Set the window to be full screen but resizable
        self.resize(width, height)
    
    def create_menu(self):
        self.menu_bar = QMenuBar()

        self.file_menu = QMenu("&File", self)
        self.exit_action = self._file_menu.addAction("E&xit")
        self.menu_bar.addMenu(self._file_menu)

        self.exit_action.triggered.connect(self.accept)

    def create_toggleable_list(self,numRows : int, numInputs : int):
         for i in range(numRows):
            section = collapsibleSection(f"testing {i}")
            form_layout = QFormLayout()
            for j in range(numInputs):
                form_layout.addRow(f"Test {i}, {j}", QLineEdit())
            section.inner_layout.addLayout(form_layout)
            self.main_layout.addWidget(section)


    ## UNCOMMENT ONCE DONE!

    def closeEvent(self, event):
        size = self.size()
        dlg = QMessageBox( QMessageBox.Icon.Question,
                           "Confirm Exit", 
                            "Are you sure you want to exit?",
                          QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                          self
                          )

        dlg.setDefaultButton(QMessageBox.StandardButton.No)

        result = dlg.exec()

        if result == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()




        # main_layout.set(form_layout)




        # self.statusBar().showMessage('Ready')
        # self.statusBar()

        # menubar = self.menuBar()
        # fileMenu = menubar.addMenu('&File')