import pyautogui
import time

# alerta de execução
pyautogui.alert('O codigo vai começar.')
pyautogui.PAUSE = 0.5

# abre o google drive
pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('https://drive.google.com/drive/my-drive')
pyautogui.press('enter')

# area de trabalho do windows
pyautogui.hotkey('winleft', 'd')
# verifica posição do mouse
# pyautogui.position()
pyautogui.moveTo(3704, 98)
pyautogui.mouseDown()
pyautogui.moveTo(2318, 1413)
pyautogui.hotkey('alt', 'tab')
time.sleep(1)
pyautogui.mouseUp()

time.sleep(5)
pyautogui.alert('O codigo finalizou.')
pyautogui.PAUSE = 0.5
