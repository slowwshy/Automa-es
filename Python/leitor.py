
import time
import re
import main
from playwright.sync_api import sync_playwright

def leitor(buttonConfirm):
    print("Iniciando automação...")
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
            elemento = pagina.get_by_text("não lidas", exact=False)
            aba = pagina.get_by_role("tab", name="Não lidas")
            numero = aba.get_by_text(re.compile(r"^\d+$"))

            if numero.is_visible():
                    time.sleep(1)
                    print("TEM MENSAGEM NÃO LIDA!", elemento.count())
                    main.processo(pagina)
            else:
                    time.sleep(1)
                    print("Nenhuma mensagem não lida.")


        except Exception as erro:
            print("[ERROR!!!]", erro)
            break


            



    

