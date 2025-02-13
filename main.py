import pyautogui
import time
import keyboard
import emoji

#apenas clicar
def clicar(x, y):
    pyautogui.click(x, y)


#clicar e escrever
def escrever():
    pyautogui.click(1300, 989)
    texto = emoji.emojize("1️⃣CRAVOS")
    pyautogui.write(texto, interval=0.25)



#aqui da o set  de onde o mouse vai ir e clicar na tela de acordo com as coordenada e vai mandar para as funcao
def autoclick():
    print("Auto clicker iniciado! Pressione 'ESC' para parar.")
    while not keyboard.is_pressed("esc"):
        escrever()
        clicar(1597, 995)
        time.sleep(3)
    print("Auto clicker encerrado.")

#quando clicar no f9 o codigo vai rodar
keyboard.add_hotkey("f9", autoclick)

print("Pressione F9 para iniciar o auto clicker. Pressione ESC para parar.")

keyboard.wait("esc")