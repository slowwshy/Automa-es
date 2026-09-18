
import time
import re
import main
from playwright.sync_api import sync_playwright

def leitor(buttonConfirm):
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
               

            except Exception as erro:
                print("[ERROR!!!]")
                break
            



    

