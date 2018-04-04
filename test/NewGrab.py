# -*- coding: cp936 -*-
import ctypes
import time
from PIL import ImageGrab
#����RECT�ṹ��
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
    print ("�Ҳ�������")
    quit()
rect =RECT()
ctypes.windll.user32.GetWindowRect(HWND,ctypes.byref(rect))
#ȥ��״̬��
rangle = (rect.left+2,rect.top+2,rect.right-2,rect.bottom-2)
time.sleep(2)
im = ImageGrab.grab(rangle)
im.show()