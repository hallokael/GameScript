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
class App():
    def __init__(self):
        self.root = tk.Tk()
        self.label = tk.Label(text="")
        self.label.pack()
        self.root.geometry("100x50")
        self.nameInput = tk.Entry(self)
        self.nameInput.pack()
        self.alertButton = tk.Button(self, text='Hello', command=self.goStart)
        self.alertButton.pack()
        self.root.mainloop()


app=App()