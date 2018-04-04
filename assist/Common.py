from pyautogui import *
# import pyautogui
import random
from PIL import ImageGrab
from PIL import Image
from numpy import *
from time import *
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
import sys,os
from configparser import ConfigParser
AllImage={}
AllPer={}
AllWords={}
AllPlace={}
AllShop={}
AllTask={}
AllBuy={}
OtherIm={}
random.seed()
def MainRun():
    # pyautogui.PAUSE=0
    MoveWindow2zero()
    sleep(2)
    a,b=position()
    Data.Global.mouseX=a
    Data.Global.mouseY=b
    while True:
        while CheckAllState():
            print("CHECK")
            pass
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
                    a,b=NPCsp[i]
                    RealMoveTo(a+ran(),b+ran())
                    click()
                    SleepR(1.5,0.5)
def TotalGoal(im):
    type=GetTypeOfTask(im)
    print("type:")
    print(type)
    if 0<type<3:
        Goal,xx,yy=GetGoal()
        if Goal != "False":
            Data.Global.x=xx
            Data.Global.y=yy
            Data.Global.path=GetPath('长安城',Goal)
            if(xx!=-1 and yy!=-1):
                Data.Global.path.append('tempPos')
            else:
                GetFinalGoal(Data.Global.path)
            print (Data.Global.path,xx,yy)
    # elif type==3:
    #     BuyWeaponAndCommit()
    elif type==3:
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
        GetNewTask()
        SleepR(2,0.5)
        im=ImageGrab.grab()
        TotalGoal(im)
        # Goal,xx,yy=GetGoal()
        # if Goal != "False":
        #     Data.Global.x=xx
        #     Data.Global.y=yy
        #     Data.Global.path=GetPath('长安城',Goal)
        #     GetFinalGoal(Data.Global.path)
        #     if(xx!=-1 and yy!=-1):
        #         Data.Global.path.append('tempPos')
        #     print (Data.Global.path,xx,yy)
def FindTypeOfBuy():
    l=WhereBuy()
    if l==[]:
        return 1
    else:
        return 2
def GetNewTask():
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
    # RmoveRel(0,x-Data.Global.mouseX,0,y-Data.Global.mouseY)
    x=int(x)
    y=int(y)
    while(True):
        # moveTo(x,y)
        # SleepR(0.5,0.5)
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
        BuyWeapon()
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
    print('BuyAndCommit Over')
def BuyNormalAndCommit():
    while(IsBuySuccess()==False):
        BuyNormal()
    ReturnBT()
    x,y,z=NPC['长安城']['镖头']
    ClickCoord(x,y)
    print('BuyNormalAndCommit Finish')
def RmoveRel(stx,enx,sty,eny):
    print('RmoveRel')
    # print(pyautogui.PAUSE)
    print(Data.Global.mouseX,enx,Data.Global.mouseY,eny)
    x=enx-Data.Global.mouseX
    y=eny-Data.Global.mouseY
    de=random.random()*2+2
    while(True):
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
        print(enx,eny,a,b,x,y)
        # sleep(0.01)
        if x==0 and y==0:
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
        print(i)
        if equal(AllTask[i],im):
            # im.show()
            # AllTask[i].show()
            return int(i)
    return -1
def BuyWeapon():
    while(True):
        a=WhereBuy()
        if a!=[]:break
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
                        x,y=NPC[i][j]
                        print(i,j)
                        ClickCoord(x,y)
                        WaitForNotMove()
                    while(True):
                        print("Buy3")
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
                                            press('esc')
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
            break
    print('Buy Over')
def BuyNormal():
    while True:
        kind=WhereBuyN()
        if kind!=-1:
            break
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
            press('esc')
            SleepR(1,0.5)
            break

    print("BuyNormalFinish")
def WhereBuy():
    l=[]
    RealMoveTo(586+Data.Global.Xp+ran(),187+ran() )
    click()
    SleepR(1,1)
    # 554,255,767,388
    im=ImageGrab.grab((644+Data.Global.Xp,327,783+Data.Global.Xp,386))
    I=array(im)
    for i in range(I.shape[0]):
        for j in range(I.shape[1]):
            if I[i][j][0]==254 and I[i][j][1]==254 and I[i][j][2]==0:
                pass
            else:
                I[i][j]=[0,0,0]
    im=Image.fromarray(I)
    for i in AllPlace:
        a,b=FindImgInImg(im,AllPlace[i],0,783-644,0,386-327)
        if a!=-1 :
            l.append(i)
            print('find '+i)
    RealMoveTo(634+Data.Global.Xp+ran()*5,315+ran()*5 )
    # moveTo(634,315)
    click()
    return l
def WhereBuyN():
    l=-1
    # moveTo(586,187)
    RealMoveTo(586+Data.Global.Xp+ran(),187+ran() )
    click()
    SleepR(1,1)
    im=ImageGrab.grab((554+Data.Global.Xp,255,767+Data.Global.Xp,388))
    I=array(im)
    for i in range(I.shape[0]):
        for j in range(I.shape[1]):
            if I[i][j][0]==254 and I[i][j][1]==254 and I[i][j][2]==254:
                pass
            else:
                I[i][j]=[0,0,0]
    im=Image.fromarray(I)
    for i in AllBuy:
        a,b=FindImgInImg(im,AllBuy[i],0,767-554,0,388-255)
        if a!=-1 :
            l=int(i)
    # moveTo(634,315)
    RealMoveTo(634+Data.Global.Xp+ran()*5,315+ran()*5 )
    click()
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
def CheckAllState():
    im=ImageGrab.grab()
    I=array(im)
    if IsTab(I):
        print('IsTab')
        press('tab')
        r=random.random()*1+2
        sleep(r)
        return True
    if IsCheckR(I):
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
        print('IsCheckL')
        k=GetLAnsByHaoi(x,y)
        k=int(k)
        RmoveRel(mouseX,x+(800-2*x)/8*(1+2*(k-1))+ran(),mouseY,367+ran())
        # if k==2:
        #     # 1 156
        #     RmoveRel(mouseX,310+ran(),mouseY,361+ran())
        # if k==3:
        #     RmoveRel(mouseX,472+ran(),mouseY,359+ran())
        # if k==4:
        #     RmoveRel(mouseX,632+ran(),mouseY,361+ran())
        r=random.random()*1+2
        sleep(r)
        return True
    # if IsCheckL(im):
    #     print('IsCheckL')
    #     k=GetLAnsByHaoi()
    #     k=int(k)
    #     if k==1:
    #         RmoveRel(mouseX,157+ran(),mouseY,367+ran())
    #     if k==2:
    #         RmoveRel(mouseX,310+ran(),mouseY,361+ran())
    #     if k==3:
    #         RmoveRel(mouseX,472+ran(),mouseY,359+ran())
    #     if k==4:
    #         RmoveRel(mouseX,632+ran(),mouseY,361+ran())
    #     r=random.random()*1+2
    #     sleep(r)
    #     return True
    if IsCheckP(I):
        print('IsCheckP')
        DealCheckP(I,im)
        r=random.random()*1+2
        sleep(r)
        return True
    if IsFight(I):
        print('IsFight')
        if Data.Global.FightDel==0:
            cokey('ctrl','a')
            Data.Global.FightDel=20
        Data.Global.FightDel-=1
        Data.Global.PlusNeed=True
        r=random.random()*1+2
        sleep(r)
        return True
    if IsTalk(I):
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
            RmoveRel(mouseX,349,mouseY,380)
            click()
        r=random.random()*1+2
        sleep(r)
        return True
    if Data.Global.PlusNeed:
        PlusHP()
        Data.Global.PlusNeed=False
    TotalGoal(im)
    return False
def PlusHP():
    RealMoveTo(643+ran()*5,35+ran()*2)
    SleepR(0.1,0.05)
    click(button='right')
    RealMoveTo(644+ran()*5,45+ran()*2)
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
                print(i,j,I[j][i])
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
    a=-1
    b=-1
    c=-1
    if next=='tempPos':
        a=Data.Global.x
        b=Data.Global.y
    else:
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
    print(I2.shape[0],I2.shape[1])
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
#         OTHER
    OtherIm['重叠s']=Image.open('重叠s.png')
    OtherIm['重叠ss']=Image.open('重叠ss.png')
    OtherIm['需求s']=Image.open('需求s.png')
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
                Goal=""
            if start != -1:
                im2 = im.crop((start, 0, end, 14))
                for j in AllWords:
                    if equal(AllWords[j],im2):
                        if j[:4]=='skip':
                            continue
                        Goal+=str(j)
                        print(Goal)
                        for k in graph:
                            if Goal==k:
                                return Goal
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
                # im2.save('words/'+str(start) + "A" + str(end) + ".png")
                start = -1
        end += 1
    if x==0 and y==0:
        return -1,-1
    return x,y
def GetFinalGoal(list):
    if len(list)==0:
        return
    a=list[-1]
    while a in NPC and len(NPC[a])==1:
        for i in NPC[a]:
            list.append(i)
            a=i
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
    print('TopRaw:', TopRaw)

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
    print('BottomRaw', BottomRaw)

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
    print('LeftRaw', LeftRaw)
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
    print('RightRaw', RightRaw)
    return TopRaw,BottomRaw,LeftRaw,RightRaw
def ClickCoord(x,y):
    Data.Global.where=WhereIs()
    # MoveWindow2zero()
    SleepR(0.5,0.5)
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
    SleepR(1,0.1)
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
        SleepR(2.0,0.1)
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
    for i in a:
        if(i==-1):
            return False
    return True
def IsTabNoI():
    im=ImageGrab.grab()
    I=array(im)
    a=GetRaw(I)
    for i in a:
        if(i==-1):
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
    for i in range(532,532+2):
        for j in range(784,784+2):
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
    imM=im.crop((coordM[pos-1][0],coordM[pos-1][1],coordM[pos-1][0]+1,coordM[pos-1][1]+20))
    imM.save('PuzTemp.png')
    I=array(imM)
    difMin=10e10
    Ans=-1
    if pos==4 or pos==2:
        for i in range(1,5):
            imT=im.crop((coord[i-1][0],coord[i-1][1],coord[i-1][0]+1,coord[i-1][1]+20))
            imT.save('PuzTemp'+str(i)+'.png')
            II=array(imT)
            dif=0
            for j in range(20):
               dif+=GetDiffOfColor(I[j][0],II[j][0])
            # print(i,dif)
            if dif<difMin:
                difMin=dif
                Ans=i
    if pos==1 or pos==3:
        for i in range(1,5):
            imT=im.crop((coord[i-1][2],coord[i-1][3],coord[i-1][2]+1,coord[i-1][3]+20))
            II=array(imT)
            dif=0
            for j in range(20):
                dif+=GetDiffOfColor(I[j][0],II[j][0])
            if dif<difMin:
                difMin=dif
                Ans=i
    return Ans
def GetDiffOfColor(c1,c2):
    temp=0
    for i in range(3):
        temp=temp+max(c1[i],c2[i])-min(c1[i],c2[i])
    return temp
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
                print('success')
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
    im.show()
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
    x,y=FindImgInImg(im,OtherIm['重叠ss'],0,0,0,0)
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
    Data.Global.ZeroX=x
    x = cfg.get('setting', 'StartY')
    Data.Global.ZeroY=x
