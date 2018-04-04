from pyautogui import *
from tkinter import *
import tkinter.messagebox as messagebox
from time import sleep
from Common import *
from PIL import Image,ImageTk
from PIL import ImageGrab
from numpy import *
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.update_clock()
    def update_clock(self):
        # now = time.strftime("%H:%M:%S")
        # print(now)
        print("Next")
        I = array(ImageGrab.grab())
        a, b = position()
        c, d, e = I[a][b]
        for i in range(100):
            for j in range(100):
                I[i][j] = [c, d, e]
        im = Image.fromarray(uint8(I))
        self.panel['image'] = im
        self.after(1000, self.update_clock)
    def createWidgets(self):
        path = "1234.jpg"
        im=Image.open(path)
        # im.show()
        # Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
        self.img = ImageTk.PhotoImage(im)
        # print(img.width())
        # The Label widget is a standard Tkinter widget used to display a text or image on the screen.
        self.panel = Label(self, image=self.img)
        self.panel.pack()
        # self.nameInput = Entry(self)
        # self.nameInput.pack()
        # self.alertButton = Button(self, text='Hello', command=self.goStart)
        # self.alertButton.pack()

    # def hello(self):
    #     sleep(1)
    #     mouse2(600,600)
    # def goStart(self):
    #     sleep(1)
    #     cokey('alt','e')

app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()



# I = array(Image.open('res/1234.jpg'))
# # im=Image.open('res/1234.jpg')
# # im.show()
# print(I[100][100])
# print(I.shape)
# for i in range(100,200):
#     for j in range(100,200):
#         I[i][j]=[200 ,0, 0]
# im = Image.fromarray(uint8(I))
# im.save('assist.jpg')