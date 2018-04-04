from pyautogui import *
from PIL import ImageGrab
from PIL import Image
from numpy import *
from time import *
A=getWindows()
# for k,v in A:
#     print(k,v)
for k in A.keys():
    if('神武3' in k):
        B=getWindow(k)
        a,b,*_=B.get_position()
        print(a,b)
        if((a,b)!=(0,0)):
            B.move(0,0)
B.set_foreground()
sleep(2)
im=ImageGrab.grab()
I = array(im)
print(I.shape)
# I[:600][:800][:]=200
# for i in range(420):
#     for j in range(800):
#         I[i][j]=[0,0,0]
# for i in [130]:
#     for j in range(420,460):
#         print(I[i][j])
#[130 197 192]
for i in range(280,320):
    for j in [733]:
        print(I[i][j])
F=0
calc=0
TopRaw=-1
for i in range(200,10,-1) :
    # print(i)
    calc=0
    for j in range(380,420):
        if((I[i][j]==array([130 ,197 ,192])).any()==False):
            calc+=1
            if calc>20:
                F=1
                break
    if(F==0):
        TopRaw=i+1
        break
    F=0
print('TopRaw:',TopRaw)

calc=0
BottomRaw=-1
for i in range(400,620) :
    # print(i)
    calc=0
    for j in range(380,420):
        if((I[i][j]==array([130 ,197 ,192])).any()==False):
            calc+=1
            if calc>20:
                F=1
                break
    if(F==0):
        BottomRaw=i-1
        break
    F=0
print('BottomRaw',BottomRaw)


calc=0
LeftRaw=-1
for j in range(200,10,-1):
    calc=0
    for i in range(280,320):
    # print(i)
        if((I[i][j]==array([130 ,197 ,192])).any()==False):
            calc+=1
            if calc>20:
                F=1
                break
    if(F==0):
        LeftRaw=j+1
        break
    F=0
print('LeftRaw',LeftRaw)


calc=0
RightRaw=-1
for j in range(500,820):
    calc=0
    for i in range(280,320):
    # print(i)
        if((I[i][j]==array([130 ,197 ,192])).any()==False):
            calc+=1
            if calc>20:
                F=1
                break
    if(F==0):
        RightRaw=j-1
        break
    F=0
print('RightRaw',RightRaw)
print(I[330][72])
print(I[131][381])

# im = Image.fromarray(uint8(I))
# im.show()