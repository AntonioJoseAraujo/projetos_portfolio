import pyautogui
import keyboard
from time import sleep

# link do jogo
# https://guitarflash.com/?lg=pt
# precisa do jogo na tela

while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(286, 599, (0, 152, 0)):
        pyautogui.press('a')
        sleep(0.05)
    if pyautogui.pixelMatchesColor(376, 599, (255, 0, 0)):
        pyautogui.press('s')
        sleep(0.05)
    if pyautogui.pixelMatchesColor(462, 600, (244, 244, 2)):
        pyautogui.press('j')
        sleep(0.05)
