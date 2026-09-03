import os
import time
import subprocess
import pyautogui
import pyscreeze
import platform
import easyocr
import re
def main(texto):
    numero = "5561996759176"

    sistema = platform.system()

    if sistema == "Windows":
            subprocess.Popen(["start", f"whatsapp://send?phone={numero}"], shell=True)

    elif sistema == "Linux":
            subprocess.Popen(["xdg-open", f"whatsapp://send?phone={numero}"])

    time.sleep(2)

    pyautogui.click(1000, 1000)

    time.sleep(2)

    pyautogui.write("hello")

    time.sleep(2)

    pyautogui.press("enter")

    time.sleep(2)

    imagem = pyautogui.screenshot(region=(450, 50, 1470, 976))

    time.sleep(1)

    imagem.save("teste.png")

    time.sleep(3)


    reader = easyocr.Reader(['pt'])


    resultado = reader.readtext('teste.png')

    for coordenadas, texto, confianca in resultado:
            with open("arquivo.txt", "a") as arquivo:
                arquivo.write(texto + "\n")

    time.sleep(40)

    os.remove("arquivo.txt")
    os.remove("teste.png")

   