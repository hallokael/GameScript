from Common import *
from time import *
import ctypes
import time
import time
import random
import ctypes
MOUSE_LEFTDOWN = 0x0002     # left button down
MOUSE_LEFTUP = 0x0004       # left button up
MOUSE_RIGHTDOWN = 0x0008    # right button down
MOUSE_RIGHTUP = 0x0010      # right button up
MOUSE_MIDDLEDOWN = 0x0020   # middle button down
MOUSE_MIDDLEUP = 0x0040     # middle button up
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
def gogo(x,y):
    while(x!=0 and y!=0):
        dirx=x/sqrt(x*x+y*y)
        diry=y/sqrt(x*x+y*y)
        nx=int(20*dirx+random.random()*3)
        ny=int(20*diry+random.random()*3)
        if x<25:
            nx=x
        if y<25:
            ny=y
        x-=nx
        y-=ny
        ctypes.windll.user32.mouse_event(0,nx,ny,0,0)
        sleep(0.01)
    pass
sleep(3)
random.seed()
time=0
Down=0
olda=clock()
while(True):
    a=clock()
    print(a-olda)
    olda=a
    im=ImageGrab.grab((846,530,996,570))
    # im.save("why.png")
    # im.show()
    # break
    I=array(im)
    i=0
    left=-1
    right=-1
    time=0
    AvgL=0
    AvgR=0
    AvgH=0
    for i in range(40):
        NowRed=0
        NowAvgL=AvgL
        NowAvgR=AvgR
        NowAvgH=AvgH
        NowL=left
        NowR=right
        for j in range(150):
            if(I[i][j][0]>210 and I[i][j][1]<150 and I[i][j][2]<150 and max(I[i][j][1],I[i][j][2])-min(I[i][j][1],I[i][j][2])<30 ):
                NowRed+=1
                if j<75:
                    if left==NowL:
                        left+=1
                    AvgL+=j
                    AvgH+=i
                if j>=75:
                    if right==NowR:
                        right+=1
                    AvgR+=j
                    AvgH+=i
        if NowRed>10:
            left=NowL
            right=NowR
            AvgL=NowAvgL
            AvgR=NowAvgR
            AvgH=NowAvgH
    if(left>10 and right>10):
        pass
        # if Down==0:
        print('Press')
        ctypes.windll.user32.mouse_event(MOUSE_LEFTDOWN,0,0,0,0)
        GoLR=(AvgL/left+AvgR/right-150)*1.6
        GoUD=(AvgH/(left+right)-20)*1.6
        gogo(GoLR,GoUD)
        # ctypes.windll.user32.mouse_event(MOUSE_LEFTUP,0,0,0,0)
            # Down=1
    elif left>10:
        ctypes.windll.user32.mouse_event(0,int(AvgL/left-75)*1.6,int(int(AvgH/(left+right)-20)*1.6),0,0)
        sleep(0.01)
        ctypes.windll.user32.mouse_event(MOUSE_LEFTDOWN,0,0,0,0)
        # ctypes.windll.user32.mouse_event(MOUSE_LEFTUP,0,0,0,0)
    elif right>10:
        ctypes.windll.user32.mouse_event(0,int(AvgR/right*1.6),int(int(AvgH/(left+right)-20)*1.6),0,0)
        sleep(0.01)
        ctypes.windll.user32.mouse_event(MOUSE_LEFTDOWN,0,0,0,0)
        # ctypes.windll.user32.mouse_event(MOUSE_LEFTUP,0,0,0,0)
    else:
        print(left,right)
        ctypes.windll.user32.mouse_event(MOUSE_LEFTUP,0,0,0,0)
        # pass

        # if Down==1:
        #     print('Release')
        #     print(left,right)
        #     ReleaseKey(0x24)
        #     Down=0
