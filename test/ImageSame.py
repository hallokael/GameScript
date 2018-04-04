from Common import *
im=Image.open("方寸山.jpg")
im1=Image.open("昆仑山.jpg")
time=0
while(time<100):
    print(im==im1)
    time+=1
    print(time)