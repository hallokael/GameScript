from Common import *
for i in range(1,14):
    im=Image.open('check'+str(i)+'.png')
    # im.show()
    im.crop((365,225,430,280)).save('temp'+str(i)+'.png')

# from Common import *
# sleep(2)
# im=ImageGrab.grab()
# im.save('check14.png')
# # im.crop((395,231,396,252)).save('checktest.png')
# # main pic
# # im.crop((395,230,396,252)).save('b.png')
# # pic 1
# # im.crop((322,343,323,365)).save("aa.png")
# # pic 2
# #im.crop((322,408,323,430)).save("a2.png")
# # pic 3