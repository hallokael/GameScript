from Common import *
# sleep(2)
# im=[]
# for i in range(100):
#     im1=ImageGrab.grab()
#     im.append(im1)
# t=0
# for i in im:
#     t+=1
#     i.save('asd'+str(t)+'.png')
# im=ImageGrab.grab()
# im.save('家具屏风.png')
# im.crop((395,231,396,252)).save('checktest.png')
# main pic
# im.crop((395,230,396,252)).save('b.png')
# pic 1
# im.crop((322,343,323,365)).save("aa.png")
# pic 2
#im.crop((322,408,323,430)).save("a2.png")
# pic 3
# sleep(2)
# pos=-1
# im1=ImageGrab.grab()
# im1.save('check28.png')
# I=array(im1)
# for i in range(1,5):
#     if IsVacant(i,I):
#         pos=i
#         print(i)
#         k=GetPuzzleAns(im1,pos)
#         print("ans:"+str(k))
#         break

pos=-1
for j in range(1,27):
    im1=Image.open('check'+str(j)+'.png')
    I=array(im1)
    for i in range(1,5):
        if IsVacantNew(i,I):
            pos=i
            print(i,j)
            k=GetPuzzleAns(im1,pos)
            print("ans:"+str(k))
            break


# im1=Image.open('check'+'11'+'.png')
# I=array(im1)
# for i in range(1,5):
#     if IsVacant(i,I):
#         print(i)
#         k=GetPuzzleAns(im1,i)
#         print("ans:"+str(k))
#         break
