from pyautogui import *
from tkinter import *
import tkinter.messagebox as messagebox
from time import sleep
from Common import *
from PIL import Image,ImageTk
from PIL import ImageGrab
from numpy import *
#This creates the main window of an application
def a():
    pass
window = Tk()
window.title("Join")
# window.geometry("300x300")
window.configure(background='grey')

path = "1234.jpg"

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = Label(window, image = img)

#The Pack geometry manager packs widgets in rows or columns.
panel.pack()

# alertButton = Button(window, text='Hello', command=a)
# alertButton.pack()

#Start the GUI
window.mainloop()
while(1):
    sleep(1)
    print("Next")
    I = array(ImageGrab.grab())
    a,b=position()
    c,d,e=I[a][b]
    for i in range(100):
        for j in range(100):
            I[i][j]=[c,d,e]
    im = Image.fromarray(uint8(I))
    panel['image']=im
