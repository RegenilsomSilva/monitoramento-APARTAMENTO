import os
from pprint import pprint
from selenium import webdriver
from datetime import datetime
from time import sleep
import pyautogui
from pyautogui import pyscreeze
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import *

print(' ')
horario = datetime.now().strftime('%d-%m-%Y -%S')
print(horario)

print(os.linesep)

# tirando_printe_do_site = str(round(time.time() * 1000)) + '.png'
Fotografia = str(datetime.now().strftime('%d-%m-%Y -S')) +  '.png'
Print = os.path.join('Diretório',Fotografia)
pyautogui.screenshot(Print)


# printe_ja_tirado = os.path.join('Diretório', tirando_printe_do_site)
 # Depois vamos usar o webdriver ou driver para fazer a função de tirar o printe da Tela

