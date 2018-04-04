from Common import *
# MoveWindow2zero()
sleep(2)
I = array(ImageGrab.grab())
II=zeros((20,60,3))
for i in range(124,124+60):
    for j in range(434,434+20):
            # print(I[i][j])
            II[j-434][i-124]=I[j][i]
im = Image.fromarray(uint8(II))
im.save("大唐境外-女儿国.png")
# im.show()
# sleep(3)
# im=Image.open(Name+".png")
# II = array(im)
# for i in range(30,43):
#     for j in range(40,100):
#             print(II[i-25][j-40])