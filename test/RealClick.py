from Common import *
from time import *
import ctypes
import time

SendInput = ctypes.windll.user32.SendInput


W = 0x11
A = 0x1E
S = 0x1F
D = 0x20

# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
sleep(3)
time=0
# for i in range(20):
#     time+=1
#     print(time)
#     im=ImageGrab.grab()
#     im.show()
#     im.save("uuuu"+str(time)+".png")
# MoveWindow2zeroOW()
Down=0
olda=clock()
while(True):
    a=clock()
    # print(a-olda)
    olda=a
    im=ImageGrab.grab((846,550,996,551))
    I=array(im)
    # print(I)
    i=0
    left=-1
    right=-1
    time=0
    for j in range(0,150):
        # II[i-200][j-200]=I[i][j]
        if(I[i][j][0]>210 and I[i][j][1]<150 and I[i][j][2]<150 and max(I[i][j][1],I[i][j][2])-min(I[i][j][1],I[i][j][2])<30 ):
        # if(I[i][j][0]>230 and I[i][j][1]<90 and I[i][j][2]<90 and max(I[i][j][1],I[i][j][2])-min(I[i][j][1],I[i][j][2])<30 ):
        #     print(I[i][j],time)
            # print(i,j)
            if j<75:
                left=1
            if j>=75:
                right=1
            # time+=1
            # elif I[i][j][0]>200:
            #     II[i-200][j-200]=I[i][j]
            #     time+=1
    if(left+right==2):
        print('Fire')
        if Down==0:
            # keyDown(']')
            print('Press')
            PressKey(0x24)
            Down=1
    else:
        if Down==1:
            # keyUp(']')
            print('Release')
            print(left,right)
            ReleaseKey(0x24)
            Down=0
    # im.show()
    # im.save('testT123.png')
    # break
    # print("123")
        # if time>10:
        #     print("YES")
        # else:
        #     print("NO")
    # im.show()
    # sleep(5)
    # im.show()
    # im.save("test2.png")
# for i in range(20):
#     sleep(1)
#     click()
