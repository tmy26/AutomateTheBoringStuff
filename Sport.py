import webbrowser
import win32api
import win32con
import time
import pyautogui as auto
import pyperclip
import pyautogui
from datetime import datetime


def shouldItStart():
    """Method to check if the program should start"""
    hour_to_start = 08
    mins_to_start = 00
    while True:
        now = datetime.now()
        current_h = now.strftime("%H")
        current_minutes = now.strftime("%M")
        hour = int(current_h)
        mins = int(current_minutes)
        if hour == hour_to_start and mins == mins_to_start:
            break


def wait(seconds):
    """Method wait"""
    time.sleep(seconds)


def openGoogleMeet():
    """Method open google meet"""
    webbrowser.open('https://meet.google.com/kbz-jazk-jru')


def move_mouse_and_click(x, y):
    """Method that moves the cursor position at x, y coordinates and simulates mouse click"""
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


def writeDownYourInfo(x, y):
    """Method that simulates typing, mouse click and moves the cursor to x,y position"""
    move_mouse_and_click(x,y)
    pyperclip.copy('Том Йорданов СИ 2101321049')
    wait(2)
    pyautogui.hotkey("ctrl", "v")
    wait(1)

def sendInfo(x, y):
    """Method that simulates mouse click, moves the cursor to x,y position, waits x time, and closes the browser"""
    move_mouse_and_click(x,y)
    wait(3300)
    pyautogui.hotkey("alt", "f4")


def main():
    """Method main"""
    shouldItStart()
    openGoogleMeet()
    wait(60)
    move_mouse_and_click(680, 750)
    move_mouse_and_click(770, 750)
    wait(5)
    move_mouse_and_click(1246, 570)
    wait(66)
    writeDownYourInfo(1780, 1030)
    sendInfo(1856, 960)


if __name__ == "__main__":
    main()









