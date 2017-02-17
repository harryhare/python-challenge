import urllib
import copy
from PIL import Image
level_url = "http://kohsamui:thailand@www.pythonchallenge.com/pc/rock/arecibo.html"
level_url2 = "http://kohsamui:thailand@www.pythonchallenge.com/pc/rock/up.html"
warmup_url = "http://kohsamui:thailand@www.pythonchallenge.com/pc/rock/warmup.txt"
up_url = "http://kohsamui:thailand@www.pythonchallenge.com/pc/rock/up.txt"

# arrow
# up


def read(url):
    f = urllib.urlopen(url)
    content = f.read()
    lines = content.split("\n")
    assert (len(lines) > 2)
    (h, v) = map(int, lines[1].split(" "))
    lineindex = 4
    horizonal = []
    vertical = []
    for l in [horizonal, vertical]:
        while True:
            t = lines[lineindex]
            if t == "":
                lineindex += 1
                continue
            l.append(map(int, t.split(" ")))
            lineindex += 1
            if len(l) == h:
                lineindex += 2
                break
    print(horizonal)
    print(vertical)
    return h, v, horizonal, vertical


def fun(head, l, length, possiblities):
    minlength = sum(l) + len(l) -1
    maxbegin = length -len(head) - minlength + 1 # !=
    x = l.pop(0)
    for i in range(maxbegin):
        if(len(l)==0):
            h1 = head + [0] * i + [1] * x
            h1 += [0] *(length - len(h1))
            possiblities.append(h1)
        else:
            h1 = head + [0] * i + [1] * x + [0]
            fun(h1, copy.copy(l), length, possiblities)
def printmatrix(m,r,c):
    rr=""
    for i in range(r):
        for j in range(c):
            rr += str(m[i * c + j]) + "\t"
        rr += "\n"
    print rr


def solve(h,v,lh,lv):
    h_possibles = []
    v_possibles = []
    for (length,l,possibles) in [(v,lh,h_possibles),(h,lv,v_possibles)]:
        for x in l:
            p = []
            fun([],x,length,p)
            possibles.append(p)
    mark = [-1] * h * v # -1 undeside 0 empty 1
    changed = True
    count = 0
    while changed == True:
        changed = False
        for i in range(h):
            p=h_possibles[i]
            for j in range(v):
                shouldbe = mark[i * v + j]
                if shouldbe != -1:#deleted
                    newp=[]
                    for x in p:
                        if x[j] == shouldbe:
                            newp.append(x)
                    p=newp
                    h_possibles[i]=p
            for j in range(v):
                if mark[i * v + j] == -1:#determine
                    p0=copy.copy(p[0])
                    same = True
                    for x in p:
                        if(x[j]!=p0[j]):
                            same = False
                            break
                    if same == True:
                        mark[i * v + j] = p0[j]
                        count += 1
                        changed = True
                        #printmatrix(mark,h,v)
        if(count==v*h):
            break
        #print(h_possibles)
        for j in range(v):
            p=v_possibles[j]
            for i in range(h):
                shouldbe = mark[i * v + j]
                if shouldbe != -1:#deleted
                    newp = []
                    for x in p:
                        if x[i] == shouldbe:
                            newp.append(x)
                    p=newp
                    v_possibles[j]=p
            for i in range(h):
                if mark[i * v + j] == -1:#determine
                    p0=copy.copy(p[0])
                    same = True
                    for x in p:
                        if(x[i]!=p0[i]):
                            same = False
                            break
                    if same == True:
                        mark[i * v + j] = p0[i]
                        changed = True
                        count+=1
                        #printmatrix(mark,h,v)
        #print(v_possibles)
        if (count == v * h):
            break
    #print(mark,h,v)
    #print(h_possibles)
    #print(v_possibles)
    return (mark,h_possibles,v_possibles)

# h, v, lh, lv = read(warmup_url)
# solve(h, v, lh, lv)
h, v, lh, lv = read(up_url)
(mark, hp, vp)=solve(h, v, lh, lv)
image=Image.new("1",(v,h))
image.putdata(mark)
image.save("./level33/level33.bmp")
# python
# beer