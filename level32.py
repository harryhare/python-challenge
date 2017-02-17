from PIL import Image
import urllib
level_url = "http://repeat:switch@www.pythonchallenge.com/pc/ring/grandpa.html"
level_url2 = "http://kohsamui:thailand@www.pythonchallenge.com/pc/rock/grandpa.html"
gif_url = "http://kohsamui:thailand@www.pythonchallenge.com/pc/rock/mandelbrot.gif"
giffile = urllib.urlopen(gif_url)
gif = Image.open(giffile)
creatfile = True
data9 = []
if creatfile:
    new = gif.copy()
    left = 0.34
    top = 0.57
    width = 0.036
    height = 0.027
    iterations = 128
    for ii in range(640):
        for ij in range(480):
            realpart = left + width / 640 * ii
            imagepart = top + height - height / 480 * (ij+1)
            z = realpart + imagepart * 1j
            t = 0
            for ik in range(128):
                t = t * t + z
                if abs(t) >= 2.0:
                    break
            new.putpixel((ii, ij), ik)
            d = ik - gif.getpixel((ii,ij))
            if(d!=0):
                data9.append(d)
    new.show()
    new.save("./level32/new.gif")
    gif.show()
    print(len(data9))#data9 and date6 are different!!!
else:
    new = Image.open("./level32/new.gif")
data1 = gif.getdata()
data2 = new.getdata()
assert len(data1) == len(data2)
data3 = []
data4 = []
data5 = []
for i in range(len(data1)):
    t1 = data1[i]
    t2 = data2[i]
    if t1 != t2:
        data5.append(i)
        data3.append(t1)
        data4.append(t2)
data6 = [abs(data3[i] - data4[i]) for i in range(len(data4))]
data7 = [data3[i]+data4[i] for i in range(len(data4))]
diffstring = False
if diffstring:
    for i in [3, 4, 6, 7]:
        print("data"+str(i)+":")
        filename = "./level32/" + str(i) + ".txt"
        filex = open(filename, "w")
        exec "temp=data" + str(i)
        exec "print temp"
        exec "string" + str(i) + "=''.join([chr(j) for j in temp])"
        exec "filex.write(string" + str(i) + ")"
        filex.close()
diffimage5 = False
if diffimage5:
    diff5 = Image.new("1", gif.size)
    blank = [0] * 640 * 480
    for i in data5:
        blank[i] = 1
    diff5.putdata(blank)
    diff5.save("diff5.bmp")#nothing

data6 = filter(lambda x: x != 13, data6)
n = len(data6)
def minfactor(x):
    for i in range(2, x / 2):
        if x % i == 0:
            return i
height = minfactor(n)
width = n / height
diff6_1 = Image.new("L", (width,height))
diff6_1.putdata(data6)
#diff6_1.show()
diff6_1.save("./level32/diff6_1.bmp")
diff6_2 = Image.new("L", (height, width))
diff6_2.putdata(data6)
diff6_2.save("./level32/diff6_2.bmp")
#diff6_2.show()
data7 = map(lambda x: 0 if x == 3 else 1, data6)
finalimage = Image.new("1", diff6_2.size)
finalimage.putdata(data7)
finalimage.save("./level32/final.bmp")
#Arecibo message
#arecibo