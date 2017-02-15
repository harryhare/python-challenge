import urllib
from PIL import Image
import bz2
import keyword
levelurl = "http://butter:fly@www.pythonchallenge.com/pc/hex/speedboat.html"
gifurl = "http://butter:fly@www.pythonchallenge.com/pc/hex/zigzag.gif"
giffile = urllib.urlopen(gifurl)
gif = Image.open(giffile)
data = gif.getdata()
data = list(data)
data2 = [0]*len(data)
palette = gif.getpalette()
palette = palette[::3]
for i in range(len(data)):
    data2[i] = palette[data[i]]
gif2 = Image.new("1", gif.size)
gif2.putdata(data2)
data3 = [0]*len(data)
l1 = ""
l2 = ""
for i in range(len(data)-1):
    if data2[i] != data[i+1]:
        data3[i] = 1
        l1 += chr(data2[i])
        l2 += chr(data[i+1])
data3[-1] = 1
gif2.putdata(data3)
gif2.show()
print(len(l1), l1)
print(len(l2), l2)
plain = bz2.decompress(l2)
print(plain)
counts={}
for i in plain.split():
    if not keyword.iskeyword(i):
        #print(i)
        if(counts.has_key(i)==False):
            counts[i]=0
        counts[i]+=1
print(counts)
#{'../ring/bell.html': 406, 'switch': 345, 'repeat': 366}