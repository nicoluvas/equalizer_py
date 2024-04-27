from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSlider, QLabel
from PyQt5.QtCore import Qt

class EqualizerUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        for i in range(10): # Assuming 10 bands for simplicity
            slider = QSlider(Qt.Horizontal)
            slider.setMinimum(-10)
            slider.setMaximum(10)
            slider.setValue(0)
            layout.addWidget(QLabel(f"Band {i+1}"))
            layout.addWidget(slider)
        self.setLayout(layout)
