import pyautogui
import time

pyautogui.FAILSAFE =False
a = 0
b = 115
first_cell_x = 2942
first_cell_y = 234
scroll_position_x = 3770
scroll_position_y = 558

excel_tab_click_x = 3331
excel_tab_click_y = 21

# print(pyautogui.position())
# pyautogui.click(excel_tab_click_x, excel_tab_click_y)
# pyautogui.press("down",presses = 3)

# this clicks through the pages
# for a in range(b):
#
#     pyautogui.moveTo(scroll_position_x, scroll_position_y)
#     pyautogui.click()
#     pyautogui.scroll(-2500)
#     pyautogui.click(3760,643)
#     pyautogui.click(3760,643)
#     time.sleep(2)


# pyautogui.click()

# this goes down the excle file
# for a in range(b):
#     pyautogui.click(first_cell_x, first_cell_y)
#     pyautogui.click(first_cell_x, first_cell_y)
#     first_cell_y += 21
#     time.sleep(.25)


# this is to automate the copy and past into excel
bottom_corner_x = 1828
bottom_corner_y = 990

top_corner_x = 5
top_corner_y = 200

pyautogui.dragTo(top_corner_x, top_corner_y, 1,  button= 'left')
pyautogui.hotkey('ctrl',"c")
pyautogui.move(2700, -990)
pyautogui.click()
pyautogui.hotkey("ctrl", "v")
time.sleep(3)
pyautogui.moveTo(1935,238)
pyautogui.mouseDown(button = 'right')
pyautogui.click(2003,392)
pyautogui.moveTo(1977,213)
pyautogui.mouseDown(button= 'right')

print(pyautogui.position())
