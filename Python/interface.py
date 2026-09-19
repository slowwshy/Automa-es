import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
import leitor
import threading

app = QApplication(sys.argv)
layout = QVBoxLayout()
parar = threading.Event()
confirmado = threading.Event()

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

def stop():
    print("Automação interrompida pelo usuário.")
    parar.set()

ButtonOff.clicked.connect(stop)

def start():
    parar.clear()
    confirmado.clear()
    threading.Thread(target=leitor.leitor, args=(parar, confirmado), daemon=True).start()

buttonConfirm = QPushButton("Confirm")
buttonConfirm.setFixedSize(150, 40)
buttonConfirm.setStyleSheet("background-color: gray")
layout.addWidget(buttonConfirm)
message_label = QLabel("Quando se conectar ao whatsapp, clique em confirmar para começar a automação.")
layout.addWidget(message_label)
buttonConfirm.clicked.connect(confirmado.set)
   
button.clicked.connect(start)

sys.exit(app.exec())