import pyautogui
import time
import pydirectinput
# pip install pywin32
import win32con
import win32gui


def focusWindow(window_title):
    windowFound = win32gui.FindWindow(None, window_title)

    if windowFound:
        win32gui.ShowWindow(windowFound, win32con.SW_RESTORE)
        win32gui.SetForegroundWindow(windowFound)
        print("window focused")
        time.sleep(0.5)
    else:
        print("window not found")
    return
    
 
def lookForHome():

    focusWindow("BloonsTD6")
    while True:
        try:
            buttonLocation = pyautogui.locateOnScreen('home.png', confidence=0.7)
            print("Looking for home/next button")
            if buttonLocation:
                pyautogui.click(buttonLocation)
                print("Home Button found!")
                main()
                break
            else:
                print("Button not found :(")
        except pyautogui.ImageNotFoundException:
            print("Button not found, checking again in 5 seconds")
        time.sleep(5)
        try:
            buttonLocation = pyautogui.locateOnScreen('next.png', confidence=0.7)
            if buttonLocation:
                pyautogui.click(buttonLocation)
                print("Next Button found!")
                pyautogui.click(850, 850)
                time.sleep(2)
                main()
                break
            else:
                print("Button not found :(")
        except pyautogui.ImageNotFoundException:
            print("Button not found, checking again in 5 seconds")
        time.sleep(5)
    return #if this doesnt work im blaming chatgpt


def main(): 
    time.sleep(3)
    menuNav()
    return

def menuNav():
    focusWindow("BloonsTD6")
    pyautogui.click(837, 985)
    time.sleep(0.5)
    pyautogui.click(421, 225)
    time.sleep(0.5)
    pyautogui.click(600, 450)
    time.sleep(0.5)
    pyautogui.click(1300, 450)
    time.sleep(2.5)
    pyautogui.click(1000, 750)
    placeTowers()
    return

def placeTowers():
    focusWindow("BloonsTD6")
    time.sleep(1)
    mermonkey1 = 628
    mermonkey2 = 502

        # place first ninja monkey
    pydirectinput.press('d')
    pyautogui.click(500, 500)
    time.sleep(0.1)
    pyautogui.click(500, 500)
    for i in range(4):
        pydirectinput.press('t')
    pydirectinput.press('b')
        
        # place alch
    pydirectinput.press('f')
    pyautogui.click(500, 560)
    time.sleep(0.1)
    pyautogui.click(500, 560)
    for i in range(4):
        pydirectinput.press('t')
    pydirectinput.press('g')
    pydirectinput.press('g')
    


        # literally all of the mermonkeys lol
    for i in range(5):
        
        pydirectinput.press(';')
        pyautogui.click(mermonkey1, mermonkey2)
        mermonkey1 = mermonkey1 + 87
    mermonkey1 = 900
    mermonkey2 = 427
    for i in range(4):
        pydirectinput.press(';')
        pyautogui.click(mermonkey1, mermonkey2)
        mermonkey2 = mermonkey2 - 75
    mermonkey1 = 497
    mermonkey2 = 403
    for i in range(3):
        pydirectinput.press(';')
        pyautogui.click(mermonkey1, mermonkey2)
        mermonkey2 = mermonkey2 - 75
    
    pydirectinput.press(';')
    pyautogui.click(625, 375)
    pydirectinput.press(';')
    pyautogui.click(730, 375)
    pydirectinput.press(';')
    pyautogui.click(730, 285)
    pydirectinput.press(';')
    pyautogui.click(627, 285)
    pydirectinput.press(';')
    pyautogui.click(490, 663)

    mermonkey1 = 645
    mermonkey2 = 675
    for i in range(6):
        
        pydirectinput.press(';')
        pyautogui.click(mermonkey1, mermonkey2)
        mermonkey1 = mermonkey1 + 90
    mermonkey1 = 1150
    mermonkey2 = 436
    for i in range(3):
        pydirectinput.press(';')
        pyautogui.click(mermonkey1, mermonkey2)
        mermonkey2 = mermonkey2 + 75

    # extra monkeys (glue gunner, wizard)
    pydirectinput.press('y')
    pyautogui.click(430, 500)
    pydirectinput.press('a')
    pyautogui.click(410, 390)

    pydirectinput.press('space')
    pydirectinput.press('space')
    lookForHome()
    return

menuNav()
