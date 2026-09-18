import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
import leitor

app = QApplication(sys.argv)
layout = QVBoxLayout()
system = bool

window = QWidget()
window.setWindowTitle("Automa-es.py")
window.resize(800, 500)
window.setLayout(layout)
window.show()

button = QPushButton("Start")
button.setFixedSize(250, 70)
button.setStyleSheet("background-color: blue")
layout.addWidget(button)

def stop():
    global system
    system = False

ButtonOff = QPushButton("Stop")
ButtonOff.setFixedSize(250, 70)
ButtonOff.setStyleSheet("background-color: red")
layout.addWidget(ButtonOff)
ButtonOff.clicked.connect(stop)

def start():
    
    buttonConfirm = QPushButton("Confirm")
    buttonConfirm.setFixedSize(150, 40)
    buttonConfirm.setStyleSheet("background-color: gray")
    layout.addWidget(buttonConfirm)
    message_label = QLabel("Quando se conectar ao whatsapp, clique em confirmar para começar a automação.")
    layout.addWidget(message_label)
    buttonConfirm.clicked.connect(lambda: leitor.leitor(system))

button.clicked.connect()

sys.exit(app.exec())