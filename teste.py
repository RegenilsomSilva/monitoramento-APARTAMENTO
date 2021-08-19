import os
import smtplib
from email.message import EmailMessage
import imghdr
import time
from datetime import datetime
import random
from time import sleep
import glob
import shutil
import pathlib

Mostrando_o_horario_que_enviou  = datetime.now().strftime('%d/%m/%Y  %H:%M')
Mostra_a_data_do_ano            = datetime.now().strftime('%d/%m/%Y')

print(Mostrando_o_horario_que_enviou,'\n')
print(Mostra_a_data_do_ano,'\n')
print(f'Valores Atualizado as {Mostrando_o_horario_que_enviou[10:]} do Dia {Mostra_a_data_do_ano}')