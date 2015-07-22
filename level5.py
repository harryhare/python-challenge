import urllib
url_prefix='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
level_url='http://www.pythonchallenge.com/pc/def/linkedlist.php'
import re
pattern=re.compile('\d+')
count=0

r = ['12345']
while( len(r)==1):
    url=url_prefix+r[0]
    urlfile=urllib.urlopen(url)
    content=urlfile.read()
    count+=1
    print(count,":",content)
    r =  pattern.findall(content)

r = ['8022']
while( len(r)==1):
    url=url_prefix+r[0]
    urlfile=urllib.urlopen(url)
    content=urlfile.read()
    count+=1
    print(count,":",content)
    r =  pattern.findall(content)

r=['63579']
while( len(r)==1):
    url=url_prefix+r[0]
    urlfile=urllib.urlopen(url)
    content=urlfile.read()
    count+=1
    print(count,":",content)
    r =  pattern.findall(content)
print(content)
