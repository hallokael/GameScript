x=500
y=400
import time
import ctypes
MOUSE_LEFTDOWN = 0x0002     # left button down
MOUSE_LEFTUP = 0x0004       # left button up
MOUSE_RIGHTDOWN = 0x0008    # right button down
MOUSE_RIGHTUP = 0x0010      # right button up
MOUSE_MIDDLEDOWN = 0x0020   # middle button down
MOUSE_MIDDLEUP = 0x0040     # middle button up
time.sleep(2)
for i in range(10):
    # time.sleep(0.1)
    if i > 0:
        pass
        # x+=17
        # y+=17
    #ctypes.windll.user32.SetCursorPos(x,y) # this does not work in game but
    #outside the game window
# for i in range(10):
#     ctypes.windll.user32.mouse_event(0,2000,0,0,0)
#     ctypes.windll.user32.mouse_event(MOUSE_LEFTDOWN,0,0,0,0)
#     ctypes.windll.user32.mouse_event(MOUSE_LEFTUP,0,0,0,0)
#     time.sleep(0.5)
ctypes.windll.user32.mouse_event(0,100,0,0,0)
print (i)