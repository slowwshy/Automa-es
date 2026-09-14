
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
button.setFixedSize(250, 70)
button.setStyleSheet("background-color: blue")
layout.addWidget(button)

ButtonOff = QPushButton("Stop")
ButtonOff.setFixedSize(250, 70)
ButtonOff.setStyleSheet("background-color: red")
layout.addWidget(ButtonOff)


if(button.clicked.connect(leitor.leitor)):
    buttonConfirm = QPushButton("Confirm")
    buttonConfirm.setFixedSize(250, 70)
    buttonConfirm.setStyleSheet("background-color: gray")
    layout.addWidget(buttonConfirm)

sys.exit(app.exec())