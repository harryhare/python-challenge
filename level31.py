import urllib
import re
from PIL import Image
level_url = "http://repeat:switch@www.pythonchallenge.com/pc/ring/yankeedoodle.html"
csv_url = "http://repeat:switch@www.pythonchallenge.com/pc/ring/yankeedoodle.csv"
csv_file = urllib.urlopen(csv_url)
rawdata = csv_file.read()
float_pattern = re.compile(r"\d\.\d+")
rawdata = re.findall(float_pattern, rawdata)
data = [int(float(i)*256) for i in rawdata]
#data = [float(i) for i in data]
n = len(data)
height = n
width = 1
for i in range(2,n // 2+1):
    if n % i == 0:
        height = i
        break
assert n % height == 0
width = n // height
image1 = Image.new("L", (width, height))
image1.putdata(data)
#image1.show()#noise
image2 = Image.new("L", (height, width))# L bmp ;F tiff # http://infohost.nmt.edu/tcc/help/pubs/pil.pdf
image2.putdata(data)
image2 = image2.transpose(Image.ROTATE_90)
image2 = image2.transpose(Image.FLIP_TOP_BOTTOM)
image2.show()
image2.save("./level31/level31.bmp")
# In bmp:
# n=str(x[i])[5]
#  +str(x[i+1])[5]
#  +str(x[i+2])[6]
txt = ""
for i in range(0,n-2,3):
    x = int(rawdata[i][5] + rawdata[i+1][5] + rawdata[i+2][6])
    txt += chr(x)
print(txt)
#grandpa