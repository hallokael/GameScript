# -*- coding: cp936 -*-
import ctypes
import time
from PIL import ImageGrab
#构造RECT结构体
class RECT(ctypes.Structure):
    _fields_ = [('left', ctypes.c_long),
                ('top', ctypes.c_long),
                ('right', ctypes.c_long),
                ('bottom', ctypes.c_long)]
    def __str__(self):
        return str((self.left, self.top, self.right, self.bottom))

HWND = ctypes.windll.user32.FindWindowA(None, "")
print (HWND)
if HWND == 0:
    print ("找不到窗口")
    quit()
rect =RECT()
ctypes.windll.user32.GetWindowRect(HWND,ctypes.byref(rect))
#去掉状态栏
rangle = (rect.left+2,rect.top+2,rect.right-2,rect.bottom-2)
time.sleep(2)
im = ImageGrab.grab(rangle)
im.show()