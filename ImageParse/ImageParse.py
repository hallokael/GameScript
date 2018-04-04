from Common import *
im=Image.open('temp1.png')
im2=im.crop((87,0,130,14))
start=-1
end=0
I=array(im)
while(end<200):
    ok=-1
    for i in range(14):
        if (I[i][end]==[0,254,0]).all()==True:
            ok=1
            break
    if(ok==1):
        if(start==-1):
            start=end
    else:
        if start!=-1:
            im2=im.crop((start,0,end,14))
            im2.save(str(start)+"A"+str(end)+".png")
            start=-1
    end+=1

