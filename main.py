import pyautogui
import time
import cv2

# pos x, y (105,142)

# open Whatsapp
pyautogui.hotkey("win", "2")

# finding the position of search box
 # print(pyautogui.position())

time.sleep(7)
pyautogui.moveTo(105, 140)
pyautogui.click()

# Enter name of the account_name
Account_name = 'Captain American '
pyautogui.write(Account_name)
pyautogui.hotkey("enter")


# position message box of WhatsApp (731 984)

time.sleep(2)
pyautogui.moveTo(731, 984)

# Enter your message
message = "hello"

# Enter number of messages in Numbers
no_of_messages = 4

for _ in range(no_of_messages):
    pyautogui.write(message)
    pyautogui.hotkey("enter")


