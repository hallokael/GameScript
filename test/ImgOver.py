from Common import *
# SleepR(2,1)
# im=ImageGrab.grab()
# im.save('iiiwww.png')
im=Image.open('iiiwww.png')
im=im.crop((820,170,840,190))
im.save('Over.png')