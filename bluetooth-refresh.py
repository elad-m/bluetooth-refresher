#! python

import pyautogui as pag
import time

pag.PAUSE = 1
pag.FAILSAFE = True


def keyboard_combo(press_and_hold_key, press_key):
    pag.keyDown(press_and_hold_key)
    pag.press(press_key)
    pag.keyUp(press_and_hold_key)
    
    
def exit_settings():
    pag.hotkey('alt', 'F4')
    
    
def navigate_settings_to_bluetooth():
    pag.moveTo(135, 141, duration=0.25)
    time.sleep(0.5)
    pag.click()
    pag.moveTo(112, 251, duration=0.25)
    time.sleep(0.5)
    pag.click()


def refresh():
    pag.moveTo(567, 138, duration=0.25) # bluetooth on-off toggle button location
    pag.click()
    time.sleep(3)
    pag.click()
    time.sleep(2)
    

def main():
    try:
        keyboard_combo('winleft', 's')
        pag.typewrite('PC settings')
        pag.moveTo(1641, 195, duration=0.25) # bluetooth settings location
        pag.click()
        time.sleep(1)
        navigate_settings_to_bluetooth()
        refresh()
        exit_settings()
    
    
    except KeyboardInterrupt:
        print('\nInterupted.')


if __name__ == "__main__":
    main()
    
    
# for i in range(5):
    # time.sleep(1)
    # print(pag.position())
