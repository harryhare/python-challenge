import urllib2
url="http://www.pythonchallenge.com/pc/def/ocr.html"
urlfile=urllib2.urlopen(url)
content=urlfile.read()
index=content.find('<!--')
content=content[index+1:]
index=content.find('<!--')
content=content[index:]
str=''
for x in content:
    if(x>='a' and x<='z'):
        str+=x
print(str)
