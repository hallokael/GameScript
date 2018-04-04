# -*- coding: cp936 -*-
from ctypes import *
from time import *
import struct

# RGBԪ�ط�Χ(0-1)
def hex_to_rgb(hex_str):
    int_tuple = struct.unpack('BBB', bytes.fromhex(hex_str))
    return tuple([val for val in int_tuple])

#����winapi
sleep(2)
gdi32 = windll.gdi32
user32 = windll.user32

#��ȡ���
hdc = user32.GetDC(None)
#��ȡָ�����ص���ɫ
olda = clock()
for i in range(100):
    c = gdi32.GetPixel(hdc,500+i,500)
a=clock()
print(a - olda)
print(c)
c/=256
print(c%256)
c/=256
print(c%256)
c/=256
print(hex_to_rgb('7BF5BE'))
