level_url='http://www.pythonchallenge.com/pc/return/italy.html'
png_url='http://huge:file@www.pythonchallenge.com/pc/return/wire.png'
jpg_url='http://www.pythonchallenge.com/pc/return/italy.jpg'

import urllib
import PIL.Image as Image
png_file=urllib.urlopen(png_url)
png=Image.open(png_file)
png.show()
png_new=Image.new('RGB',(100,100))
x=0
y=0
left=0
right=99
up=0
down=99
d=0
#(x,y)
#step={'up':{1,0},'right':{0,1},'down':{-1,0},'left':{0,-1}}
step=[(1,0),(0,1),(-1,0),(0,-1)]
for i in range(0,10000):
    color=png.getpixel((i,0))
    png_new.putpixel((x,y),color)
    if(x==right and d==0):
        d=1
        up+=1
    elif(y==down and d==1):
        d=2
        right-=1
    elif(x==left and d==2):
        d=3
        down-=1
    elif(y==up and d==3):
        d=0
        left+=1
    x+=step[d][0]
    y+=step[d][1]
png_new.show()
        
#cat
#uzi

