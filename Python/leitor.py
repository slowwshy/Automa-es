import os
import time
import re
import main
import sys
from playwright.sync_api import sync_playwright

if getattr(sys, "frozen", False):   
    os.environ["PLAYWRIGHT_BROWSERS_PATH"] = "0"

def leitor(parar, confirmado):

        with sync_playwright() as p:

            navegador = p.chromium.launch(
                headless=False,
                args=["--start-maximized"]
            )

            pagina = navegador.new_page(no_viewport=True)
            pagina.goto("https://web.whatsapp.com")


            while not confirmado.is_set():
                time.sleep(1)

            while True:
                try:
                    elemento = pagina.get_by_text("não lidas", exact=False)
                    aba = pagina.get_by_role("tab", name="Não lidas")
                    numero = aba.get_by_text(re.compile(r"^\d+$"))

                    if numero.is_visible():
                            time.sleep(1)
                            main.processo(pagina)
                    else:
                            time.sleep(1)
                    if parar.is_set():
                        break
                except Exception as erro:
                    print(f"Erro: {erro}")
                    break
                


            



    

