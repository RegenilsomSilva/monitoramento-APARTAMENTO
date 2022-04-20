
from datetime import datetime
from email.message import EmailMessage
import glob
import os
from shutil import move
import shutil


Mostrando_o_horario_que_enviou  = datetime.now().strftime('%H:%M')
Mostra_a_data_do_ano            = datetime.now().strftime('%d/%m/%Y')

print(Mostrando_o_horario_que_enviou,'\n')
print(Mostra_a_data_do_ano,'\n')
print(f'Valores Atualizado as {Mostrando_o_horario_que_enviou} do Dia {Mostra_a_data_do_ano}')


# targetPatter = os.path.join(os.getcwd() + os.sep + 'Diretorio_dos_excel' + os.sep + '*.xlsx')
# emails_em_anexos = glob.glob(targetPatter)
targetPatter = os.path.join(os.getcwd() + os.sep + '*.xlsx')
emails_em_anexos = glob.glob(targetPatter)
print(emails_em_anexos)
targetPatter = os.path.join(os.getcwd() + os.sep + 'Diretorio_dos_excel' + os.sep + '*.xlsx')
Destinatario = glob.glob(targetPatter)

# move(emails_em_anexos,os.path.join(os.getcwd() + os.sep + 'Diretorio_dos_excel' + os.sep ))
shutil.move(os.getcwd() + os.sep +  'Apartamento_CDHU.xlsx', os.getcwd() + os.sep + 'Diretorio_dos_excel')