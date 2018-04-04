from Common import *
sleep(2)
MoveWindow2zero()
im=ImageGrab.grab()
I=array(im)
im2=GetMissionDetail(I)
im2.save('jsd.png')
GetSingleWord(im2)
# im2.show()
