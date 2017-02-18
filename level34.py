import urllib
import math
from PIL import Image
level_url = "http://kohsamui:thailand@www.pythonchallenge.com/pc/rock/beer.html"
png_url = "http://kohsamui:thailand@www.pythonchallenge.com/pc/rock/beer2.png"
pngfile = urllib.urlopen(png_url)
png = Image.open(pngfile)
data = list(png.getdata())
colors = png.getcolors()
histogram = png.histogram()
for i in range(33):
    c1 = colors[-(1 + i * 2)][1]
    c2 = colors[-(2 + i * 2)][1]
    datatemp1 = data
    datatemp2 = [c == c1 or c == c2 for c in data]
    datatemp3 = [c == c1 for c in data]
    datatemp4 = [c == c2 for c in data]
    n = math.sqrt(sum(histogram[:c1+1]))
    n = int(n)
    assert (len(datatemp1) == n * n)
    imagetemp1 = Image.new("L", (n, n))
    imagetemp1.putdata(datatemp1)
    imagetemp1.save("./level34/" + str(i) + "_1.bmp")

    imagetemp2 = Image.new("1", (n, n))
    imagetemp2.putdata(datatemp2)
    imagetemp2.save("./level34/" + str(i) + "_2.bmp")

    imagetemp3 = Image.new("1", (n, n))
    imagetemp3.putdata(datatemp3)
    imagetemp3.save("./level34/" + str(i) + "_3.bmp")

    imagetemp4 = Image.new("1", (n, n))
    imagetemp4.putdata(datatemp4)
    imagetemp4.save("./level34/" + str(i) + "_4.bmp")

    datatemp5 = filter(lambda x: x != c1 and x != c2, data)
    data = datatemp5

# gremlins (alphabet in squares)
