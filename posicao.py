import pyautogui
import time

### CAIXA DE TEXTO
# pag.confirm("Are you ready?") # Você esta pronto?
# pag.alert("The program has crashed!") #O programa travou!
# pag.prompt("Please enter your name: ") #Por favor, insira seu nome:

#capturar posição
#time.sleep(5)

#print(pyautogui.position())
#x, y = pyautogui.position()

# sim_ou_nao = pyautogui.confirm("Are you ready?")

# if sim_ou_nao == "OK":
#     print("CONFIRMADO!")
# else:
#     print("CANCELADO")
pyautogui.PAUSE = 3
pyautogui.keyDown('alt')
pyautogui.press('tab')
pyautogui.keyUp('alt')
pyautogui.press('SIAPE2.PNG')