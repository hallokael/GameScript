from Common import *
sleep(3)
time=0
# for i in range(20):
#     time+=1
#     print(time)
#     im=ImageGrab.grab()
#     im.show()
#     im.save("uuuu"+str(time)+".png")
# MoveWindow2zeroOW()
ti=0
while(True):
    ti+=1
    im=ImageGrab.grab()
    I=array(im)
    II=zeros((50,150,3))
    for i in range(525,575):
        time=0
        for j in range(850,1000):
            # II[i-200][j-200]=I[i][j]
            if(I[i][j][0]>210 and I[i][j][1]<150 and I[i][j][2]<150 and max(I[i][j][1],I[i][j][2])-min(I[i][j][1],I[i][j][2])<30 ):
            # if(I[i][j][0]>230 and I[i][j][1]<90 and I[i][j][2]<90 and max(I[i][j][1],I[i][j][2])-min(I[i][j][1],I[i][j][2])<30 ):
                # print(I[i][j],time)
                # print(i,j)
                II[i-525][j-850]=I[i][j]
                time+=1
            # elif I[i][j][0]>200:
            #     II[i-200][j-200]=I[i][j]
            #     time+=1
    im = Image.fromarray(uint8(I))
    print(ti)
    im.show()
    im.save('testT123.png')
    break
    # print("123")
        # if time>10:
        #     print("YES")
        # else:
        #     print("NO")
    # im.show()
    # sleep(5)
    # im.show()
    # im.save("test2.png")
# for i in range(20):
#     sleep(1)
#     click()
