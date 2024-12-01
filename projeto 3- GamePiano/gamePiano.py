import pyautogui
import keyboard
import win32api
import win32con
from time import sleep

# link do jogo
# https://gameforge.com/en-US/littlegames/magic-piano-tiles/
# precisa do jogo na tela


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


pyautogui.click(357, 404, duration=1)

while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(258, 354, (0, 0, 0)):
        click(258, 354)
    if pyautogui.pixelMatchesColor(325, 354, (0, 0, 0)):
        click(325, 354)
    if pyautogui.pixelMatchesColor(393, 355, (0, 0, 0)):
        click(393, 355)
    if pyautogui.pixelMatchesColor(454, 358, (0, 0, 0)):
        click(454, 358)
