from pyautogui import *
from tkinter import *
import tkinter.messagebox as messagebox
from time import sleep
from Common import *
AllImage={}
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.OpenAllImage()
    def OpenAllImage(self):
        onlyfiles = [ f[:-4] for f in listdir('res') if f.endswith('.png') ]
        print(onlyfiles)
        for i in onlyfiles:
            AllImage[i]=Image.open('res/'+str(i)+'.png')
    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='move', command=self.move2)
        self.alertButton.pack()
        self.alertButton = Button(self, text='Press', command=self.goStart)
        self.alertButton.pack()
        self.alertButton = Button(self, text='move2coord', command=self.coord)
        self.alertButton.pack()
        self.alertButton = Button(self, text='Where', command=self.WhereIs)
        self.alertButton.pack()
    def move2(self):
        sleep(1)
        # mouse2(600,600)
        MoveWindow2zero()
    def goStart(self):
        sleep(1)
        # cokey('alt','e')
        press('tab')
    def coord(self):
        sleep(1)
        MoveWindow2zero()
        sleep(2)
        # '长安城':[550, 325],
        top,bottom,left,right=GetRaw()
        for i in [top,bottom,left,right]:
            if i==-1:
                print("error")
                return
        RealClickX=left+(right-left)*1.0/550.0*100
        RealClickY=bottom-(bottom-top)*1.0/325.0*100
        print(RealClickX,RealClickY)
        press('tab')
        sleep(2)
        mouse2(RealClickX,RealClickY)
        sleep(0.5)
        press('tab')
        sleep(1)
        click()
    def WhereIs(self):
        im=GetMapInf()
        # print(im.getcolors())
        for k in AllImage.keys():
            if(equal(AllImage[k],im)):
            # if(im==AllImage[k]):
                print(k)
            # else:
                # print(k,'no')
                # print(AllImage[k].getcolors())
                # AllImage[k].show()
                # im.save("ii1.jpg")
                # AllImage[k].save("ii2.jpg")
        # for i in range(5):
        #     moveRel(50,0,2)
        #     click()
        #     print(position())
        #     sleep(2)
app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()