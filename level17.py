level_url='http://www.pythonchallenge.com/pc/return/mozart.html'
image_url='http://huge:file@www.pythonchallenge.com/pc/return/mozart.gif'
import PIL.Image as Image
import urllib
image_file=urllib.urlopen(image_url)
image_new=Image.new('P',(1280,480))
image=Image.open(image_file)
image.show()
palette=image.getpalette()
image_new.putpalette(palette)
for i in range(480):
    for j in range(635):
        if(image.getpixel((j,i))==195 and image.getpixel((j+1,i)) and image.getpixel((j+2,i))):
            start=j
            break
    for k in range(0,640):
        color=image.getpixel((k,i))
        image_new.putpixel((640-start+k,i),color)

#romance        
#pillow ,PIL fork
#document:
#http://pillow.readthedocs.org/en/latest/handbook/concepts.html#concept-modes
