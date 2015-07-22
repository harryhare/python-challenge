import PIL.Image
import urllib
import re
#import PIL.Image
level_url = 'http://www.pythonchallenge.com/pc/def/oxygen.html'
png_url = 'http://www.pythonchallenge.com/pc/def/oxygen.png'
png_name = 'oxygen.png'

image_file = urllib.urlopen(png_url)
image = PIL.Image.open(image_file)
y=43#43-51
x_begin=0
x_end=609
step=7
str=''
for x in range(x_begin,x_end,step):
    point=image.getpixel((x,y))
    if(point[0]!=point[1] or point[1]!=point[2]):
        print('Error',"x="+x,"y="+y)
    str+=chr(point[0])
print(str)

pattern=re.compile('\d+')
temp=pattern.findall(str)
str=''
for x in temp:
    str+=chr(int(x))
print(str)
