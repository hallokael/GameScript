from Common import *
# x1 = 203
# x2 = x1+10
# y1 = 239
# y2 = y1+10
# OpenAllImage()
# im=Image.open('重叠2.png')
# # print(IsCheckLNew(im))
# im = im.crop((x1, y1, x2, y2))
# I = array(im)
# for i in range(I.shape[0]):
#     for j in range(I.shape[1]):
#         if I[i][j][0] == 254 and I[i][j][1] == 254 and I[i][j][2] == 0:
#             I[i][j] = [254, 254, 0]
#         else:
#             I[i][j] = [0, 0, 0]
# im = Image.fromarray(I)
# im.save('重叠ss.png')
sleep(2)
x1 = 614 + Data.Global.Xp
x2 = 665 + Data.Global.Xp
y1 = 166
y2 = 178
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
im.save('type4.png')
# im.save('whyyyyy.png')
