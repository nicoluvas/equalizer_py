from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
from ui import EqualizerUI
from process import load_audio, play_audio, apply_equalization

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.equalizerUI = EqualizerUI()
        layout.addWidget(self.equalizerUI)
        
        # Add a "Play" button
        self.playButton = QPushButton("Play")
        self.playButton.clicked.connect(self.play_audio)
        layout.addWidget(self.playButton)
        
        self.setLayout(layout)
        self.setWindowTitle('Audio Equalizer')
        self.show()

    def play_audio(self):
        # Load and play the audio
        audio = load_audio("hell_rise.mp3")
        play_audio(audio)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec_()
