level_url='http://www.pythonchallenge.com/pc/return/5808.html'
img_url='http://huge:file@www.pythonchallenge.com/pc/return/cave.jpg'

import urllib
import PIL.Image as Image
file=urllib.urlopen(img_url)
image=Image.open(file)
image_new=[]
image_new.append(Image.new('RGB',(640,480)))
image_new.append(Image.new('RGB',(640,480)))
width=640
height=480
total=width*height
for y in range(0,480):
    for x in range(0,640):
        i=x+y
        color=image.getpixel((x,y))
        if(y%2==0):
            if(x%2==1):
                image_new[0].putpixel((x,y),color)
                image_new[0].putpixel((x-1,y),color)
            else:
                image_new[1].putpixel((x,y),color)
                image_new[1].putpixel((x+1,y),color)
        else:
            if(x%2==0):
                image_new[0].putpixel((x,y),color)
                image_new[0].putpixel((x+1,y),color)
            else:
                image_new[1].putpixel((x,y),color)
                image_new[1].putpixel((x-1,y),color)
image_new[0].show()
image_new[1].show()
        
    
    
    


