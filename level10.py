level_url = 'http://huge:file@www.pythonchallenge.com/pc/return/good.html'
username='huge'
password='file'
import urllib
urlfile=urllib.urlopen(level_url,)
content=urlfile.read()
#print(content)


index=content.find('second')
content=content[index+1:]
index=content.find('second')
content1=content[:index]
content2=content[index:]
import re
pattern=re.compile('\d+')
first=pattern.findall(content1)
second=pattern.findall(content2)
first_num=[]
second_num=[]
for x in first:
    first_num.append(int(x))
for x in second:
    second_num.append(int(x))

import PIL.Image as Image
import PIL.ImageDraw as ImageDraw
image = Image.new('RGB',(640,480))
draw = ImageDraw.Draw(image)
draw.line(first_num,'white')
draw.line(second_num,'red')
image.show()
#cow?
#bull?
