from PIL import Image
from numpy import *

# img = Image.open('qwe.png')
# img = img.convert("RGBA")
# datas = img.getdata()
# newData = list()
# for item in datas:
#     if item[0] > 250 and item[1] > 250 and item[2] > 250:
#         newData.append((255, 255, 255, 0))
#     else:
#         newData.append(item)
#
# img.putdata(newData)
# img.save('qwer.png', "PNG")
I=array(Image.open('qwe.png'))
r=50
for i in range(101):
    for j in range(101):
        if((i-r)*(i-r)+(j-r)*(j-r)>=2200 and (i-r)*(i-r)+(j-r)*(j-r)<=2450):
            I[i][j]=[254,0,0,254]
        else:
            I[i][j]=[254,254,254,0]
im=Image.fromarray(I)
im.show()
im.save('100x100.png')
