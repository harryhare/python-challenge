import zlib
import bz2
log=""
file=open("./level20/package.pack","rb")
reversed=False
data=file.read()
while True:
    print(data[:2])
    if(data[:2]=='x\x9c'):
        data=zlib.decompress(data)
        reversed=False
        log+="z"
    elif(data[:2]=="BZ"):
        data=bz2.decompress(data)
        reversed=False
        log+='b'
    elif(reversed==False):
        data=data[::-1]
        reversed=True
        log+='r'
    else:
        break
log=log.replace('r','\n')
log=log.replace("z"," ")
print log
#print log[::-1]
#copper