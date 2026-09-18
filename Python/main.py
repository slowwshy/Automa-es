import time

def processo(pagina):
       pagina.get_by_text("Não lidas", exact=True).click()

       time.sleep(2)

       conversa = pagina.get_by_role("row").first
       conversa.click()

       time.sleep(1)

       campo = pagina.get_by_test_id("conversation-compose-box-input")
       campo.click()
       campo.fill(".")
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

      


