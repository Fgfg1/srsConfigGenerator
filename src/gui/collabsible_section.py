
from PyQt6.QtWidgets import (
    QGroupBox,
    QVBoxLayout,
    QWidget,
    QSizePolicy,
    QLayout
)

from PyQt6.QtCore import Qt

# Spacing global
S = 20

class collapsibleSection(QGroupBox):
    def __init__(self, title, parent=None):
        super().__init__(title, parent)
        self.setCheckable(True)
        self.setChecked(False)
        self.toggled.connect(self.toggle_section)

        # self.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.inner_layout = QVBoxLayout()
        self.inner_widget = QWidget()
        self.inner_widget.setLayout(self.inner_layout)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.inner_widget)
        main_layout.setContentsMargins(S,S,S,S)
        self.setLayout(main_layout)

        self.inner_widget.setVisible(False)
        # self.setStyleSheet("border: 1px solid red")
        self.setContentsMargins(S,S,S,S)

    def toggle_section(self, checked):
        self.inner_widget.setVisible(checked)