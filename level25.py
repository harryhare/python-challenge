from PIL import Image,ImageDraw
import urllib
level_url="http://www.pythonchallenge.com/pc/hex/ambiguity.html"
pic_url="http://www.pythonchallenge.com/pc/hex/maze.png"

class Maze:
    def __init__(self,maze,height,width):
        self.maze=maze
        self.width=width
        self.height=height
        self.total=width*height
    def search(self):
        #debug
        # file=open("maze.png","rb")
        # png=Image.open(file)
        # png.show()

        visited=[0]*self.total
        self.pre=[0]*self.total
        temp = []
        for i in range(self.width):
            if (self.maze[i] != 255 and self.maze[i] != 127):
                temp.append(i)
        end=[]
        for i in range(self.total-self.width,self.total):
            if ( self.maze[i]!= 255 and self.maze[i] != 127):
                end.append(i)
        print ("end",end,divmod(end[0],self.width))
        assert (len(temp)==1)
        start = temp[-1]
        visited[start] = 1
        pointer=0
        while(len(temp)>pointer):
            x=temp[pointer]
            pointer+=1
            i,j=divmod(x,self.width)
            for d in [self.lookup,self.lookdown,self.lookleft,self.lookright]:
                t=d(i,j)
                if(t!=None):
                    t=t[0]*self.width+t[1]
                    if(self.maze[t]!=255  and visited[t]==0):
                        self.pre[t]=x
                        temp.append(t)
                        #print(divmod(t,self.width))
                        visited[t]=1
                        if(t==end[0]):
                            break
        #debug
        # end=temp[pointer-1]
        # print(pointer,divmod(temp[pointer-1],self.width))
        # print(self.pre[410241])
        # for i in temp:
        #     x=i//self.width
        #     y=i%self.width
        #     png.putpixel((y,x),(0,0,127))
        # png.show()
        # t=end[0]
        # while(t!=0):
        #     (x,y)=divmod(t,self.width)
        #     png.putpixel((y, x), (0, 0, 127))
        #     t=self.pre[t]
        # png.show()
        t=end[0]
        path=[]
        while(t!=0):
            path.append(t)
            t=self.pre[t]
        return path
    def lookup(self,i,j):
        if (i>=1):
            return (i-1,j)
        else:
            return None
    def lookdown(self,i,j):
        if(i<=self.height-2):
            return(i+1,j)
        else:
            return None
    def lookleft(self,i,j):
        if(j>=1):
            return(i,j-1)
        else:
            return None
    def lookright(self,i,j):
        if(j<=self.width-2):
            return(i,j+1)
        else:
            return None

def part1():
    #file=urllib.urlopen(pic_url)
    #file=open("maze.png")
    #pic=Image.open(file)
    pic=Image.open("maze.png")
    data=pic.getdata()
    width,height=pic.size
    total=len(data)
    assert (total==width*height)
    maze=[0]*total
    visited=[0]*total
    for i in range(total):
        if(data[i]==(255,255,255,255)):
            maze[i]=255
    for i in range(0,60):
        for j in range(0,60):
            maze[i]=255
    m=Maze(maze,height,width)
    path=m.search()
    path=path[::-1]
    x=bytearray(len(path))
    for i in range(0,len(path)):
        x[i]=data[path[i]][0]
    print(x[:200])
    file=open("level25.zip","wb")
    file.write(x[1::2])
    for i in x[0::2]:
        assert i==0
    file.close()

    #lake#

#part 2
from hashlib import md5
md5_digest='bbb8b499a0eef99b52c7f13f4e78c24b'
file=open("./level25/mybroken.zip","rb")
content=file.read()
n=len(content)
for i in range(n):
    for j in range(256):
        x=content[:i]+chr(j)+content[i+1:]
        if(md5(x).hexdigest()==md5_digest):
            print(i,j)
            break
file.close()
newfile=open("./level25/repaired.zip","wb")
newfile.write(content[:i]+chr(j)+content[i+1:])
newfile.close()
#speed