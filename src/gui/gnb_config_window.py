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
    QLayout,
    QSizePolicy
    )

from PyQt6.QtCore import Qt 

from PyQt6.QtGui import (
    QIcon,
    QFont
    )

from gui.collabsible_section import collapsibleSection

M = 20

class GNBConfigWindow(QMainWindow):
    numInputs = 7
    numRows = 3

    def __init__(self):
        super().__init__()
        self.init_gui()

    def init_gui(self):

        # Initialize GUI layout and widgets

        self.main_layout = QVBoxLayout(self)
        # self.main_layout.

        self.create_toggleable_list(self.numInputs,self.numRows)
        font = QFont()
        font.setPointSize(16)

        # label = QLabel("Hello, World!", self)

        self.main_layout.addStretch()

        exit_button = QPushButton("Exit")
        # exit_action = exit_button.addAction("E&xit")
        # exit_action.triggered.connect()

        
        self.main_layout.addWidget(exit_button)

        self.main_layout.setObjectName("main_layout")
        
        self.main_layout.setSpacing(M)
        self.main_layout.setContentsMargins(M,M,M,M)
        
        # All items will be put into this widget to be shown
        main_widget = QWidget()
        main_widget.setLayout(self.main_layout)
        
        # main_widget.setSizePolicy(QSizePolicy.Policy.Expanding)
        # main_widget.set
        self.setCentralWidget(main_widget)
        self.setWindowTitle('SRSDashboard')

        #global content settings
        self.setStyleSheet("border: 1px solid black")
        self.setContentsMargins(M,M,M,M)

        self.setGeometry(600, 100, 1000, 900)
        self.setFixedSize(1000,900)

        #self.expand()
        

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
            # section.setContentsMargins(M,M,M,M)
            form_layout = QFormLayout()
            # form_layout.setContentsMargins(M,M,M,M)
            form_layout.setSpacing(M)
            for j in range(numInputs):
                form_layout.addRow(f"Test {i}, {j}", QLineEdit())
            section.inner_layout.addLayout(form_layout)
            self.main_layout.addWidget(section)


    ## UNCOMMENT ONCE DONE!

    # def closeEvent(self, event):
    #     size = self.size()
    #     dlg = QMessageBox( QMessageBox.Icon.Question,
    #                        "Confirm Exit", 
    #                         "Are you sure you want to exit?",
    #                       QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
    #                       self
    #                       )

    #     dlg.setDefaultButton(QMessageBox.StandardButton.No)

    #     result = dlg.exec()

    #     if result == QMessageBox.StandardButton.Yes:
    #         event.accept()
    #     else:
    #         event.ignore()