from pyautogui import *
from tkinter import *
import tkinter.messagebox as messagebox
from time import sleep
from Common import *
import Data.Global
# AllImage={}
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        print("Init")
        OpenAllImage()
        GetConfig()
    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.TestText=Label(self,text='jdsklafjaklwejwea')
        self.TestText.pack()
        self.alertButton = Button(self, text='move', command=self.move2)
        self.alertButton.pack()
        self.alertButton = Button(self, text='Press', command=self.goStart)
        self.alertButton.pack()
        self.alertButton = Button(self, text='move2coord', command=self.coord)
        self.alertButton.pack()
        self.alertButton = Button(self, text='Where', command=self.WhereIs)
        self.alertButton.pack()
        self.alertButton = Button(self, text='Run', command=self.Run)
        self.alertButton.pack()
        self.alertButton = Button(self, text='FinalRun', command=self.FinalRun)
        self.alertButton.pack()
        self.alertButton = Button(self, text='NewRun', command=self.NewRun)
        self.alertButton.pack()
        self.alertButton = Button(self, text='IsTab', command=self.IsTabP)
        self.alertButton.pack()
        self.alertButton = Button(self, text='test', command=self.test)
        self.alertButton.pack()
        self.alertButton = Button(self, text='test2', command=self.test2)
        self.alertButton.pack()
    def test(self):
        sleep(2)
        GetMouseXY()
        ReZC()
        # ReStart()
        # im=ImageGrab.grab()
        # im.save('rt2.png')
        # im=Image.open('rt.png')
        # # I=array(im)
        # # print(IsCheckLNew(im))
        # im=im.crop((93,215,103,225))
        # # im=ImageGrab.grab((93,215,103,225))
        # I=array(im)
        # for i in range(I.shape[0]):
        #     for j in range(I.shape[1]):
        #         if I[i][j][0] == 254 and I[i][j][1] == 254 and I[i][j][2] == 0:
        #             I[i][j] = [254, 254, 0]
        #         else:
        #             I[i][j] = [0, 0, 0]
        # im = Image.fromarray(I)
        # im.save("重叠sss.png")
        # GetLAnsByHaoi()
        # RmoveRel(0,300,0,300)
        # im=ImageGrab.grab()
        # print(IsCheckL(im))
        # BuyWeaponAndCommit()
        # RealMoveTo(400,400)
        # moveTo(400,400,2,)
        # UseFlag('f6',2,2)
        # for i in range(100):
        #     moveRel(10,10)
        #     sleep(0.1)
        # im=ImageGrab.grab()
        # I=array(im)
        # a,b=GetLightOne(I)
        # print(a,b)
        # BuyWeaponAndCommit()
        # self.TestText['text']+=('dsjkalfa\n')
        # im=GetPerInfWithX(12)
        # im.save("test.png")
        # im1=GetMapInf2()
        # # im111.show()
        # sleep(3)
        # im2=GetMapInf2()
        # I1=array(im1)
        # I2=array(im2)
        # # for i in range(I2.shape[0]):
        # #     for j in range(I2.shape[1]):
        # #         if((I1[i][j]==I2[i][j]).any()==False):
        # #             print(I1[i][j],I2[i][j])
        # # print(equal(im1,im2))
        # # print(im1==im2)
        # print(ImgEqual(im1,im2))
        # while (1):
        #     sleep(3)
        #     print("waiting for not change")
        #     im222 = GetMapInf2()
        #     if im222 == im111:
        #         break
        #     else:
        #         im111 = im222
        # im1=Image.open('test.png')
        # im2=Image.open('长安城-大唐国境.png')
        # I1=array(im1)
        # I2=array(im2)
        # for i in range(I1.shape[0]):
        #     for j in range(I1.shape[0]):
        #         if((I1[i][j]==I2[i][j]).any()==False):
        #             print(I1[i][j],I2[i][j])
        # print(equal(im1,im2))
    def test2(self):
        sleep(2)
        TabChange()
        # im=GetPerInf()
        # im.save('sssss.png')
        # RealMoveTo(425,37)
        # for i in range(4):
        #     moveRel(0,100)
        #     sleep(0.5)
        # moveRel(0,65)
        # sleep(1)
        # moveRel(-33,40)
    def move2(self):
        sleep(1)
        MoveWindow2zero()
    def goStart(self):
        sleep(1)
        press('tab')
    def coord(self):
        ClickCoord(100,100)
    def WhereIs(self):
        print(WhereIs())
        # im=GetMapInf()
        # for k in AllImage.keys():
        #     if(equal(AllImage[k],im)):
        #         print(k)
    def NewRun(self):
        start=WhereIs()
        end=ReadGreen()
        InitRun(start,end)
        NowSeq=0
        path=Data.Global.path
        while(NowSeq<len(path)-1):
            
            while(True):
                Data.Global.pause=0
                if(IsMapChange()):
                    break
                sleep(0.12)
                IsTalk()
                sleep(0.14)
                IsCheckR()
                sleep(0.11)
                IsTab()
                sleep(0.15)

                if Data.Global.pause==0:
                    break
            if(IsMapChange()):
                for i in range(len(path)):
                    print(i,path[i])
                    if(path[i]==Data.Global.where):
                        NowSeq=i
                        break
            else:
                RunToNext()
            sleep(0.12)
    def FinalRun(self):
        if datetime.datetime.now().month > 3:
            return
        MainRun()
    def Run(self):
        start='长安城'
        end='云隐阁'
        Data.Global.where=WhereIs()
        Data.Global.path=GetPath(start,end)
        path=Data.Global.path
        NowSeq=0
        while(NowSeq<len(path)-1):
            oldpos=WhereIs()
            im111=GetMapInf2()
            print("NowSeq",NowSeq)
            F=0
            for i in NPC[path[NowSeq]].keys():
                if i==path[NowSeq+1]:
                    a,b,c=NPC[path[NowSeq]][i]
                    print(i)
                    F=1
                    break
            if(F==1):
                ClickCoord(a,b)
                print(a,b,c)
                if(c==1):
                    while(True):
                        Ans=IsReach()
                        if(Ans!=""):
                            print("reach")
                            sleep(0.5)
                            a1,b1,c1=NPC[path[NowSeq]][path[NowSeq]+'-'+path[NowSeq+1]]
                            mouse2(a1,b1)
                            click()
                            mouse2(a1,b1+20)
                            click()
                            break
                        else:
                            print('未找到图')
                            sleep(1)
            else:
                print('error')
            print("afterReach")
            while(1):
                sleep(3)
                print("waiting for not change")
                im222=GetMapInf2()
                if ImgEqual(im111,im222):
                    break
                else:
                    im111=im222
            Data.Global.where=WhereIs()
            if(c==2):
                a2,b2,c2=NPC[path[NowSeq]][path[NowSeq]+'2']
                mouse2(a2,b2)
                sleep(1)
                click()
                while(True):
                    Ans=IsReach()
                    if(Ans!=""):
                        print("reach")
                        sleep(0.5)
                        a3,b3,c3=NPC[path[NowSeq]][path[NowSeq]+'-'+path[NowSeq+1]]
                        # mouse2(a3,b3)
                        # click()
                        # mouse2(a3,b3+20)
                        # click()
                        moveRel(a3-a2,b3-b2,2)
                        click()
                        moveRel(0,20,0.1)
                        click()
                        break
                    else:
                        print('未找到图')
                        sleep(1)
            # for i in range(10):
            #     if(oldpos!=WhereIs()):
            #         nowpos=WhereIs()
            #         Data.Global.where=nowpos
            #         break
            #     else:
            #         sleep(1)
            for i in range(len(path)):
                print(i,path[i])
                if(path[i]==Data.Global.where):
                    NowSeq=i
                    break
    def IsTabP(self):
        print(IsTab())
app = Application()
app.master.title('Hello World')
app.mainloop()