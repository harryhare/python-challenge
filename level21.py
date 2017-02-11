import urllib
import httplib
import base64
import re
level_url="http://www.pythonchallenge.com/pc/hex/idiot2.html"
pic_url="http://www.pythonchallenge.com/pc/hex/unreal.jpg"
pattern=re.compile(r"\d+")
headers={"Authorization":"Basic"+" "+base64.b64encode("butter:fly")}
conn=httplib.HTTPConnection("www.pythonchallenge.com")
pre_begin=-1
next_begin=-1
#part 1
while(True):
    conn.request("GET",'/pc/hex/unreal.jpg','',headers)
    response=conn.getresponse()
    range_string=response.getheader("content-range")
    print(response.status,response.reason,range_string)
    x=response.read()
    print(x[:200])
    if(range_string==None or range_string==""):
        break
    temp=re.findall(pattern,range_string)
    if(len(temp)!=3):
        break
    (begin, end, upbound)=temp
    if(int(begin)<pre_begin):
        break
    pre_begin=next_begin
    next_begin=int(end)+1
    next_end=max(int(upbound),int(end)+50)
    headers['Range']='bytes'+'='+str(next_begin)+'-'+str(next_end)
    #print(headers)

next_begin=2123456789+1
next_end=next_begin+50
headers['Range'] = 'bytes' + '=' + str(next_begin) + '-' + str(next_end)
while(True):
    conn.request("GET",'/pc/hex/unreal.jpg','',headers)
    response=conn.getresponse()
    range_string=response.getheader("content-range")
    print(response.status,response.reason,range_string)
    x=response.read()
    print(x,x[::-1])
    if(range_string==None or range_string==""):
        break
    temp=re.findall(pattern,range_string)
    if(len(temp)!=3):
        break
    (begin, end, upbound)=temp
    next_begin=int(begin)-1
    next_end=2123456789
    headers['Range']='bytes'+'='+str(next_begin)+'-'+str(next_end)
    #print(headers)

next_begin=1152983631
nex_end=2123456789
headers['Range'] = 'bytes' + '=' + str(next_begin) + '-' + str(next_end)
conn.request("GET", '/pc/hex/unreal.jpg', '', headers)
response = conn.getresponse()
range_string = response.getheader("content-range")
print(response.status, response.reason, range_string)
x = response.read()
print(x[:200])
out=open("level20.zip","wb")
out.write(x)
out.close()
print("invader"[::-1])