from PIL import Image
import urllib
level_url = "http://repeat:switch@www.pythonchallenge.com/pc/ring/bell.html"
png_url = "http://repeat:switch@www.pythonchallenge.com/pc/ring/bell.png"

pngfile = urllib.urlopen(png_url)
png = Image.open(pngfile)
(red, green, blue) = png.split()
data = green.getdata()
n = len(data)
points = []
data2 = [0]*n
data3 = ""
data4 = ""
data5 = ""
data6 = ""
for i in range(0, n, 2):
    if abs(data[i] - data[i + 1]) != 42:
        points.append((i % 640, i // 640))
        data2[i] = 1
        data3 += chr(data[i])
        data4 += chr(data[i+1])
        data5 += chr(abs(data[i] - data[i+1]))
        data6 += chr((data[i] + data[i+1]) % 256)
new = Image.new("1", png.size)
new.putdata(data2)
new.show()
print(data3)
print(data4)
print(data5)#whodunnit().split()[0]
print(data6)

#thesamet
#bit4
#guido