import pyautogui
import keyboard

click = False

while True:
    if keyboard.is_pressed('a'):
        click = not click
        while keyboard.is_pressed('a'):
            pass

    if keyboard.is_pressed('q'):
        break

    if click:
        pyautogui.click()


