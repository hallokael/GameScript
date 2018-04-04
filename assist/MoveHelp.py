from Common import *
im=Image.open('testCA.png')
I=array(im)
# I = array(ImageGrab.grab())
II = zeros((30, 60, 3))
for i in range(30, 43):
    for j in range(40, 100):
        if ((I[i][j] == [246, 242, 150]).all() == True):
            print(I[i][j])
            II[i - 25][j - 40] = [246, 242, 150]
im = Image.fromarray(uint8(II))
im.save('Q长安.png')
