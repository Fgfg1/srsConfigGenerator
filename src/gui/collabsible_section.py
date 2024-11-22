
from PyQt6.QtWidgets import (
    QGroupBox,
    QVBoxLayout,
    QWidget,
)

from PyQt6.QtCore import Qt

class collapsibleSection(QGroupBox):
    def __init__(self, title, parent=None):
        super().__init__(title, parent)
        self.setCheckable(True)
        self.setChecked(False)
        self.toggled.connect(self.toggle_section)

        self.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.inner_layout = QVBoxLayout()
        self.inner_widget = QWidget()
        self.inner_widget.setLayout(self.inner_layout)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.inner_widget)
        self.setLayout(main_layout)

        self.inner_widget.setVisible(False)

    def toggle_section(self, checked):
        self.inner_widget.setVisible(checked)