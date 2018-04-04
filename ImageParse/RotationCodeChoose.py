from Common import *
# 220,350,233,391
# 352,350,365,391
# 477,350,490,391
# 604,350,617,391
im=Image.open('Rotation/asd1.png')
I=[]
I.append(array(im.crop((220,350,233,391))))
I.append(array(im.crop((352,350,365,391))))
I.append(array(im.crop((477,350,490,391))))
I.append(array(im.crop((604,350,617,391))))
print (I)
Run=zeros((4))
for i in range(2,100):
    im=Image.open('Rotation/asd'+str(i)+'.png')
    II=[]
    II.append(array(im.crop((220,350,233,391))))
    II.append(array(im.crop((352,350,365,391))))
    II.append(array(im.crop((477,350,490,391))))
    II.append(array(im.crop((604,350,617,391))))
    for k in range(4):
        TemNum=0
        fl=0
        for i in range(II[1].shape[0]):
            for j in range(II[1].shape[1]):
                Dif=GetDiffOfColor(I[k][i][j],II[k][i][j])
                if Dif>100:
                    TemNum+=1
                    if TemNum>10:
                        Run[k]+=1
                        fl=1
                        break
            if fl==1:
                break
    I=II
    print(Run)
