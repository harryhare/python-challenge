level_url='http://huge:file@www.pythonchallenge.com/pc/return/evil.html'
img_url='http://huge:file@www.pythonchallenge.com/pc/return/evil2.gfx'
import urllib
import PIL.Image as Image
file=urllib.urlopen(img_url,'rb')
content=file.read()
sub_file=[]
from cStringIO import StringIO
for i in range(0,5):
    temp_content=content[i::5]
    #image=Image.open(StringIO(temp_content))
    #image.show()
    temp_file=open('level13_subimg'+str(i)+".jpg",'wb')
    temp_file.write(temp_content)
    temp_file.close()
#disproportionality
#disproportional

