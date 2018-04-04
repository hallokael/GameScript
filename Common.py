from pyautogui import *
# import pyautogui
import random
from PIL import ImageGrab
from PIL import Image
from numpy import *
from time import *
import time
from PIL import ImageChops
from os import listdir
from os.path import isfile, join
from Data.MapConnect import graph
from Data.MapSize import MapSize
from Data.NPC_DATA import NPC,NPCsp
import Data.Global
from Data.Global import mouseX
from Data.Global import mouseY
from functools import reduce
import base64
import requests
from io import BytesIO
import threading
import sys,os
import datetime
from configparser import ConfigParser
AllImage={}
AllPer={}
AllWords={}
AllPlace={}
AllShop={}
AllTask={}
AllBuy={}
AllNumber={}
OtherIm={}
random.seed()
def MainRun():
    # pyautogui.PAUSE=0
    # timer=threading.Timer(2.0,ProtectError,0)
    # timer.start()
    MoveWindow2zero()
    sleep(2)
    GetMouseXY()
    NowPos=WhereIs()
    OldPos=WhereIs()
    Data.Global.STime=0
    while True:

        OldPos=NowPos
        NowPos=WhereIs()
        if NowPos==OldPos:
            Data.Global.STime+=1
        else:
            Data.Global.STime=0
        print('STime'+str(Data.Global.STime))
        if 3<Data.Global.STime<5:
            ReStart()
        if Data.Global.STime>5:
            RealReStart()
            Data.Global.STime=0
        while CheckAllState():
            print("CHECK")
        Now = time.time()
        if Now - Data.Global.XiangTime >1500:
            press('f5')
            Data.Global.XiangTime=Now
            # r=random.random()*1+2
        # sleep(r)
        now,next=FindNext()
        print("next:"+str(next))
        if next!="":
            RunToNext(now,next)
        t=WaitForNotMove()
        if t<=2:
            while CheckAllState():
                pass
            print('ClickNPCsp')
            for i in NPCsp:
                if i==(now+'-'+next):
                    press('f9')
                    a,b,c=NPCsp[i]
                    RealMoveTo(a+ran(),b+ran())
                    click()
                    SleepR(1.5,0.5)
                    press('f9')
def GetTaskAndGoal(im):
    type=GetTypeOfTask(im)
    print("type:")
    print(type)
    TotalGoal(im,type,0)
def TotalGoal(im,type,time):
    print('TotalGoal')
    if 0<type<3 or type==4:
        Goal,xx,yy=GetGoal()
        print('Goal:'+Goal)
        if Goal != "False":
            Data.Global.x=xx
            Data.Global.y=yy
            Data.Global.path = GetPath('长安城', Goal)
            # if Data.Global.path==[]:
            #     Data.Global.path.append(WhereIs())
            if(xx!=-1 and yy!=-1):
                Data.Global.path.append('tempPos')
            else:
                GetFinalGoal(Data.Global.path)
            if WhereIs() not in Data.Global.path:
                Data.Global.path=GetPath(WhereIs(),Goal)
                print('PATH!!!!')
                print(Data.Global.path)
                if Data.Global.path==[]:
                    Data.Global.path.append(WhereIs())
                if(xx!=-1 and yy!=-1):
                    Data.Global.path.append('tempPos')
                else:
                    GetFinalGoal(Data.Global.path)
            print (Data.Global.path,xx,yy)
    # elif type==3:
    #     BuyWeaponAndCommit()
    elif type==3:
        SleepR(0.5,0.1)
        im=ImageGrab.grab()
        type = GetTypeOfTask(im)
        if type!=3:
            return
        if IsBuySuccess()==True:
            BuyNormalAndCommit()
            return
        type=FindTypeOfBuy()
        print('buyType:'+str(type))
        if type==1:
            BuyNormalAndCommit()
        if type==2:
            BuyWeaponAndCommit()

    else:

        if time==1:
            GetNewTask()
            SleepR(2,0.5)
            im=ImageGrab.grab()
            GetTaskAndGoal(im)
        else:
            SleepR(5, 0.5)
            im=ImageGrab.grab()
            type=GetTypeOfTask(im)
            print("type:")
            print(type)
            TotalGoal(im, type, 1)
def FindTypeOfBuy():
    print('FindType1')
    l=WhereBuy()
    print('FindType2')
    print(l)
    if l==[]:
        return 1
    else:
        return 2
def GetNewTask():
    if IsAllOver():
        for i in range(100):
            print('AllOver')
        while True:
            SleepR(1,1)
    Data.Global.path=[]
    # Data.Global.ZCTime+=1
    # if Data.Global.ZCTime>10:
    #     ReZC()
    #     Data.Global.ZCTime=0
    print("GetNewTask")
    if ReturnBT()==False:
        print("GetNewTask Fail")
        return
    x,y,z=NPC['长安城']['镖头']
    ClickCoord(x,y)
    while True:
        WaitForNotMove()
        im=ImageGrab.grab()
        I=array(im)
        if IsTalk(I):
            RmoveRel(mouseX,351,mouseY,404)
            click()
            SleepR(0.5,0.5)
            press('esc')
            SleepR(2,0.5)
            print("ClickBT")
            break
        else:
            ClickCoord(x,y)
    print('GetNewTask Finish')
def RealMoveTo(x,y):
    # RmoveRel(0,x,0,y)
    # return
    x=int(x)
    y=int(y)
    T=0
    while(True):
        # moveTo(x,y)
        # SleepR(0.5,0.5)
        T+=1
        if T>200:
            for i in range(100):
                print('RealMoveError')
            # while True:
            #     SleepR(1,1)
            ReStart()
            return
        a,b=position()
        de=random.random()*2+2
        if abs(a-x)<15 and abs(b-y)<15:
            moveTo(x,y,0.01*de,easeInOutQuad)
        else:
            xF=1
            yF=1
            if random.random()>0.97:
                xF=-1
            if random.random()>0.97:
                yF=-1
            sX=sign(x-a)
            if sX==0:
                if random.random()<0.5:
                    sX=0.1
                else:
                    sX=-0.1
            sY=sign(y-b)
            if sY==0:
                if random.random()<0.5:
                    sY=0.1
                else:
                    sY=-0.1
            moveRel(sX*xF*random.randint(0,15),sY*yF*random.randint(0,15),0.01*de,easeInOutQuad)
            # moveRel(sX*xF*random.randint(0,15),sY*yF*random.randint(0,15),0.01*de)
            # print('moveRel')
        # print(x,y,a,b)
        if x==a and y==b :
            print("RealMove")
            Data.Global.mouseX=a
            Data.Global.mouseY=b
            break
def BuyWeaponAndCommit():
    while(IsBuySuccess()==False):
        F=BuyWeapon()
        if F==False:
            return
    ReturnBT()
    x,y,z=NPC['长安城']['镖头']
    ClickCoord(x,y)
    while True:
        WaitForNotMove()
        im=ImageGrab.grab()
        I=array(im)
        if IsTalkBT(I):
            RmoveRel(mouseX,309+ran(),mouseY,443+ran())
            # moveTo(309,443)
            click()
            break
        else:
            ClickCoord(x,y)
    while True:
        im=ImageGrab.grab()
        im=im.crop((431,331,506,349))
        I=array(im)
        f=0
        for i in range(I.shape[0]):
            for j in range(I.shape[1]):
                if I[i][j][0]==0 and I[i][j][1]==254 and I[i][j][2]==0:
                    f=1
                    break
            if f==1:
                break
        if f==1:
            # RealMoveTo(400,100)
            # SleepR(0.3,0.3)
            RmoveRel(mouseX,397+ran(),mouseY,341+ran())
            # moveTo(442,341)
            SleepR(0.3,0.3)
            click()
            RmoveRel(mouseX,Data.Global.mouseX-200+ran(),mouseY,Data.Global.mouseY+ran())
            # moveRel(-200,0)
            break
        SleepR(1,1)
    while(True):
        im=ImageGrab.grab()
        I=array(im)
        if GetDiffOfColor( I[102,569] , [152,223,217] )>15:
            SleepR(0.5,0.5)
            # RealMoveTo(0,400)
            # moveRel(-1000,-1000)
        else:
            a,b=GetLightOne(I)
            RmoveRel(mouseX,a+ran(),mouseY,b+ran())
            # for i in range(20):
            #     moveRel((a-400)/20,(b-100)/20)
            #     sleep(0.1)
            click()
            SleepR(0.5,0.5)
            RmoveRel(mouseX,266+ran(),mouseY,514+ran())
            SleepR(0.5,0.5)
            click()
            break

    # 152,223,217
    # SleepR(3,0.1)
    print('BuyAndCommit Over')
def BuyNormalAndCommit():
    while(IsBuySuccess()==False):
        F=BuyNormal()
        if F==False:
            return
    ReturnBT()
    x,y,z=NPC['长安城']['镖头']
    ClickCoord(x,y)
    # SleepR(3,0.1)
    print('BuyNormalAndCommit Finish')
def RmoveRel(stx,enx,sty,eny):
    print('RmoveRel')
    T=0
    # print(pyautogui.PAUSE)
    print(Data.Global.mouseX,enx,Data.Global.mouseY,eny)
    x=enx-Data.Global.mouseX
    y=eny-Data.Global.mouseY
    de=random.random()*2+2
    while(True):
        T+=1
        if T>200:
            for i in range(100):
                print('RelMoveError')
            ReStart()
            return
            # while True:
            #     SleepR(1,1)
        # xp=1
        # yp=1
        if random.random()>0.97:
            xp=-1
        else:
            xp=1
        if random.random()>0.97:
            yp=-1
        else:
            yp=1
        if x<0:
            xp*=(-1)
        if y<0:
            yp*=(-1)
        if x==0:
            if random.random()<0.5:
                xp*=(-0.1)
            else:
                xp*=0.1
        if y==0:
            if random.random()<0.5:
                yp*=(-0.1)
            else:
                yp*=0.1
        if abs(x)<15 and abs(y)<15:
            moveRel(x,y,0.1,easeInOutQuad)
            x=0
            y=0
        else:
            xx=random.randint(0,15)
            x-=(xx*xp)
            yy=random.randint(0,15)
            y-=(yy*yp)
            moveRel(xx*xp,yy*yp,0.01*de,easeInOutQuad)
            # pyautogui.moveRel(xx)
            # moveRel(xx*xp,yy*yp,0.01*de)
        a,b=position()
        # print(enx,eny,a,b,x,y)
        # sleep(0.01)
        if x==0 and y==0:
            xx,yy=position()
            if xx>800 or yy>600:
                ReStart()
                return
            Data.Global.mouseX=enx
            Data.Global.mouseY=eny
            return

def GetLightOne(I):
    ml=0
    mq,mw=-1,-1
    for q in range(5):
        for w in range(8):
            nl=0
            for j in range(q*48+388,q*48+431):
                for i in range(w*48+153,w*48+169):
                   for k in range(3):
                       if I[i][j][k]>200:
                           print(q,w)
                           print(i,j,k)
                           return 388+q*48+20,153+w*48+5
    #                    nl+=I[i][j][k]
    #         if nl>ml:
    #             ml,mq,mw=nl,q,w
    # return mq,mw
def ReturnBT():
    UseFlag('f6',2,2)
    print("FlagFinish")
    SleepR(2.0,0.5)
    if WhereIs()=='长安城':
        return True
    return False
def UseFlag(a,b1,b2):
    RealMoveTo(400+ran()*100.1,200+ran()*100.1)
    SleepR(0.5,0.5)
    press(a)
    SleepR(0.3,0.3)
    RmoveRel(mouseX,215+b2*120,mouseY,290+b1*30)
    # moveTo(215+b2*120,290+b1*30)
    SleepR(0.5,0.3)
    click()
    SleepR(3,0.5)
    # mouseDown()
    # print('Down')
    # SleepR(1,1)
    # print('Up')
    # mouseUp()
def IsBuySuccess():
    print('IsBuySuccess')
    im=ImageGrab.grab()
    im=im.crop((620+Data.Global.Xp,165,706+Data.Global.Xp,175))
    I=array(im)
    for i in range(I.shape[0]):
        for j in range(I.shape[1]):
            if I[i][j][0]==0 and I[i][j][1]==254 and I[i][j][2]==0:
                return True
    return False
def GetTypeOfTask(im):
    if Data.Global.mouseX>500:
        RmoveRel(mouseX,300+100*ran(),mouseY,300+100*ran())
    x1=614+Data.Global.Xp
    x2=665+Data.Global.Xp
    y1=166
    y2=178
    # im=ImageGrab.grab((x1,y1,x2,y2))
    im=im.crop((x1,y1,x2,y2))
    I=array(im)
    for i in range(I.shape[0]):
        for j in range(I.shape[1]):
            if I[i][j][0]==254 and I[i][j][1]==254 and I[i][j][2]==0:
                I[i][j]=[254,254,0]
            else:
                I[i][j]=[0,0,0]
    im=Image.fromarray(I)
    # im.save('whyyyyy.png')
    for i in AllTask:
        # print(i)
        if equal(AllTask[i],im):
            # im.show()
            # AllTask[i].show()
            return int(i)
    return -1
def BuyWeapon():
    while(True):
        a=WhereBuy()
        print(a)
        if a!=[]:break
        else:return False

    L1=['临仙镇', '傲来国', '清河镇', '长安城']
    L2=['服饰店', '武器店']
    tempD={'长安城':[599,291],'傲来国':[599,325],'临仙镇':[599,353],'清河镇':[599,261]}
    L3=['临仙服饰店', '临仙武器店', '傲来服饰店', '傲来武器店', '清河服饰店', '清河武器店', '长安服饰店', '长安武器店']
    for i in L1:
        if i in a:
            while(True):
                print("Buy1")
                press('f6')
                RmoveRel(mouseX,tempD[i][0]+ran(),mouseY,tempD[i][1]+ran())
                click()
                SleepR(1,1)
                if WhereIs()==i:
                    break
            for j in L2:
                if j in a:
                    while(True):
                        print("Buy2")
                        if WhereIs() in L3:
                            break
                        x,y,uio=NPC[i][j]
                        print(i,j)
                        ClickCoord(x,y)
                        WaitForNotMove()
                    while(True):
                        print("Buy3")
                        press('f9')
                        RealMoveTo(NPC[str(i)+str(j)][0]+ran(),NPC[str(i)+str(j)][1]+ran())
                        # moveTo(NPC[str(i)+str(j)][0],NPC[str(i)+str(j)][1])
                        click()
                        SleepR(1,1)
                        im=ImageGrab.grab()
                        I=array(im)
                        if IsTalk(I):
                            y = FindTalkColor(I)
                            print(y)
                            if y == -1:
                                print('error')
                            else:
                                RmoveRel(mouseX,312+random.random()*20,mouseY, y+ran())
                                click()
                                # RmoveRel(mouseX,425,mouseY, 37)
                                # RealMoveTo(425,37)
                            SleepR(1,1)
                            while(True):
                                RmoveRel(0,275,0,525)
                                SleepR(0.5,0.2)
                                imS=Image.open('需求s.png')
                                im=ImageGrab.grab()
                                x,y=FindImgInImg(im,imS,50,500,50,500)
                                print(x,y)
                                if x!=-1:
                                    # for i in range(4):
                                    #     moveRel(0,100)
                                    #     sleep(0.5)
                                    # moveRel(0,58)
                                    RmoveRel(mouseX,442+ran(),mouseY,mouseY+489+ran())
                                    click()
                                    sleep(1)
                                    while(True):
                                        imS=Image.open('需求s.png')
                                        im=ImageGrab.grab()
                                        x,y=FindImgInImg(im,imS,50,500,50,500)
                                        print(x,y)
                                        if x==-1:
                                            ESCconfirm()
                                            print('esc')
                                            break
                                        else:
                                            # RealMoveTo(425,37)
                                            # for i in range(4):
                                            #     moveRel(0,100)
                                            #     sleep(0.5)
                                            # moveRel(0,58)
                                            RmoveRel(mouseX,442+ran(),mouseY,mouseY+489+ran())
                                            click()
                                            SleepR(1,0.5)
                                    break
                            break
                        press('f9')
            break
    print('Buy Over')
    return True
def BuyNormal():
    while True:
        kind=WhereBuyN()
        if kind!=-1:
            break
        else:
            return False
    while(True):
        UseFlag('f6',0,1)
        ClickCoord(295,34)
        # RealMoveTo(350+ran()*100,200+ran()*100)
        WaitForNotMove()
        im=ImageGrab.grab()
        # im.save('ttt.png')
        I=array(im)
        if IsTalk(I):
            y=FindJYTalkColor(I)
            RmoveRel(mouseX,350+ran()*20,mouseY,y+ran())
            # moveTo(350,y)
            print("YYY"+str(y))
            click()
            w=0
            SleepR( 2.5,0.5)
            im=ImageGrab.grab()
            I=array(im)
            for i in range(400,410):
                if GetDiffOfColor(I[100][i],[146,217,209])>20:
                    w=1
                    break
            if w==0:
                while(True):
                    #     131,126
                    # RmoveRel(131-350,126-y+29*kind)
                    RmoveRel(mouseX,131+ran(),mouseY,126+29*kind+ran())
                    click()
                    SleepR(1.5,0.5)
                    break
                break
    # posx=131
    # posy=126+29*kind
    while(True):
        # 426,466
        im=ImageGrab.grab()
        imS=OtherIm['需求s']
        # I=array(im)
        a,b=FindImgInImg(im,imS,209,471,105,431)
        print("find 需求s")
        print(a,b)
        if a==-1:
            RmoveRel(mouseX,426+ran(),mouseY,466+ran())
            # RmoveRel(426-posx,466-posy)
            click()
            SleepR(1,0.5)
        else:
            # RmoveRel(a-posx,b-posy)
            RmoveRel(mouseX,a+ran(),mouseY,b+ran()+10)
            click()
            SleepR(1,0.5)
            press('enter')
            SleepR(1,0.5)
            ESCconfirm()
            break
    return True
    print("BuyNormalFinish")
def WhereBuy():
    l=[]
    RmoveRel(0,586+Data.Global.Xp+ran(),0,187+ran() )
    click()
    SleepR(1,1)
    # 554,255,767,388
    im=ImageGrab.grab((574+Data.Global.Xp,300,853+Data.Global.Xp,486))
    I=array(im)
    print('WhereBuy1')
    for i in range(I.shape[0]):
        for j in range(I.shape[1]):
            if I[i][j][0]==254 and I[i][j][1]==254 and I[i][j][2]==0:
                pass
            else:
                I[i][j]=[0,0,0]
    im=Image.fromarray(I)
    print('WhereBuy2')
    for i in AllPlace:
        print('WhereBuy3'+i)
        a,b=FindImgInImg(im,AllPlace[i],0,853-574,0,486-300)
        if a!=-1 :
            l.append(i)
            print('find '+i)
    # RealMoveTo(634+Data.Global.Xp+ran()*5,315+ran()*5 )
    # moveTo(634,315)
    # click()
    press('esc')
    return l
def WhereBuyN():
    l=-1
    # moveTo(586,187)
    RmoveRel(0,586+Data.Global.Xp+ran(),0,187+ran())
    click()
    SleepR(1,1)
    im=ImageGrab.grab((554+Data.Global.Xp,255,767+Data.Global.Xp,458))
    I=array(im)
    for i in range(I.shape[0]):
        for j in range(I.shape[1]):
            if I[i][j][0]==254 and I[i][j][1]==254 and I[i][j][2]==254:
                pass
            else:
                I[i][j]=[0,0,0]
    im=Image.fromarray(I)
    for i in AllBuy:
        a,b=FindImgInImg(im,AllBuy[i],0,767-554,0,458-255)
        if a!=-1 :
            # AllBuy[i].show()
            l=int(i)
            break
    # moveTo(634,315)
    # RealMoveTo(634+Data.Global.Xp+ran()*5,315+ran()*5 )
    # click()
    press('esc')
    print("kind "+str(l))
    return l
def SleepR(s,ran):
    r=random.random()*ran+s
    sleep(r)
# def IsTalkTwoLine(im):
#     calc=0
#     im = im.crop((267, 339, 512, 356))
#     I = array(im)
#     for i in range(I.shape[0]):
#         for j in range(I.shape[1]):
#             if (I[i][j] == [254, 254, 254]).all() == True:
#                 calc+=1
#     if calc>5:
#         return True
#     return False
def WaitForNotMove():
    im111=GetMapInf2()
    t=0
    while(1):
        t+=1
        SleepR(2.5,0.5)
        print("waiting for not change")
        im222=GetMapInf2()
        if ImgEqual(im111,im222):
            return t
        else:
            im111=im222
def CheckAllState(Sp=False):
    im=ImageGrab.grab()
    I=array(im)

    if IsCheckR(I):
        if Data.Global.CheckState==2:
            ReGetMouseXY()
        Data.Global.CheckState=2
        Data.Global.STime=0
        print('IsCheckR')
        k=GetCheckRAns()
        if k==0:
            RmoveRel(mouseX,230+ran(),mouseY,362+ran())
        if k==1:
            RmoveRel(mouseX,357+ran(),mouseY,361+ran())
        if k==2:
            RmoveRel(mouseX,485+ran(),mouseY,367+ran())
        if k==3:
            RmoveRel(mouseX,609+ran(),mouseY,362+ran())
        click()
        print("Ans:"+str(k))
        r=random.random()*1+2
        sleep(r)
        return True
    x,y=IsCheckLNew(im)
    if x!=-1:
        if Data.Global.CheckState==3:
            ReGetMouseXY()
        Data.Global.CheckState=3
        Data.Global.STime=0
        print('IsCheckLNew')
        k=GetLAnsByHaoi(x,y)
        k=int(k)
        x-=26
        RmoveRel(mouseX,x+(800-2*x)/8*(1+2*(k-1))+ran(),mouseY,367+ran())
        click()
        r=random.random()*1+3
        sleep(r)
        im=ImageGrab.grab()
        x,y=IsCheckLNew(im)
        if x!=-1:
            RmoveRel(mouseX, x + (800 - 2 * x) / 8 * (1 + 2 * (k - 1)) + ran()-10, mouseY, 367 + ran())
            click()
        r=random.random()*1+3
        sleep(r)
        im = ImageGrab.grab()
        x,y=IsCheckLNew(im)
        if x!=-1:
            RmoveRel(mouseX, x + (800 - 2 * x) / 8 * (1 + 2 * (k - 1)) + ran()+10, mouseY, 367 + ran())
            click()
        r = random.random() * 1 + 2
        sleep(r)
        return True
    if IsCheckP(I):
        Data.Global.STime=0
        # if Data.Global.CheckState==4:
        #     ReGetMouseXY()
        Data.Global.CheckState=4
        print('IsCheckP')
        DealCheckP(I,im)
        r=random.random()*1+2
        sleep(r)
        return True
    if IsTab(I):
        if Data.Global.CheckState==5:
            ReGetMouseXY()
        Data.Global.CheckState=5
        print('IsTab')
        press('tab')
        r=random.random()*1+2
        sleep(r)
        return True
    if IsFight(I):
        # if Data.Global.CheckState==6:
        #     ReGetMouseXY()
        Data.Global.CheckState=6
        print('IsFight')
        Data.Global.STime=0
        if Data.Global.FightDel==0:
            cokey('ctrl','a')
            Data.Global.FightDel=20
        Data.Global.FightDel-=1
        Data.Global.PlusNeed=True
        r=random.random()*1+2
        sleep(r)
        return True
    if IsTalk(I):
        if Data.Global.CheckState==7:
            ReGetMouseXY()
        Data.Global.CheckState=7
        Data.Global.STime=0
        print('IsTalk')
        # if MissionOver(im):
        #     print('MissionOver')
        # if GetTask1(im):
        #     print('GetTask')
        if IsReach()!="":
            print('IsReach')
            y=FindTalkColor(I)
            print(y)
            if y==-1:
                print('error')
            else:
                # RealMoveTo(400,100)
                # sleep(0.3)
                RmoveRel(mouseX,322,mouseY,y)
                click()
        else:
            press('esc')
            # RmoveRel(mouseX,349,mouseY,380)
            # click()
        r=random.random()*1+2
        sleep(r)
        return True
    SleepR(1,1)
    GetMouseXY()
    if Data.Global.PlusNeed:
        PlusHP()
        Data.Global.PlusNeed=False
    if Sp==False:
        GetTaskAndGoal(im)
    Data.Global.CheckState=8
    return False
def PlusHP():
    RealMoveTo(643+ran()*5,35+ran()*2)
    SleepR(0.1,0.05)
    click(button='right')
    RealMoveTo(644+ran()*5,45+ran()*2)
    SleepR(0.1,0.05)
    click(button='right')
    RealMoveTo(644+ran()*5,68+ran()*2)
    SleepR(0.1,0.05)
    click(button='right')
    RealMoveTo(761+ran()*5,32+ran()*2)
    SleepR(0.1,0.05)
    click(button='right')
    RealMoveTo(762+ran()*5,45+ran()*2)
    SleepR(0.1,0.05)
    click(button='right')
def GetCheckRAns():
    ims=[]
    for i in range(50):
        ims.append(ImageGrab.grab())
    # im = Image.open('Rotation/asd1.png')
    im=ims[0]
    I = []
    I.append(array(im.crop((220, 350, 233, 391))))
    I.append(array(im.crop((352, 350, 365, 391))))
    I.append(array(im.crop((477, 350, 490, 391))))
    I.append(array(im.crop((604, 350, 617, 391))))
    # print(I)
    Run = zeros((4))
    for i in range(2, 50):
        im=ims[i-1]
        II = []
        II.append(array(im.crop((220, 350, 233, 391))))
        II.append(array(im.crop((352, 350, 365, 391))))
        II.append(array(im.crop((477, 350, 490, 391))))
        II.append(array(im.crop((604, 350, 617, 391))))
        for k in range(4):
            TemNum = 0
            fl = 0
            for i in range(II[1].shape[0]):
                for j in range(II[1].shape[1]):
                    Dif = GetDiffOfColor(I[k][i][j], II[k][i][j])
                    if Dif > 100:
                        TemNum += 1
                        if TemNum > 10:
                            Run[k] += 1
                            fl = 1
                            break
                if fl == 1:
                    break
        I = II
    maxR=-1
    maxRi=-1
    print(Run)
    for i in range(4):
        if Run[i]>maxR:
            maxR=Run[i]
            maxRi=i
    return maxRi
def FindTalkColor(I):
#     267,321,414,410
    for j in range(267,414):
        calc=0
        for i in range(321,410):
            if I[j][i][0]<10 and I[j][i][1]>200 and I[j][i][2]>200:
                # print(i,j,I[j][i])
                calc+=1
        if calc>10:
            return j+5
    return -1
def FindJYTalkColor(I):
    #     267,321,414,410
    #     275,336,401,451
    for j in range(275,451):
        calc=0
        for i in range(336,451):
            if I[j][i][0]<10 and I[j][i][1]>200 and I[j][i][2]>200:
                print(i,j,I[j][i])
                calc+=1
        if calc>10:
            return j+25
    return -1
def MissionOver(im):
    im = im.crop((317, 319, 512, 356))
    I = array(im)
    for i in range(I.shape[0]):
        for j in range(I.shape[1]):
            if (I[i][j] != [254, 254, 254]).any() == True:
                I[i][j] = [0, 0, 0]
    im = Image.fromarray(I)
    im1=Image.open('ImageParse/跑镖结束.png')
    if ImgEqual(im,im1):
        return True
    return False
def GetTask1(im):
    im = im.crop((317, 319, 512, 336))
    I = array(im)
    for i in range(I.shape[0]):
        for j in range(I.shape[1]):
            if (I[i][j] != [254, 254, 254]).any() == True:
                I[i][j] = [0, 0, 0]
    im = Image.fromarray(I)
    im1=Image.open('ImageParse/运镖.png')
    if ImgEqual(im,im1):
        return True
    return False
def GetGoal():
    im = ImageGrab.grab()
    I = array(im)
    im2 = GetMissionDetail(I)
    goal=FindGoal(im2)
    x,y=FindGoalXY(im2)
    return goal,x,y
def FindNext():
    now=WhereIs()
    print("now:"+str(now))
    f=0
    next=""
    for i in Data.Global.path:
        if f==1:
            next=i
            break
        if(now==i):
            f=1
    return now,next
def RunToNext(now,next):
    print("runtonext")
    if now=='清河镇外':
        if next=='东海龙宫':
            SpecialRunInQH(1)
            return
        elif next=='傲来国':
            SpecialRunInQH(2)
            return
        elif next=='清河镇':
            SpecialRunInQH(3)
            return
    a=-1
    b=-1
    c=-1
    if next=='tempPos':
        a=Data.Global.x
        b=Data.Global.y
    else:
        # for i in NPC[now]:
        #     print(i)
        a,b,c=NPC[now][next]
    ClickCoord(a,b)
def cokey(a,b):
    keyDown(a)
    press(b)
    keyUp(a)
def equal(im1, im2):
    return ImageChops.difference(im1, im2).getbbox() is None
def ImgEqual(im1,im2):
    I1=array(im1)
    I2=array(im2)
    # print(I2.shape[0],I2.shape[1])
    for i in range(I2.shape[0]):
        for j in range(I2.shape[1]):
            if((I1[i][j]==I2[i][j]).any()==False):
                I=I1[i][j]-I2[i][j]
                for k in range(3):
                    I[k]=max(I1[i][j][k],I2[i][j][k])-min(I1[i][j][k],I2[i][j][k])
                    if(I[k]>20):
                        return False
    return True
def mouse2(a,b):
    c, d = position()
    time=1
    while(c!=a or d!=b):
        time+=1
        # print(time)
        # if time>50:
        #     return
        c, d = position()
        if(abs(c-a)<15 and abs(d-b)<15):
            moveTo(a,b)
            break
        if(a-c>0):
            tempX=15
        else:
            tempX=-15
        if(b-d>0):
            tempY=15
        else:
            tempY=-15
        # tempX,tempY=a-c,b-d
        p=random.random()
        dir1=random.random()
        dir2=random.random()
        # print(dir1,dir2)
        if(dir1>0.5):
            dir1=1
        else:
            dir1=-1
        if(dir2>0.5):
            dir2=1
        else:
            dir2=-1
        # moveTo(c+tempX+p*dir1*3,d+tempY+p*dir2*3)
        moveTo(c+tempX,d+tempY)
        # sleep(1.0/100.0)
def WhereIs():
    im=GetMapInf()
    for k in AllImage.keys():
        if(equal(AllImage[k],im)):
            Data.Global.where=k
            print(k)
            return k
    for k in AllShop.keys():
        if(equal(AllShop[k],im)):
            Data.Global.where=k
            print(k)
            return k
    MoveWindow2zero()
    return ""
def OpenAllImage():
    onlyfiles = [ f[:-4] for f in listdir('res') if f.endswith('.png') ]
    print(onlyfiles)
    for i in onlyfiles:
        AllImage[i]=Image.open('res/'+str(i)+'.png')
    onlyfiles = [ f[:-4] for f in listdir('res/Person') if f.endswith('.png') ]
    print(onlyfiles)
    for i in onlyfiles:
        AllPer[i]=Image.open('res/Person/'+str(i)+'.png')
    onlyfiles = [ f[:-4] for f in listdir('ImageParse/words/') if f.endswith('.png') ]
    print(onlyfiles)
    for i in onlyfiles:
        AllWords[i]=Image.open('ImageParse/words/'+str(i)+'.png')
    onlyfiles = [ f[1:-4] for f in listdir('res/Y') if f.endswith('.png') ]
    print(onlyfiles)
    for i in onlyfiles:
        AllPlace[i]=Image.open('res/Y/Y'+str(i)+'.png')
    onlyfiles = [ f[:-4] for f in listdir('res/Shop') if f.endswith('.png') ]
    print(onlyfiles)
    for i in onlyfiles:
        AllShop[i]=Image.open('res/Shop/'+str(i)+'.png')
    onlyfiles = [ f[4:-4] for f in listdir('res/Task') if f.endswith('.png') ]
    print(onlyfiles)
    for i in onlyfiles:
        AllTask[i]=Image.open('res/Task/type'+str(i)+'.png')
    onlyfiles = [ f[:-4] for f in listdir('res/NormalType') if f.endswith('.png') ]
    print(onlyfiles)
    for i in onlyfiles:
        AllBuy[i]=Image.open('res/NormalType/'+str(i)+'.png')
    onlyfiles = [ f[1:-4] for f in listdir('res/Game') if f.endswith('.png') ]
    print(onlyfiles)
    for i in onlyfiles:
        AllNumber[i]=Image.open('res/Game/G'+str(i)+'.png')
#         OTHER
    OtherIm['重叠s']=Image.open('重叠s.png')
    OtherIm['重叠sss']=Image.open('重叠sss.png')
    OtherIm['需求s']=Image.open('需求s.png')
    OtherIm['Over'] = Image.open('Over.png')
def GetMapInf():
    I = array(ImageGrab.grab())
    II = zeros((30, 60, 3))
    for i in range(30, 43):
        for j in range(40, 100):
            if ((I[i][j] == [246, 242, 150]).all() == True):
                II[i - 25][j - 40] = I[i][j]
    im = Image.fromarray(uint8(II))
    return im
def GetMapInf2():
    I = array(ImageGrab.grab())
    II = zeros((30, 100, 3))
    for i in range(28,41):
        for j in range(130, 196):
            II[i - 28][j - 130] = I[i][j]
    im = Image.fromarray(uint8(II))
    return im
def GetMission(I):
    # I = array(ImageGrab.grab())
    II=zeros((20,120,3))
    for i in range(545,545+120):
        for j in range(165,165+15):
            # print(I[i][j])
            if((I[j][i]==[254,254,0]).all()==True):
                II[j-165][i-545]=I[j][i]
    im = Image.fromarray(uint8(II))
    return im
def GetMissionDetail(I):
    # I = array(ImageGrab.grab())
    II=zeros((35,200,3))
    for i in range(535+Data.Global.Xp,535+200+Data.Global.Xp):
        for j in range(180,180+32):
            # print(I[i][j])
            if((I[j][i]==[0,254,0]).all()==True):
                II[j-180][i-535-Data.Global.Xp]=I[j][i]
    im = Image.fromarray(uint8(II))
    return im
def GetSingleWord(im):
    # im2 = im.crop((87, 0, 130, 14))
    start = -1
    end = 0
    I = array(im)
    while (end < 200):
        ok = -1
        for i in range(14):
            if (I[i][end] == [0, 254, 0]).all() == True:
                ok = 1
                break
        if (ok == 1):
            if (start == -1):
                start = end
        else:
            if start != -1:
                im2 = im.crop((start, 0, end, 14))
                im2.save('words/'+str(start) + "A" + str(end) + ".png")
                start = -1
        end += 1
def FindGoal(im):
    Goal=""
    start = -1
    end = 0
    I = array(im)
    conti=0
    while (end < 200):
        ok = -1
        for i in range(14):
            if (I[i][end] == [0, 254, 0]).all() == True:
                ok = 1
                break
        if (ok == 1):
            conti=0
            if (start == -1):
                start = end
        else:
            conti+=1
            if conti>5:
                # if Goal != '':
                #     print(Goal, conti)
                for p in range(len(Goal)+1):
                    for k in graph:
                        # print(Goal[:p],k)
                        if Goal[:p]==k:
                            if Goal[:p+1]=='清河镇外':
                                return Goal[:p+1]
                            if Goal[:p + 1] == '长安城外':
                                return Goal[:p + 1]
                            print("returnMap")
                            return Goal[:p]
                Goal=""
            if start != -1:
                im2 = im.crop((start, 0, end, 14))
                for j in AllWords:
                    if equal(AllWords[j],im2):
                        if j[:4]=='skip':
                            continue
                        Goal+=str(j)
                        # print(Goal)
                # im2.save('words/'+str(start) + "A" + str(end) + ".png")
                start = -1
        end += 1
    return "False"
def FindGoalXY(im):
    Goal=""
    start = -1
    end = 0
    I = array(im)
    conti=0
    State=0
    x=0
    y=0
    while (end < 200):
        ok = -1
        for i in range(14):
            if (I[i][end] == [0, 254, 0]).all() == True:
                ok = 1
                break
        if (ok == 1):
            conti=0
            if (start == -1):
                start = end
        else:
            conti+=1
            if conti>5:
                Goal=""
            if start != -1:
                im2 = im.crop((start, 0, end, 14))
                if equal(AllWords['左'],im2):
                    # print('equalway 1')
                    State=1
                if equal(AllWords['逗号'],im2):
                    State=2
                if equal(AllWords['右'],im2):
                    return x,y
                for i in range(10):
                    if equal(AllWords[str(i)],im2):
                        if State==1:
                            x*=10
                            x+=i
                        if State==2:
                            y*=10
                            y+=i
                        # print(i,x,y,'1')
                if State==0:
                    # print('Isleft')
                    if IsLeftNum(im2):
                        # print('equalway 2')
                        xx,yy=im2.size
                        # im2.show()
                        im2=im2.crop((3,0,xx,yy))
                        # im2.show()
                        State=1
                        for i in range(10):
                            if equal(AllWords[str(i)],im2):
                                if State==1:
                                    x*=10
                                    x+=i
                                # print(i, x, y,'2')
                # im2.save('words/'+str(start) + "A" + str(end) + ".png")
                start = -1
        end += 1
    if x==0 and y==0:
        return -1,-1
    return x,y
def GetFinalGoal(list):
    print('GetFinalGoal',list)
    if len(list)==0:
        return
    a=list[-1]
    if a not in NPC:
        return
    Num=0
    for i in NPC[a]:
        print(i)
    for i in NPC[a]:
        print(a,i)
        aa,bb,cc=NPC[a][i]
        if cc!=4:
            Num+=1
    if Num==1:
        for i in NPC[a]:
            aa, bb, cc = NPC[a][i]
            if cc != 4:
                list.append(i)
                GetFinalGoal(list)
    # while a in NPC and len(NPC[a])==1:
    #     for i in NPC[a]:
    #         list.append(i)
    #         a=i
def GetPerInf():
    I = array(ImageGrab.grab())
    II=zeros((20,60,3))
    for i in range(124,124+60):
        for j in range(434,434+20):
            # print(I[i][j])
            II[j-434][i-124]=I[j][i]
    im = Image.fromarray(uint8(II))
    return im
def GetPerInfWithX(x):
    I = array(ImageGrab.grab())
    II=zeros((20,60,3))
    for i in range(124-x,124+60-x):
        for j in range(434,434+20):
            # print(I[i][j])
            II[j-434][i-124+x]=I[j][i]
    im = Image.fromarray(uint8(II))
    return im
def GetF9():
    I = array(ImageGrab.grab())
    # II = zeros((20, 100, 3))
    time=0
    for i in range(57, 74):
        for j in range(60, 154):
            # II[i - 57][j - 60] = I[i][j]
            if(I[i][j]==[254,254,254]).all()==True:
                time+=1
                # print(i,j,time)
    # im = Image.fromarray(uint8(II))
    return time
def IsReach():
    # print(AllPer.keys())
    im=GetPerInf()
    for k in AllPer.keys():
        if(ImgEqual(im,AllPer[k])):
            return k
    return ""
def GetRandomPoint(x1,y1,x2,y2):
    pass
def MoveWindow2zero():
    A=getWindows()
    # for k,v in A:
    #     print(k,v)
    for k in A.keys():
        if ('神武3' in k):
            B = getWindow(k)
            a, b, *_ = B.get_position()
            print(a, b)
            if ((a, b) != (Data.Global.ZeroX, Data.Global.ZeroY)):
                B.move(Data.Global.ZeroX, Data.Global.ZeroY)
    B.set_foreground()
def MoveWindow2zeroName(name):
    A=getWindows()
    # for k,v in A:
    #     print(k,v)
    for k in A.keys():
        if (name in k):
            B = getWindow(k)
            a, b, *_ = B.get_position()
            print(a, b)
            if ((a, b) != (0, 0)):
                B.move(0, 0)
    B.set_foreground()
def MoveWindow2zeroOW():
    A=getWindows()
    # for k,v in A:
    #     print(k,v)
    for k in A.keys():
        if ('守望先锋' in k):
            B = getWindow(k)
            a, b, *_ = B.get_position()
            print(a, b)
            if ((a, b) != (0, 0)):
                B.move(0, 0)
    B.set_foreground()
def GetRaw(I):
    F = 0
    calc = 0
    TopRaw = -1
    for i in range(250, 10, -1):
        # print(i)
        calc = 0
        for j in range(380, 420):
            # if ((I[i][j] == array([130, 197, 192])).any() == False):
            if GetDiffOfColor(I[i][j],[130,197,192])>10:
                calc += 1
                if calc > 20:
                    F = 1
                    break
        if (F == 0):
            TopRaw = i + 1
            break
        F = 0
    # print('TopRaw:', TopRaw)

    calc = 0
    BottomRaw = -1
    for i in range(400, 620):
        # print(i)
        calc = 0
        for j in range(380, 420):
            # if ((I[i][j] == array([130, 197, 192])).any() == False):
            if GetDiffOfColor(I[i][j],[130,197,192])>10:
                calc += 1
                if calc > 20:
                    F = 1
                    break
        if (F == 0):
            BottomRaw = i - 1
            break
        F = 0
    # print('BottomRaw', BottomRaw)

    calc = 0
    LeftRaw = -1
    for j in range(250, 10, -1):
        calc = 0
        for i in range(280, 320):
            # print(i)
            # if ((I[i][j] == array([130, 197, 192])).any() == False):
            if GetDiffOfColor(I[i][j],[130,197,192])>10:
                calc += 1
                if calc > 20:
                    F = 1
                    break
        if (F == 0):
            LeftRaw = j + 1
            break
        F = 0
    # print('LeftRaw', LeftRaw)
    calc = 0
    RightRaw = -1
    for j in range(500, 820):
        calc = 0
        for i in range(280, 320):
            # print(i)
            # if ((I[i][j] == array([130, 197, 192])).any() == False):
            if GetDiffOfColor(I[i][j],[130,197,192])>10:
                calc += 1
                if calc > 20:
                    F = 1
                    break
        if (F == 0):
            RightRaw = j - 1
            break
        F = 0
    # print('RightRaw', RightRaw)
    return TopRaw,BottomRaw,LeftRaw,RightRaw
def ClickCoord(x,y):
    Data.Global.where=WhereIs()
    # MoveWindow2zero()
    # GetMouseXY()
    # SleepR(0.5,0.5)
    t=0
    RmoveRel(mouseX,400+50*ran(),mouseY,300+50*ran())
    im=ImageGrab.grab()
    I=array(im)
    while(IsTabNoI()==False):
        if IsCheckP(I):
            DealCheckP(I,im)
            SleepR(1,0.5)
        press('tab')
        t+=1
        if t>1:
            return
        SleepR(2,0.1)
    im=ImageGrab.grab()
    I=array(im)
    top,bottom,left,right=GetRaw(I)
    # for i in [top,bottom,left,right]:
    #     if i==-1:
    #         print("error")
    #         return
    if x>MapSize[Data.Global.where][0]-1:
        x=MapSize[Data.Global.where][0]-1
    if y>MapSize[Data.Global.where][1]-1:
        y=MapSize[Data.Global.where][1]-1
    RealClickX=left+(right-left)*1.0/MapSize[Data.Global.where][0]*x
    RealClickY=bottom-(bottom-top)*1.0/MapSize[Data.Global.where][1]*y
    print(RealClickX,RealClickY)
    press('tab')
    SleepR(1,0.1)
    # mouse2(RealClickX,RealClickY)
    if IsCheckP(I):
        DealCheckP(I,im)
        SleepR(1,0.5)
    RealMoveTo(RealClickX+ran(),RealClickY+ran())
    SleepR(0.5,0.1)
    press('tab')
    while (IsTabNoI() == False):
        press('tab')
        SleepR(1,0.1)
    # SleepR(1,0.5)
    click()
    # sleep(0.1)
    # click()
    SleepR(0.3,0.2)
    press('tab')
    # SleepR(1,0.1)
    t=0
    while(IsTabNoI()):
        press('tab')
        t=t+1
        if t>1:
            break
        SleepR(1.0,0.1)
def ClickCoordRel(x,y):
    sleep(1)
    MoveWindow2zero()
    sleep(2)
    if(IsTabNoI()==False):
        press('tab')
    while(IsTabNoI()==False):
        sleep(0.1)
    im=ImageGrab.grab()
    I=array(im)
    top,bottom,left,right=GetRaw(I)
    # for i in [top,bottom,left,right]:
    #     if i==-1:
    #         print("error")
    #         return
    RealClickX=left+(right-left)*1.0/MapSize[Data.Global.where][0]*x
    RealClickY=bottom-(bottom-top)*1.0/MapSize[Data.Global.where][1]*y
    print(RealClickX,RealClickY)
    # mouse2(RealClickX,RealClickY)
    a,b=position()
    moveRel(RealClickX-a,RealClickY-b)
    click()
    sleep(1)
    if(IsTabNoI()):
        press('tab')
def GetPath( start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                return path + [next]
                # yield path + [next]
            else:
                queue.append((next, path + [next]))
    return []
def IsTab(I):
    a=GetRaw(I)
    T=0
    for i in a:
        if(i==-1):
            T+=1
    if T>=2:
        return False
    return True
def IsTabNoI():
    im=ImageGrab.grab()
    I=array(im)
    a=GetRaw(I)
    T=0
    for i in a:
        if(i==-1):
            T+=1
    if T>=2:
        return False
    return True
# fight
# 784,532
# [14 66 68]

# talk
# 84,443
# [ 10 140 172]
# diff<10

# checkRotation
# 293+50,216
# [197 254 249]

# checkPuzzle
# 290+10,234+10
# [138,214,207]
def IsTalkBT(I):
    for i in range(470,471):
        for j in range(99,104):
            if(GetDiffOfColor(I[i][j],[10,140,172])>10):
                return False
    return True
def IsTalk(I):
    for i in range(443,446):
        for j in range(84,87):
            if(GetDiffOfColor(I[i][j],[10,140,172])>10):
                return False
    return True
def IsCheckP(I):
    for i in range(234,234+10):
        for j in range(290,290+10):
            if (I[i][j]==[138,214,207]).any()==False:
                return False
    return True
def IsFight(I):
    for i in range(555,555+2):
        for j in range(789,789+2):
            if (I[i][j]==[14,66,68]).any()==False:
                return False
    return True
def IsCheckR(I):
   for i in range(216,217):
       for j in range(293,293+40):
           if (I[i][j]==[197,254,249]).any()==False:
               return False
   return True
def IsCheckL(im):
    x1 = 311
    x2 = 427
    y1 = 216
    y2 = 225
    im = im.crop((x1, y1, x2, y2))
    I = array(im)
    for i in range(I.shape[0]):
        for j in range(I.shape[1]):
            if I[i][j][0] == 254 and I[i][j][1] == 254 and I[i][j][2] == 0:
                I[i][j] = [254, 254, 0]
            else:
                I[i][j] = [0, 0, 0]
    im = Image.fromarray(I)
    if equal(im,OtherIm['重叠s']):
        return True
    return False
# def IsMapChange(I):
#     pass
def IsVacant(number,I):
    TempI=zeros((3))
    Fix=[131,175,179]
    if(number==1):
        for i in range(378,381):
            for j in range(236,240):
                for p in range(3):
                    TempI[p]=max(I[j][i][p],Fix[p])-min(I[j][i][p],Fix[p])
                # 131,175,179
                if (TempI[0]>20 or TempI[1]>20 or TempI[2]>20):
                    # print(I[j][i])
                    return False
        return True
    if(number==2):
        for i in range(409,413):
            for j in range(237,241):
                # 131,175,179
                for p in range(3):
                    TempI[p]=max(I[j][i][p],Fix[p])-min(I[j][i][p],Fix[p])
                # 131,175,179
                if (TempI[0]>20 or TempI[1]>20 or TempI[2]>20):
                    # print(I[j][i])
                    return False
        return True
    if(number==3):
        for i in range(382,385):
            for j in range(257,260):
                for p in range(3):
                    TempI[p]=max(I[j][i][p],Fix[p])-min(I[j][i][p],Fix[p])
                # 131,175,179
                if (TempI[0]>20 or TempI[1]>20 or TempI[2]>20):
                    # print(I[j][i])
                    return False
        return True
    if(number==4):
        for i in range(405,408):
            for j in range(257,260):
                for p in range(3):
                    TempI[p]=max(I[j][i][p],Fix[p])-min(I[j][i][p],Fix[p])
                # 131,175,179
                if (TempI[0]>20 or TempI[1]>20 or TempI[2]>20):
                    # print(I[j][i])
                    return False
        return True
def IsVacantNew(number,I):
    TempI=zeros((3))
    Fix=[131,175,179]
    if(number==1):
        for i in range(395,396):
            for j in range(242,247):
                for p in range(3):
                    TempI[p]=max(I[j][i][p],Fix[p])-min(I[j][i][p],Fix[p])
                # 131,175,179
                if (TempI[0]>20 or TempI[1]>20 or TempI[2]>20):
                    # print(I[j][i])
                    return False
        return True
    if(number==2):
        for i in range(397,398):
            for j in range(242,247):
                # 131,175,179
                for p in range(3):
                    TempI[p]=max(I[j][i][p],Fix[p])-min(I[j][i][p],Fix[p])
                # 131,175,179
                if (TempI[0]>20 or TempI[1]>20 or TempI[2]>20):
                    # print(I[j][i])
                    return False
        return True
    if(number==3):
        for i in range(392,393):
            for j in range(252,256):
                for p in range(3):
                    TempI[p]=max(I[j][i][p],Fix[p])-min(I[j][i][p],Fix[p])
                # 131,175,179
                if (TempI[0]>20 or TempI[1]>20 or TempI[2]>20):
                    # print(I[j][i])
                    return False
        return True
    if(number==4):
        for i in range(400,401):
            for j in range(256,260):
                for p in range(3):
                    TempI[p]=max(I[j][i][p],Fix[p])-min(I[j][i][p],Fix[p])
                # 131,175,179
                if (TempI[0]>20 or TempI[1]>20 or TempI[2]>20):
                    # print(I[j][i])
                    return False
        return True
def GetPuzzleAns(im,pos):
    coord=zeros((4,4))
    coordM=zeros((4,2))
    coordM[0]=[397,230]
    coordM[1]=[395,230]
    coordM[2]=[397,252]
    coordM[3]=[395,252]
    coord[0]=[322,343,343,343]
    coord[1]=[462,343,483,343]
    coord[2]=[322,408,343,408]
    coord[3]=[463,408,484,408]

    coord2=zeros((4,4))
    coordM2=zeros((4,2))
    coordM2[0]=[375,252]
    coordM2[1]=[396,252]
    coordM2[2]=[375,250]
    coordM2[3]=[396,250]
    coord2[0]=[322,343,343,343]
    coord2[1]=[462,343,483,343]
    coord2[2]=[322,408,343,408]
    coord2[3]=[463,408,484,408]



    imM=im.crop((coordM[pos-1][0],coordM[pos-1][1],coordM[pos-1][0]+1,coordM[pos-1][1]+20))
    # imM.show()
    # imM.save('PuzTemp.png')
    imM2=im.crop((coordM2[pos-1][0],coordM2[pos-1][1],coordM2[pos-1][0]+20,coordM2[pos-1][1]+1))
    # imM2.show()
    I=array(imM)
    I2=array(imM2)
    difMin=-1
    Ans=-1

    if pos==1:
        for i in range(1,5):
            imT=im.crop((coord[i-1][2],coord[i-1][3],coord[i-1][2]+1,coord[i-1][3]+20))
            II=array(imT)
            dif=0
            for j in range(20):
                dif+=GetDiffOfColorNew(I[j][0],II[j][0])
            # imT=im.crop((coord[i-1][0],coord[i-1][1]+21,coord[i-1][0]+20,coord[i-1][1]+22))
            # II=array(imT)
            # for j in range(20):
            #     dif+=GetDiffOfColorNew(I2[0][j],II[0][j])
            if dif>difMin:
                difMin=dif
                Ans=i
            print(i,dif)
    if pos==3:
        for i in range(1,5):
            imT=im.crop((coord[i-1][2],coord[i-1][3],coord[i-1][2]+1,coord[i-1][3]+20))
            II=array(imT)
            dif=0
            for j in range(20):
                dif+=GetDiffOfColorNew(I[j][0],II[j][0])
            # imT=im.crop((coord[i-1][0],coord[i-1][1],coord[i-1][0]+20,coord[i-1][1]+1))
            # II=array(imT)
            # for j in range(20):
            #     dif+=GetDiffOfColorNew(I2[0][j],II[0][j])
            if dif>difMin:
                difMin=dif
                Ans=i
            print(i,dif)
    if pos==2:
        for i in range(1,5):
            imT=im.crop((coord[i-1][0],coord[i-1][1],coord[i-1][0]+1,coord[i-1][1]+20))
            II=array(imT)
            # imT.show()
            dif=0
            for j in range(20):
                dif+=GetDiffOfColorNew(I[j][0],II[j][0])
            # imT=im.crop((coord[i-1][0],coord[i-1][1],coord[i-1][0]+20,coord[i-1][1]+1))
            # II=array(imT)
            # # imT.show()
            # for j in range(20):
            #     dif+=GetDiffOfColorNew(I2[0][j],II[0][j])
            if dif>difMin:
                difMin=dif
                Ans=i
            print(i,dif)
    if pos==4:
        for i in range(1,5):
            imT=im.crop((coord[i-1][0],coord[i-1][1],coord[i-1][0]+1,coord[i-1][1]+20))
            II=array(imT)
            dif=0
            for j in range(20):
                dif+=GetDiffOfColorNew(I[j][0],II[j][0])
            # imT=im.crop((coord[i-1][0],coord[i-1][1]+21,coord[i-1][0]+20,coord[i-1][1]+22))
            # II=array(imT)
            # for j in range(20):
            #     dif+=GetDiffOfColorNew(I2[0][j],II[0][j])
            if dif>difMin:
                difMin=dif
                Ans=i
            print(i,dif)

    # if pos==4 or pos==2:
    #     for i in range(1,5):
    #         imT=im.crop((coord[i-1][0],coord[i-1][1],coord[i-1][0]+1,coord[i-1][1]+20))
    #         imT.save('PuzTemp'+str(i)+'.png')
    #         II=array(imT)
    #         dif=0
    #         for j in range(20):
    #            dif+=GetDiffOfColor(I[j][0],II[j][0])
    #         # print(i,dif)
    #         if dif<difMin:
    #             difMin=dif
    #             Ans=i
    # if pos==1 or pos==3:
    #     for i in range(1,5):
    #         imT=im.crop((coord[i-1][2],coord[i-1][3],coord[i-1][2]+1,coord[i-1][3]+20))
    #         II=array(imT)
    #         dif=0
    #         for j in range(20):
    #             dif+=GetDiffOfColor(I[j][0],II[j][0])
    #         if dif<difMin:
    #             difMin=dif
    #             Ans=i
    return Ans
def GetDiffOfColor(c1,c2):
    temp=0
    for i in range(3):
        temp=temp+max(c1[i],c2[i])-min(c1[i],c2[i])
    return temp
def GetDiffOfColorNew(c1,c2):
    temp=0
    for i in range(3):
        if max(c1[i],c2[i])-min(c1[i],c2[i])>50:
            return 0
    return 1
def FindImgInImg(imM,imS,stx,enx,sty,eny):
    I=array(imM)
    II=array(imS)
    if stx==enx==0:
        eny=I.shape[0]
        enx=I.shape[1]
    for i in range(eny-sty-(II.shape[0])):
        for j in range(enx-stx-(II.shape[1])):
            fl=0
            for k in range(II.shape[0]):
                for l in range(II.shape[1]):
                    if GetDiffOfColor(I[sty+i+k][stx+j+l],II[k,l])>0:
                        fl=1
                        break
                if fl==1:
                    break
            if fl==0:
                print('success',j+stx,i+sty)
                return j+stx,i+sty
    return -1,-1
def FindImgInImgWithLoss(imM,imS,stx,enx,sty,eny,loss):
    I=array(imM)
    II=array(imS)
    print('Finding')
    # print(II.shape)
    for i in range(eny-sty-(II.shape[0])):
        for j in range(enx-stx-(II.shape[1])):
            fl=0
            for k in range(II.shape[0]):
                for l in range(II.shape[1]):
                    if GetDiffOfColor(I[sty+i+k][stx+j+l],II[k,l])>loss:
                        # print('wrong1')
                        fl=1
                        break
                if fl==1:
                    break
            if fl==0:
                print('success')
                return j+stx,i+sty
    # print('wrong2')
    return -1,-1
def equal(im1, im2):
    if im1.size!=im2.size:
        return False
    return ImageChops.difference(im1, im2).getbbox() is None
def ran():
    return (random.random()-0.5)*3.0
def DealCheckP(I,im):
    for i in range(1,5):
        if IsVacant(i,I):
            pos=i
            print(i)
            k=GetPuzzleAns(im,pos)
            print("ans:"+str(k))
            # RealMoveTo(100,100)
            if k==1:
                RmoveRel(mouseX,330+ran(),mouseY,354+ran())
            if k==2:
                RmoveRel(mouseX,472+ran(),mouseY,352+ran())
            if k==3:
                RmoveRel(mouseX,334+ran(),mouseY,421+ran())
            if k==4:
                RmoveRel(mouseX,472+ran(),mouseY,418+ran())
            click()
            break
def GetLAnsByHaoi(x,y):
    im=ImageGrab.grab((x-10,y-10,(800-x)+10,(800-y)+10))
    # im.show()
    buffer = BytesIO()
    im.save(buffer, format="JPEG")
    ba = base64.b64encode(buffer.getvalue())
    host = 'sv14.haoi23.net:8009'
    random.seed()
    randi = random.randint(1, 1e9)
    dataA = {
        'userstr': 'fjbisk001|D69E7F1F818C49A1',
        'gameid': '5001',
        'timeout': 50,
        'rebate': 'D69E7F1F818C49A1',
        'DaiLi': 'haoi',
        'kou': 0,
        'ver': 'web2',
        'key': randi,
        'Img': ba,
    }
    host = 'http://' + host
    headersA = {'Content-Type': 'application/x-www-form-urlencoded'}
    r = requests.post(host + u'/UploadBase64.aspx', data=dataA, headers=headersA)

    dataB = {
        'id': r.text,
        'r': randi,
    }
    print(r.text)
    for i in range(8):
        sleep(2)
        r = requests.post(host + u'/GetAnswer.aspx', data=dataB, headers=headersA)
        print(r.text)
        if r.text!="":
            break
    return r.text
def IsCheckLNew(im):
    x1 = 11
    x2 = 427
    y1 = 116
    y2 = 425
    im = im.crop((x1, y1, x2, y2))
    I = array(im)
    for i in range(I.shape[0]):
        for j in range(I.shape[1]):
            if I[i][j][0] == 254 and I[i][j][1] == 254 and I[i][j][2] == 0:
                I[i][j] = [254, 254, 0]
            else:
                I[i][j] = [0, 0, 0]
    im = Image.fromarray(I)
    # im.show()
    x,y=FindImgInImg(im,OtherIm['重叠sss'],0,0,0,0)
    if x!=-1:
        return x,y
    return -1,-1
    # if equal(im,OtherIm['重叠s']):
    #     return True
    # return False
def GetConfig():
    cfg = ConfigParser()
    cfg.read('setting.ini')
    # print(cfg.read('setting.ini'))
    # print(cfg.sections())
    x = cfg.get('setting', 'StartX')
    Data.Global.ZeroX=int(x)
    x = cfg.get('setting', 'StartY')
    Data.Global.ZeroY=int(x)
def IsLeftNum(im1):
    im2=AllWords['左']
    x,y=im1.size
    im1=im1.crop((0,0,3,y))
    # im1.show()
    # im2.show()
    # SleepR(3,0)
    if equal(im1,im2):
        return True
    return False
    # im2=AllWords['左']
    # I1=array(im1)
    # I2=array(im2)
    # for i in range(I2.shape[0]):
    #     for j in range(I2.shape[1]):
    #         if (I1[i][j]==I2[i][j]).any()==False:
    #             return False
    # return True
def IsAllOver():
    RmoveRel(0,417+100*ran(),0,465+30*ran())
    cokey('alt','y')
    print('cokey1')
    T=0
    while IsAltY()!=True:
        T+=1
        SleepR(2,0.5)
        if T>4:
            cokey('alt','y')
            print('cokey2')
            T=0

    im=ImageGrab.grab()
    x,y=FindImgInImg(im,OtherIm['Over'],0,0,0,0)

    cokey('alt','y')
    print('cokey3')
    T=0
    while IsAltY():
        T+=1
        SleepR(2,0.5)
        if T>4:
            print('cokey4')
            cokey('alt','y')
            T=0
    if x!=-1:
        return False
    return True
def IsAltY():
    im=ImageGrab.grab()
    I=array(im)
    if GetDiffOfColor(I[108][321],[153,222,216])<20:
        return True
    return False
def ESCconfirm():
    while GetTypeOfTask(ImageGrab.grab()) == -1:
        press('esc')
        SleepR(1, 0.5)
def ReStart():
    print('ReStart')
    RmoveRel(0,100,0,100)
    Data.Global.STime=0
    MoveWindow2zero()
    SleepR(2,0)
    # GetMouseXY()
    while IsReStartMenu()==False:
        press('esc')
        SleepR(1,0.1)
    press('esc')
    SleepR(1,0.1)
    GetMouseXY()
    # RmoveRel(0,316+ran()*5,0,377+ran())
    # click()
    # while WhereIs()!='':
    #     SleepR(0.3,0.2)
    # while WhereIs()=='':
    #     SleepR(0.8,0.7)
    #     press('enter')
    # GetMouseXY()
    print('ReStartFinish')
def RealReStart():
    print('RealReStart')
    Data.Global.STime=0
    RmoveRel(0,100,0,100)
    MoveWindow2zero()
    SleepR(2,0)
    # GetMouseXY()
    while IsReStartMenu()==False:
        press('esc')
        SleepR(1,0.1)
    RmoveRel(0,316+ran()*5,0,377+ran())
    click()
    while WhereIs()!='':
        SleepR(0.3,0.2)
    while WhereIs()=='':
        SleepR(0.8,0.7)
        press('enter')
    GetMouseXY()
    print('RealReStartFinish')
def GetMouseXY():
    print('GetMouseXY')
    a,b=position()
    Data.Global.mouseX=a
    Data.Global.mouseY=b
def ProtectError(Time):
    whe=WhereIs()
    if whe !='' and whe!=Data.Global.ProtectWhere:
        Time=0
        Data.Global.ProtectWhere=whe
    Time+=1
    if Time>600:
        for i in range(100):
            print('ProtectError')
        while True:
            SleepR(1,1)
    global timer
    timer=threading.Timer(1.0,ProtectError,Time)
    timer.start()
def GetGamePos():
    stx=135
    sty=31
    T=0
    Stage=1
    x=0
    y=0
    for i in range(100):
        if T!=-1:
            T+=1
        # print(T)
        if T>10:
            Stage+=1
            T=-1
        if Stage==3:
            # if x==0 or y==0:
            #     return -1,-1
            return x,y
        nx=stx+i
        ny=sty
        im=ImageGrab.grab((nx,ny,nx+6,ny+12))
        # im.show()
        I=array(im)
        for i in range(I.shape[0]):
            for j in range(I.shape[1]):
                if (I[i][j]==[254,254,254]).any()==False:
                    I[i][j]=[0,0,0]
        im=Image.fromarray(I)
        NowNum=IdentifyNumber(im)
        if NowNum!=-1:
            if Stage==1:
                x*=10
                x+=NowNum
                T=0
            if Stage==2:
                y*=10
                y+=NowNum
                T=0
    return -1,-1
def SpecialRunInQH(type):
    MainX=400
    MainY=325
    # LG
    if type==1:
        TargetX=110
        TargetY=63
    # AL
    if type==2:
        TargetX=115
        TargetY=25
    if type==3:
        TargetX=0
        TargetY=0
    T=0
    while(WhereIs()=='' or WhereIs()=='清河镇外'):
        T+=1
        if T>=15:
            RealReStart()
            while CheckAllState(True):
                print("CHECKinSp")
            T=0
        Nx, Ny = GetGamePos()
        print(Nx,Ny)
        while Ny==-1:
            Nx,Ny=GetGamePos()
            print(Nx,Ny)
            print('GetGamePosError')
        Qx=TargetX-Nx
        Qy=Ny-TargetY
        if Nx>=100 and Ny<=32 and type==2:
            print('Type2Trans')
            TransX,TransY=FindTrans(2)
            if TransX==-1:
                SleepR(1,1)
            else:
                RmoveRel(0,TransX,0,TransY-40)
                click()
        elif Nx>=100 and 58<Ny<70 and type==1:
            print('Type1Trans')
            TransX,TransY=FindTrans(1)
            if TransX==-1:
                SleepR(1,1)
            else:
                RmoveRel(0,TransX,0,TransY-40)
                click()
        else:
            RunX,RunY=GetRunNum(Qx,Qy)
            RmoveRel(0,MainX+RunX,0,MainY+RunY)
            PAUSE=0
            mouseDown()
            mouseUp()
            PAUSE=0.1
            SleepR(0.1, 0.1)
            click(button='right')
        SleepR(0.1,0.2)
        while CheckAllState(True):
            print("CHECKinSp")
    print('SpecialFinish')
def FindTrans(type):
    im=ImageGrab.grab()
    I=array(im)
    Xnum=0
    Xsum=0
    Ynum=0
    Ysum=0
    stx=0
    sty=0
    if type==2:
        # stx=I.shape[0]/2
        sty=int(I.shape[1]/2)
    for i in range(stx,I.shape[0]):
        for j in range(sty,I.shape[1]):
            if I[i][j][0]!=221 or I[i][j][1]!=81 or I[i][j][2]!=88:
                I[i][j]=[0,0,0]
            else:
                Xnum+=1
                Xsum+=j
                Ynum+=1
                Ysum+=i
    if Xnum>10:
        return Xsum/Xnum,Ysum/Ynum
    else:
        return -1,-1

    # im=Image.fromarray(I)
    # im.show()
def GetRunNum(Qx,Qy):
    AllQ=sqrt(Qx*Qx+Qy*Qy)
    if AllQ>20:
        AllRun=400
    else:
        AllRun=20*AllQ
    RunX=AllRun*Qx/(Qx+Qy)
    RunY=AllRun*Qy/(Qx+Qy)
    if RunX>270:
        RunX=270
    if RunY>220:
        RunY=220
    return RunX+20*ran(),RunY+ran()*20
def IdentifyNumber(im):
    for i in range(10):
        if equal(im,AllNumber[str(i)]):
            return i
    return -1
def ReGetMouseXY():
    ReStart()
def IsReStartMenu():
    # 474，342
    # 155，226，219
    im=ImageGrab.grab()
    I=array(im)
    for i in range(342,352):
        if I[i][474][0]==155 and I[i][474][1]==226 and I[i][474][2]==219:
            return True
    return False
# def ReZC():
#     cokey('alt','c')
#     RmoveRel(0,243,0,325)
#     click()
#     SleepR(0.5,0.2)
#     press('esc')
