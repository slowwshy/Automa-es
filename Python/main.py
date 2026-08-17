import os
import time
import subprocess
import pyautogui
import pyscreeze
import platform
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

numero = "5561993299082"

sistema = platform.system()

if sistema == "Windows":
    subprocess.Popen(["start", f"whatsapp://send?phone={numero}"], shell=True)

elif sistema == "Linux":
    subprocess.Popen(["xdg-open", f"whatsapp://send?phone={numero}"])

time.sleep(2)

pyautogui.click(1000, 1000)

time.sleep(2)

pyautogui.write("")

time.sleep(2)

pyautogui.press("enter")

time.sleep(2)

imagem = pyautogui.screenshot(region=(700, 800, 976, 1818))

time.sleep(1)

imagem.save("teste.png")

time.sleep(3)

text = pytesseract.image_to_string(imagem)

print(text)