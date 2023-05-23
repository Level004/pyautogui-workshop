import pyautogui
import keyboard

count = 0
while True:
    # on Q press it stops the script
    if keyboard.is_pressed("q"):
        print("stopping loop")
        break

    # clicks on the cookie
    pyautogui.click(x=266, y=490)
    count += 1

    # if count reaches 100 it stops clicking on the cookie
    # then it clicks on the upgrades then resumes clicking on the cookie
    if count == 100:
        base = 325
        for i in range(4):
            pyautogui.click(x=1767, y=base)
            base += 60
        count = 0
