import pyautogui
import requests
import PIL
from PIL import Image,ImageGrab
import os
import base64
from io import BytesIO
# press('a')c
# pyautogui.typewrite('cka',interval=1)
# pyautogui.hotkey('alt', 'y')
# pyautogui.moveTo(500,500)
# pyautogui.click()
# pyautogui.keyDown('alt')
# pyautogui.press('y')
# pyautogui.keyUp('alt')
im = ImageGrab.grab()
# im.show()
# ls_f=base64.b64encode(im)
print(im)
im.save("hhhhh.jpg","JPEG")
#
# r = requests.get('http://3.haoi23.net/svlist.html')
# print(r.text)
buffer = BytesIO()
im.save(buffer, format="JPEG")
print(base64.b64encode(buffer.getvalue()))



