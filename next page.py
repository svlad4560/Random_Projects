import pyautogui
import time
# Start position under the R in ready (x=2912, y=788)
# First Excel box = (x=2942, y=233)
# search bar = (x=1941, y=222)
# Char No = (x=2392, y=487)
# search cart = (x=2200, y=535)
a = 0
b = 100

first_cell_x = 2942
first_cell_y = 233
excel_tab_click_x = 3331
excel_tab_click_y = 21



for a in range(b):

    #cliick First excel
    pyautogui.click(excel_tab_click_x, excel_tab_click_y)
    time.sleep(1)

    #click again
    pyautogui.press('down')
    time.sleep(1)

    # cntrl + c
    pyautogui.hotkey('ctrl',"c")
    time.sleep(1)

    first_cell_y += 21

    # Click Search bar
    pyautogui.click(1941, 222)
    time.sleep(3)

    #click Chart No.
    pyautogui.click(2392, 487)
    time.sleep(2)

    #paste v
    pyautogui.hotkey("ctrl","v")
    time.sleep(2)

    #click Search charts
    pyautogui.click(2200, 535)
    time.sleep(2.5)

    # click chart number
    pyautogui.click(2005,338)
    time.sleep(2.5)

    #click adminstrative login_button
    pyautogui.click(2259, 168)
    time.sleep(2.5)

    #click Print wizard
    pyautogui.click(2742, 400)
    time.sleep(2.5)

    #click Genrate Files
    pyautogui.click(2421, 455)
    time.sleep(2)

    #click close Files
    pyautogui.click(2654, 490)
    time.sleep(1.25)

    pyautogui.click(2607, 127)
    time.sleep(1.25)



# print(pyautogui.position())
