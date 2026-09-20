import time
from pathlib import Path

ARQUIVO = Path(__file__).parent / "Mensages.txt"

def processo(pagina):
       pagina.get_by_text("Não lidas", exact=True).click()

       time.sleep(2)

       conversa = pagina.get_by_role("row").first
       conversa.click()

       time.sleep(1)

       campo = pagina.get_by_test_id("conversation-compose-box-input")
       mensagem = ARQUIVO.read_text(encoding="utf-8").strip() if ARQUIVO.exists() else ""
       campo.click()
       campo.fill(mensagem or ".")
       pagina.keyboard.press("Enter")

       time.sleep(2)

       pagina.get_by_test_id("conversation-header").get_by_role(
              "button",
              name="Mais opções"
              ).click()
      
       time.sleep(1)

       pagina.get_by_text("Fechar conversa", exact=True).click()

       time.sleep(1)

       pagina.get_by_text("Tudo", exact=True).click()

      


