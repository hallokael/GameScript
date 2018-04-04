from Common import *
MoveWindow2zero()
sleep(2)
im=ImageGrab.grab()
im.save("重叠2.png")


# im=Image.open('需求.png')
# im.crop((392,339,396,343)).save('需求s.png')

# im1=Image.open('需求.png')
# im2=Image.open('需求s.png')
# print(FindImgInImg(im1,im2,360,630,260,600))

# im=Image.open('xn.png')
# im=im.crop((267,339,512,356))
# I=array(im)
# for i in range(I.shape[0]):
#     for j in range(I.shape[1]):
#         if (I[i][j]!=[254,254,254]).any()==True:
#             I[i][j]=[0,0,0]
# im=Image.fromarray(I)
# im.save('xnet.png')
# im.save('运镖.png')
# im.save('跑镖结束.png')
# fight
# 784,532
# [14 66 68]

# talk
# 84,443
# [ 10 140 172]
# diff<10

# checkRotation
# 293+50,216
# [197 254 249]

# checkPuzzle
# 290+10,234+10
# [138,214,207]

# im=Image.open('check1.png')
# I=array(im)
# for i in range(234,234+10):
#     for j in range(290,290+10):
#         print(I[i][j])

# 烹饪
# (630,290,650,300)


# im=Image.open('15级烹饪.png')
# # im=im.crop((500,200,700,400))
# im=im.crop((630,290,650,300))
# I=array(im)
# for i in range(I.shape[0]):
#     for j in range(I.shape[1]):
#         if I[i][j][0]==254 and I[i][j][1]==254 and I[i][j][2]==254:
#             print(I[i][j])
#         else:
#             I[i][j]=[0,0,0]
# im=Image.fromarray(I)
# im.save('words/烹饪.png')

