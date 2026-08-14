import os
import time
import subprocess
import pyautogui
import pyscreeze
import platform

numero = "5561993299082"

sistema = platform.system()

if sistema == "Windows":
    subprocess.Popen(["start", f"whatsapp://send?phone={numero}"], shell=True)

elif sistema == "Linux":
    subprocess.Popen(["xdg-open", f"whatsapp://send?phone={numero}"])

time.sleep(2)

pyautogui.click(800, 1000)

time.sleep(2)

pyautogui.write("linda")

time.sleep(6)

imagem = pyautogui.screenshot()

imagem.save("teste.png")

pyautogui.press("enter")
