from Common import *
# sleep(2)
# x1=311
# x2=427
# y1=216
# y2=225
# # im=ImageGrab.grab()
# # im=ImageGrab.grab((x1,y1,x2,y2))
# im=Image.open('重叠1.png')
# im=im.crop((x1,y1,x2,y2))
# I=array(im)
# for i in range(I.shape[0]):
#     for j in range(I.shape[1]):
#         if I[i][j][0]==254 and I[i][j][1]==254 and I[i][j][2]==0:
#             I[i][j]=[254,254,0]
#         else:
#             I[i][j]=[0,0,0]
# im=Image.fromarray(I)
# im.show()
# im.save('重叠s.png')
# 614 665 166 178

# x1 = 618
# x2 = 665
# y1 = 165
# y2 = 177
# im=Image.open('tttttttt.png')
# # im.show()
# im = im.crop((x1, y1, x2, y2))
# I = array(im)
# for i in range(I.shape[0]):
#     for j in range(I.shape[1]):
#         if I[i][j][0] == 254 and I[i][j][1] == 254 and I[i][j][2] == 0:
#             I[i][j] = [254, 254, 0]
#         else:
#             I[i][j] = [0, 0, 0]
# im = Image.fromarray(I)
# im.save('TTT.png')
sleep(2)
Xp=6
Yp=0
x1 = 614+Xp
x2 = 665+Xp
y1 = 166+Yp
y2 = 178+Yp
im=ImageGrab.grab((x1,y1,x2,y2))
# im = im.crop((x1, y1, x2, y2))
I = array(im)
for i in range(I.shape[0]):
    for j in range(I.shape[1]):
        if I[i][j][0] == 254 and I[i][j][1] == 254 and I[i][j][2] == 0:
            I[i][j] = [254, 254, 0]
        else:
            I[i][j] = [0, 0, 0]
im = Image.fromarray(I)
im.save('ZZZZZZ.png')


