from time import sleep
from PIL import ImageGrab
from PIL import Image
import random
sleep(2)
im=ImageGrab.grab()
a=random.randint(1,1e9)
im.save('IMG/shot'+str(a)+'.png')
