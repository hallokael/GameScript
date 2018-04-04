# for python 3.x use 'tkinter' rather than 'Tkinter'
import tkinter as tk
import time
from pyautogui import *
import tkinter.messagebox as messagebox
from time import sleep
from Common import *
from PIL import Image,ImageTk
from PIL import ImageGrab
from numpy import *
tempim=Image.open("yyy.jpg")
class App():
    def __init__(self):
        self.root = tk.Tk()
        self.label = tk.Label(text="")
        self.label.pack()
        self.label2 = tk.Label(text="")
        self.label2.pack()
        self.root.geometry("100x90")
        path = "1234.jpg"
        im=Image.open(path)
        # im.show()
        # Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
        self.img = ImageTk.PhotoImage(im)
        # print(img.width())
        # The Label widget is a standard Tkinter widget used to display a text or image on the screen.
        self.panel = tk.Label(image=self.img)
        # self.panel.pack(side = "left", fill = "both", expand = "yes")
        self.panel.pack(side = "left")
        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        # now = time.strftime("%H:%M:%S")
        # self.label.configure(text=now)
        # print("before grab")
        self.I = array(ImageGrab.grab())
        self.II = array(tempim)
        # print("grab")
        a, b = position()
        self.label.configure(text=str(a)+"  "+str(b))
        # print("mouse",a,b)
        c, d, e = self.I[b][a]
        # print("before write")
        for i in range(47):
            for j in range(169):
                self.II[i][j] = [c, d, e]
        # print(type(self.I))
        self.im = Image.fromarray(uint8(self.II))
        self.img = ImageTk.PhotoImage(self.im)
        self.panel['image'] = self.img
        self.label2.configure(text=str(c)+" "+str(d)+" "+str(e))
        self.root.after(10, self.update_clock)

app=App()