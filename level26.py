import urllib
from PIL import Image,ImageDraw
import wave
level_url="http://butter:fly@www.pythonchallenge.com/pc/hex/lake.html"
url_head="http://butter:fly@www.pythonchallenge.com/pc/hex/lake"

def getwav():
    try:
        for i in range(0,30):
            file=urllib.urlopen(url_head+str(i)+".wav")
            if(file.getcode()==200):
                out=open("./level26/lake"+str(i)+".wav","wb")
                out.write(file.read())
                out.close()
            file.close()
    except:
        print("can not save file lake '"+str(i)+".wav'")

def getimg():
    wholeimg=Image.new("RGB",(300,300))
    for i in range(1,26):
        wavfile=wave.open("./level26/lake"+str(i)+".wav","rb")
        data=wavfile.readframes(wavfile.getnframes())
        img=Image.frombytes("RGB",(60,60),data)
        #img.save("./level26/lake"+str(i)+".jpg")
        wholeimg.paste(img,((i-1)%5*60,(i-1)//5*60))
    wholeimg.save("./level26/whole.jpg")
getimg()
#decent