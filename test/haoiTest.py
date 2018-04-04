import base64
import requests
from PIL import Image
from io import BytesIO
import random
import time
im=Image.open("1234.jpg")
buffer = BytesIO()
im.save(buffer, format="JPEG")
ba=base64.b64encode(buffer.getvalue())
host='sv14.haoi23.net:8009'
# sv14.haoi23.net:8009
#SendFile(MyUserStr, GameID, FilePath, TimeOut, LostPoint, BeiZhu)
#{Host}/UploadBase64.aspx
random.seed()
randi=random.randint(1,1e10)
dataA={
    'userstr':'fjbisk001|D69E7F1F818C49A1',
    'gameid':'5001',
    'timeout':50,
    'rebate':'D69E7F1F818C49A1',
    'DaiLi':'haoi',
    'kou':0,
    'ver':'web2',
    'key':randi,
    'Img':ba,
}
host='http://'+host
headersA={'Content-Type':'application/x-www-form-urlencoded'}
r = requests.post(host+u'/UploadBase64.aspx',data=dataA,headers=headersA)

dataB = {
    'id': r.text,
    'r': randi,
}
print(r.text)
while 1:
    time.sleep(2)
    r = requests.post(host + u'/GetAnswer.aspx', data=dataB, headers=headersA)
    print(r.text)
