from pyautogui import *
from tkinter import *
import tkinter.messagebox as messagebox
from time import sleep
from Common import *
import Data.Global

# AllImage={}
class Application(Frame):
    # Method=0
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        print("Init")

    def createWidgets(self):
        self.TestText = Label(self, text='Sleep')
        self.TestText.pack()
        self.slp = Entry(self)
        self.slp.pack()

        self.TestText = Label(self, text='StartX')
        self.TestText.pack()
        self.stx = Entry(self)
        self.stx.pack()

        self.TestText = Label(self, text='StartY')
        self.TestText.pack()
        self.sty = Entry(self)
        self.sty.pack()

        self.TestText = Label(self, text='EndX')
        self.TestText.pack()
        self.enx = Entry(self)
        self.enx.pack()

        self.TestText = Label(self, text='EndY')
        self.TestText.pack()
        self.eny = Entry(self)
        self.eny.pack()

        v=IntVar()
        v.set(1)

        def r1():
            self.Method=1
        def r2():
            self.Method=2
        def r3():
            self.Method=3
        def r4():
            self.Method=4
        self.Ra1G=Radiobutton(self, text='green',variable=v,value=1,command=r1)
        self.Ra1G.pack()
        self.Ra1Y=Radiobutton(self, text='yellow',variable=v,value=2,command=r2)
        self.Ra1Y.pack()
        self.RalW=Radiobutton(self, text='white',variable=v,value=3,command=r3)
        self.RalW.pack()
        self.RalN=Radiobutton(self, text='no',variable=v,value=4,command=r4)
        self.RalN.pack()
        self.alertButton = Button(self, text='crop', command=self.test)
        self.alertButton.pack()
        self.alertButton = Button(self, text='AllPs', command=self.test2)
        self.alertButton.pack()
    def test(self):
        mb=1
        if self.Method==1:
            M=[0,254,0]
        if self.Method==2:
            M=[254,254,0]
        if self.Method==3:
            M=[254,254,254]
        if self.Method==4:
            mb=0
        slp=int(self.slp.get())
        stx=int(self.stx.get())
        enx=int(self.enx.get())
        sty=int(self.sty.get())
        eny=int(self.eny.get())
        sleep(slp)
        im=ImageGrab.grab((stx,sty,enx,eny))
        if mb==1:
            I=array(im)
            for i in range(I.shape[0]):
                for j in range(I.shape[1]):
                    for k in range(3):
                        if I[i][j][k]!=M[k]:
                            I[i][j]=[0,0,0]
                            break
            im=Image.fromarray(I)
        im.save('crop.png')
        # if mb==1:
    def test2(self):
        slp=int(self.slp.get())
        sleep(slp)
        im=ImageGrab.grab()
        im.save('AllPs.png')
app = Application()
app.master.title('Hello World')
app.mainloop()
