import os
import time
import subprocess
import pyautogui
import pyscreeze
import platform
import easyocr
import re
from leitor import pagina, navegador


def main(texto):
        conversa_nao_lida = pagina.locator(
    '[data-testid="cell-frame-container"]').filter(
        has = pagina.locator('[data-testid="icon-unread-count"]')
)
        conversa_nao_lida.first.click(button="left")