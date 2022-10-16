import os
import time
import win32api
import win32con
import pyautogui


def deleteFile(path):
    if os.path.exists(path):
        os.remove(path)


def getClick(msg):
    print(msg)
    while True:
        a = win32api.GetKeyState(0x02)
        if a == -127 or a == -128:
            x, y = pyautogui.position()
            return x, y
        time.sleep(0.01)


def dragMouseInverted(x1, x2, y1, y2):
    win32api.SetCursorPos((x2, y2))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x2, y2)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x1 - x2, y1 - y2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x1, y1)
