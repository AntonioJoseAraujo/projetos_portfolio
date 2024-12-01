import os
import webbrowser
import pyautogui
import pyperclip
from time import sleep


def msg(txt):
    pyperclip.copy(txt)
    pyautogui.hotkey('ctrl', 'v')

# Opção 1 (descomentar a opção desejada)
# telefones = [5516993785434, 55479875432, 557896385274] # 55 Brasil + DD + Número


# Opção 2 (descomentar a opção desejada)
telefones = []
arquivo_fones = 'fones.txt'

# Verificar o diretório atual de trabalho 
print("Diretório atual de trabalho:", os.getcwd()) # Definir o nome do arquivo com o caminho para o subdiretório 
arquivo_fones = os.path.join('projeto 4- MsgWhatsApp', 'fones.txt') # Listar todos os arquivos no diretório atual para ver se o subdiretório está correto 
print("Arquivos no diretório atual:", os.listdir())

# OP 2- Verificar se o arquivo existe
if os.path.exists(arquivo_fones):
    with open(arquivo_fones, 'r') as arquivo:
        for linha in arquivo:
            telefones.append(linha.strip())
    print(telefones)
else:
    print(f"Erro: O arquivo '{arquivo_fones}' não foi encontrado.")

# Envio das mensagens
for telefone in telefones:
    webbrowser.open(f'https://api.whatsapp.com/send?phone={telefone}')
    sleep(10)
    pyautogui.click(730, 220, duration=1)
    sleep(10)
    msg('Olá tudo bem? Estou usando sua automação que esta no seu portfolio, para teste.')
    sleep(5)
    pyautogui.press('enter')
    sleep(300)
