
import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import leitor

app = QApplication(sys.argv)
layout = QVBoxLayout()

window = QWidget()
window.setWindowTitle("Automa-es.py")
window.resize(800, 500)
window.setLayout(layout)
window.show()

button = QPushButton("Start")
layout.addWidget(button)

button.clicked.connect(leitor.leitor)
sys.exit(app.exec())