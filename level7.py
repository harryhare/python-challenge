level_url='http://www.pythonchallenge.com/pc/def/channel.html'
start='90052'

import re
pattern=re.compile('\d+')
r=[start]
count=0
'''
while(len(r)==1):
    myfile=open('channel/'+r[0]+'.txt')
    content=myfile.read()
    count+=1
    print(count,content)
    r=pattern.findall(content)
'''

import zipfile 
file=zipfile.ZipFile('channel.zip','r')
comment=''
while(len(r)==1):
    filename=r[0]+'.txt'
    content=file.read(filename)
    count+=1
    print(count,content)
    comment+=file.getinfo(filename).comment
    r=pattern.findall(content)
print(comment)


