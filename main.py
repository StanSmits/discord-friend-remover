import pyautogui
import time

"""
Point(x=1448, y=154)
Point(x=1512, y=242)
Point(x=1081, y=578)
"""
amountOfFriends = 0

screensize = pyautogui.size()
X1, Y1 = (1448 / 1920) * screensize[0], (152 / 1080) * screensize[1]
X2, Y2 = (1512 / 1920) * screensize[0], (242 / 1080) * screensize[1]
X3, Y3 = (1081 / 1920) * screensize[0], (578 / 1080) * screensize[1]


for i in range(amountOfFriends):
    pyautogui.click(X1, Y1)
    time.sleep(0.2)

    pyautogui.click(X2, Y2)
    time.sleep(0.3)

    pyautogui.click(X3, Y3)
    time.sleep(0.5)
