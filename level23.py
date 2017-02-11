import httplib
import urllib
from PIL import Image,ImageDraw,ImageSequence

level_url="http://www.pythonchallenge.com/pc/hex/copper.html"
gif_file="http://www.pythonchallenge.com/pc/hex/white.gif"

class Turtle:
    def __init__(self,n):
        self.image=Image.new("RGB",(40*n,40*n),'white')
        self.init_position=zip(range(20,40*n,40),range(20,40*n,40))
        self.draw=ImageDraw.Draw(self.image)
        self.x=20
        self.y=20
        self.n=n
        self.current=-1

    def act(self,cmd):
        if(cmd=='u' or cmd==98*200+100):
            self.y-=1
        elif(cmd=='r' or cmd==20102):
            self.x+=1
        elif(cmd=='d' or cmd==102*200+100):
            self.y+=1
        elif(cmd=='l' or cmd==20098):
            self.x-=1
        elif(cmd=='n' or cmd==20100):
            self.current+=1
            self.x,self.y=self.init_position[self.current]
        elif(cmd=="ul" or cmd==98*200+98):
            self.x-=1
            self.y-=1
        elif(cmd=="ur" or cmd==98*200+102):
            self.x+=1
            self.y-=1
        elif(cmd=="dl" or cmd==102*200+98):
            self.x-=1
            self.y+=1
        elif(cmd=="dr" or cmd==102*200+102):
            self.x+=1
            self.y+=1
        else:
            print(cmd)
            assert False
        self.draw.point((self.x,self.y),"blue")

    def show(self):
        self.image.show()

    def save(self,name):
        self.image.save(name)

#file=urllib.urlopen(gif_file)
file=open("white.gif","rb")
gif=Image.open(file)
palette=gif.getpalette()
assert (palette[24:27]==[8,8,8])
palette[24:27]=[255,255,255]
gif.putpalette(palette)
gif.save("white_.gif")


# approach 1
# x,y=gif.size
# points=[]
# f=0
# for image in ImageSequence.Iterator(gif):
#     points.append([])
#     for i in range(0,x):
#         for j in range(0,y):
#             if(image.getpixel((i,j))!=0):
#                 points[f].append((i,j))
#     f+=1
# print(points)

# approach 2
locations=[0]*gif.n_frames
c=0
for image in ImageSequence.Iterator(gif):
    data=list(image.getdata())
    assert (len(data)==40000)
    i=data.index(8)
    #y,x=divmod(i,200)
    locations[c]=i
    c+=1
print locations

turtle=Turtle(10)
for i in locations:
    turtle.act(i)
turtle.show()
turtle.save("level23.png")

#bonus