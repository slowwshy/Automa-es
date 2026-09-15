
import time
import subprocess
from playwright.sync_api import sync_playwright




def processo(pagina):
       pagina.get_by_text("Não lidas", exact=True).click()

       time.sleep(4)

       print(pagina.locator("body").inner_text())