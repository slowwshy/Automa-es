import os
import time
import subprocess
import pyautogui
import pyscreeze
import platform
import pytesseract
import re

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

imagem = pyautogui.screenshot(region=(80, 50, 1900, 976))

imagem = imagem.convert("L")

imagem = imagem.point(
    lambda p: 255 if p > 180 else 0
)

time.sleep(1)

imagem.save("teste.png")



time.sleep(3)

text = pytesseract.image_to_string(
    imagem, 
    lang= "por", 
    config= '-c tessedit_char_whitelist"=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789áàâããéêíóôõúçÁÀÂÃÉÊÍÓÔÕÚÇ?!.,:;()-"--psm 7'
)

text = re.sub( r"[^a-zA-ZÀ-ÿ0-9?!., ]", "", text)

mensagens = re.findall(
    r"(.*?)\s\d{2}:\d{2}",
    text
)

print(text)

print(mensagens)

time.sleep(20)

os.remove("teste.png")