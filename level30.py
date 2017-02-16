import urllib
import bz2
level_url = "http://repeat:switch@www.pythonchallenge.com/pc/ring/guido.html"
html = urllib.urlopen(level_url)
content = html.read()
begin = content.find("</html>")
content = content[begin:]
l = content.split("\n")
l = l[1:]
lens = [chr(len(i)) for i in l]
crypt = "".join(lens)
plain = bz2.decompress(crypt)
print(plain)

#"Isn't it clear? I am yankeedoodle!"
