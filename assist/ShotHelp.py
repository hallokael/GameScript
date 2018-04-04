from Common import *
Data.Global.ZeroY=4
while(1):
    Name = input('Capture: ')
    MoveWindow2zero()
    sleep(2)
    I = array(ImageGrab.grab())
    II=zeros((30,60,3))
    for i in range(30,43):
        for j in range(40,100):
            if((I[i][j]==[246 ,242, 150]).all()==True):
                print(I[i][j])
                II[i-25][j-40]=[246,242,150]
    im = Image.fromarray(uint8(II))
    im.save(Name+".png")
    # sleep(3)
    # im=Image.open(Name+".png")
    # II = array(im)
    # for i in range(30,43):
    #     for j in range(40,100):
    #             print(II[i-25][j-40])