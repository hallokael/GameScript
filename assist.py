from PIL import Image
from numpy import *
I = array(Image.open('res/1234.jpg'))
# im=Image.open('res/1234.jpg')
# im.show()
print(I[100][100])
print(I.shape)
for i in range(100,200):
    for j in range(100,200):
        I[i][j]=[200 ,0, 0]
im = Image.fromarray(uint8(I))
im.save('assist.jpg')

