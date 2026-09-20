import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QTextEdit, QLineEdit
from sympy import true
from PySide6.QtGui import QIcon
import leitor
import threading
from pathlib import Path

ARQUIVO = Path(__file__).parent / "Mensages.txt"

app = QApplication(sys.argv)
layout = QVBoxLayout()
parar = threading.Event()
confirmado = threading.Event()

def recurso(nome):
    base = Path(getattr(sys, "_MEIPASS", Path(__file__).parent))
    return str(base / nome)

app.setWindowIcon(QIcon(recurso("icone.png")))


window = QWidget()
window.setWindowTitle("Automa-es.py")
window.resize(800, 500)
window.setLayout(layout)
window.show()

campo_texto = QTextEdit()
campo_texto.setFixedHeight(100)
layout.addWidget(campo_texto)
campo_texto.setPlaceholderText("Mensagem (texto e links)")
if ARQUIVO.exists():
    campo_texto.setPlainText(ARQUIVO.read_text(encoding="utf-8"))
layout.addWidget(campo_texto)

campo_texto.textChanged.connect(
    lambda: ARQUIVO.write_text(campo_texto.toPlainText(), encoding="utf-8")
)
    
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