import os
import glob
from time import sleep
import random
from datetime import datetime


#targetPatter = r"C:\Users\regen\Desktop\Projetos_Pyton\AUTOMACAO\Mestre do E-mail\Arquivo_TEMPORARIO_de_print_do_site\*.png"

# BUSCAR POR DIRETORIO VAI PROCURA PASTA QUE SE ENCONTRA AS FOTOS OU OS PRINTS '.PNG'
targetPatter = os.path.join(os.getcwd() + os.sep + 'Arquivo_TEMPORARIO_de_print_do_site' + os.sep +   '*.png') 
# VAMOS ATRIBUIR A UMA VARIAVÉL, PARA BUSCAR TODAS AS INFORMAÇÕES DO targetPatter
caminho_do_diretorio = glob.glob(targetPatter)

print(caminho_do_diretorio)
print(os.linesep)
print(os.linesep)

# vamos aguardar um tempo para que o Sistema envie o E-mail com as Imagens e Depois os apague 
sleep(random.randint(15,35))
print(f'⏭ Vamos Excluir todas as Fotos com final .png{os.linesep}.....Aguarde{os.linesep}')

for caminhos_dos_diretorios in caminho_do_diretorio:
    print(f'⏭ Vamos criar um Laço de Repetição  para poder resolver a questão da exclusão em Massa {os.linesep}')
    os.remove(caminhos_dos_diretorios)
    print(f'⏭ Excluimos com Sucesso {os.linesep}')

    mostrando_horario_certo =  datetime.now().strftime('%d%m%Y %H:%M')
    mostrando_a_data = datetime.now().strftime('%d-%m-%Y')

    print(f'💯💯💯 Exclusão feitas as {mostrando_horario_certo[9:]} do Dia {mostrando_a_data}{os.linesep} ')

    print(f'🤖🤖Obrigado por usar o Nosso Boot🤖🤖🤖 até mais...{os.linesep}{os.linesep}')