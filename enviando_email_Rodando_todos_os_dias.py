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



print(os.linesep)
class EnvioDeEmails:

    def __init__(self):
# Configuração de login
        print(f'configuração de Login {os.linesep}')
        self.ENDERECO_EMAIL  = os.environ.get('EMAIL_REMETENTE')
        self.SENHA_EMAIL     = os.environ.get('SENHA_DO_EMAIL')
        self.contatos        = ['paula43oliveira@hotmail.com','regenilsomfeliz@outlook.com']
    
    def Start_Send(self):

        self.Configurations_To_Envio()
        self.Anexa_Files()
        self.Anexo_Imagens()
        self.To_Send_Email()
        

    def Configurations_To_Envio(self):
# Criando o e-mail
        print(f'Criando um  E-mail para ser Enviado{os.linesep}.....Aguarde{os.linesep}')
        self.mensagem = EmailMessage()
        self.mensagem['Subject'] = f'Valores Atualizado ás {datetime.now()}'
        self.mensagem['From'] =  self.ENDERECO_EMAIL
        self.mensagem['To'] = ', '.join(self.contatos)
        self.mensagem.set_content(' 🙌🙌🙌🙌 Olá a Sua Pesquisa do Apartamento CDHU Chegou ✔️ !!!')
    

# Configurar o anexo de imagens
    def Anexo_Imagens(self):
        
        print(f'⚙🔍 Configuração de Envio de Imagens para o E-mail...{os.linesep}....Aguarde ⚙🔍 {os.linesep}')

        # Estarei fazendo com que o sistema faça a integração caminho + o Diretório que se encontra as fotos .png
        targetPatter  = os.path.join(os.getcwd() + os.sep + 'Arquivo_TEMPORARIO_de_print_do_site' + os.sep + '*.png')
        caminho_das_fotos = glob.glob(targetPatter)
        
        # Aqui estou fazendo um Loop, para que o Sistema Encontre minha extensão .png 
        for caminho_das_foto in caminho_das_fotos:
            with open(caminho_das_foto, 'rb') as arquivo:
                dados = arquivo.read()
                extensao_imagem = imghdr.what(arquivo.name)
                nome_arquivo = arquivo.name
            self.mensagem.add_attachment(dados, maintype='image',
                               subtype=extensao_imagem, filename=nome_arquivo)

            print(f'⏳ Acabamos de Fazer a Manipulação de imagens.... ⏳ {os.linesep}.....Aguarde')
            sleep(random.randint(1,2))
            print(os.linesep)                   

    def Anexa_Files(self):      
# Anexar arquivos

        print(f' 🙌🙌 Enviando E-mail com Anexo de Arquivo{os.linesep}.......Aguarde{os.linesep}')
        emails_em_anexos = str[os.path.join(os.getcwd() + os.sep + 'Apartamento_CDHU.xlsx')]


        for email_em_anexo in emails_em_anexos:
            with open(email_em_anexo, 'rb') as anexo:
                informacoes_anexo = anexo.read()
                nome_arquivo = anexo.name
            self.mensagem.add_attachment(informacoes_anexo, maintype='application', subtype='octet-stream', filename=nome_arquivo)
            print(os.linesep)

    def To_Send_Email(self):
  # Fazendo  o envio de Emails      
        for contato in self.contatos:          
            print(f' 🙌🙌 Fazendo Envio Seguro de E-mail{os.linesep}......Aguarde{os.linesep}')

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as sistema_de_envio:
                sistema_de_envio.login(self.ENDERECO_EMAIL, self.SENHA_EMAIL)
                sistema_de_envio.send_message(self.mensagem)
                sleep(random.randint(8,10))

        print(f'🤖🤖Obrigado por usar o Nosso Boot🤖🤖🤖{os.linesep}') 

SendingMailing = EnvioDeEmails()
SendingMailing.Start_Send()           
