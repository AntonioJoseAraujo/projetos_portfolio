import pyautogui
import webbrowser
from time import sleep


def sair():
    pyautogui.click(135, 233, duration=1)
    pyautogui.click(101, 681, duration=1)
    pyautogui.click(103, 616, duration=1)


while True:
    # # -Abrir o site
    # webbrowser.open_new('https://www.instagram.com')
    # sleep(5)
    # # -Login e senha (para outros usuarios)
    # login = pyautogui.prompt(text='Digite seu login', title='Seu Login')
    # senha = pyautogui.password(text='Digite sua senha', title='Senha de login')

    # # #-Clicar para fazer o login
    # log = pyautogui.locateCenterOnScreen('login.png')
    # pyautogui.click(log[0], log[1], duration=1)
    # pyautogui.typewrite(login)
    # sleep(0.5)
    # pyautogui.press('tab')
    # pyautogui.typewrite(senha)
    # sleep(5)
    # pyautogui.press('enter')
    # sleep(5)

    # # -Salvar no navegador
    # pyautogui.click(808, 472, duration=1)
    # sleep(5)

    # -Navegar até a pagina escolhida, pesquisar a pagina
    # pesquisar = pyautogui.locateCenterOnScreen('pesquisa.png')
    # pyautogui.click(pesquisar[0], pesquisar[1], duration=1)
    # sleep(1)
    # pyautogui.typewrite('qixskate')
    # sleep(5)

    # # -Entrar na pagina
    # pyautogui.click(209, 271, duration=1)
    # sleep(3)

    # - Clicar na postagem mais recente
    pyautogui.scroll(-400)
    pyautogui.click(490, 355, duration=1)
    sleep(5)

    # - Verificar se ja foi feito a curtida
    # coracao = pyautogui.locateCenterOnScreen('coracaoN.png')
    # sleep(1)

    # - Se já tiver curtido, fazer nada, e pausar o bot por 24 horas

    # 12 - Se não tiver curtido, curtir a foto
    try:
        botao_curtir = pyautogui.locateCenterOnScreen('coracaoN.png', region=(653,529,750,650))
    except pyautogui.ImageNotFoundException:
        botao_curtir = None
        print("A imagem 'coracaoN.png' não foi encontrada na tela.")

# Aqui, caso a imagem de coração vazio tenha sido encontrado, ele vai curtir, e caso contrário, enviará o alerta de que já foi curtido.
    if botao_curtir:
        pyautogui.click(botao_curtir, duration=1.5)
        sleep(0.5)
    else:
        pyautogui.alert('Você já curtiu essa publicação!!')

    sleep(86400)

    # 13 - Se não tiver curtido, comentar na foto
    pyautogui.click(735, 677, duration=1)
    sleep(1)
    pyautogui.typewrite('Boaaa!')
    sleep(5)
    #     pyautogui.click(1059, 676, duration=1)
    # # - Após a 24 horas rodar tudo de novo
    #     sair()
    #     sleep(30)
