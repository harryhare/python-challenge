import urllib2
url="http://www.pythonchallenge.com/pc/def/equality.html"
urlfile=urllib2.urlopen(url)
content=urlfile.read()
urlfile.close()
index=content.find('<!--')
content=content[index:]
import re
m=re.search('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]',content)
print(m.group())
print(m.group(1))
pattern=re.compile('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]')
array=pattern.findall(content)
print(array)
str=''
for x in array:
    str+=x
print(str)

