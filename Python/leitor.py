import os
import time
import subprocess
import pyautogui 
import pyscreeze
import platform
import easyocr
import re
import main
import numpy as np
from pywinauto import Desktop
from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    navegador = p.chromium.launch(
        headless=False,
        args=["--start-maximized"]
    )

    pagina = navegador.new_page(no_viewport=True)

    pagina.goto("https://web.whatsapp.com")

    input("Entre no WhatsApp e abra a conversa. Pressione ENTER...")

    while True:
        try:
            elemento = pagina.locator("#unread-filter")

            texto = elemento.inner_text().strip().splitlines()

            if len(texto) > 1:
                    time.sleep(1)
                    print("🔔 TEM MENSAGEM NÃO LIDA!")
            else:
                time.sleep(1)
                print("Nenhuma mensagem não lida.")

        except:
            pass


    

