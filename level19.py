import difflib

def output(data,name):
    file=open(name,"wb")
    total=len(data)
    bytes=bytearray((total+3)//3)
    i=0
    j=0
    try:
        while(i<total):
            bytes[j]=int(data[i:i+2],16)
            i+=3
            j+=1
    except:
        print(name,(j//18)+1,j%18,data[i:i+2])
    file.write(bytes)
    file.close()



if True:
    level_url='http://www.pythonchallenge.com/pc/return/balloons.html'
    infile=open("./deltas/delta.txt")
    file1=""
    file2=""
    for line in infile.readlines():
        file1+=line[0:53]+"\n"
        file2+=line[56:109]+"\n"
    print(file1[0:200])
    print(file2[0:200])
    result1=""
    result2=""
    result3=""
    # the result of this piece of code is wrong
    # seq=difflib.SequenceMatcher(None,file1,file2)
    # for tag,i1,i2,j1,j2 in seq.get_opcodes():
    #     if(tag=='equal'):
    #         result1+=file1[i1:i2]
    #     elif(tag=='delete'):
    #         result2+=file1[i1:i2]
    #     elif(tag=='insert'):
    #         result3+=file2[j1:j2]
    #     elif(tag=='replace'):
    #         result2+=file1[i1:i2]
    #         result3+=file2[j1:j2]
    #     else:
    #         print("error")
    #         assert(0)
    #result3=result1[:3*18]+result3
    diff = difflib.ndiff(file1.splitlines(1),file2.splitlines(1))
    for i in diff:
        if(i[0]=="+"):
            result2+=i[2:]
        elif(i[0]=='-'):
            result3+=i[2:]
        elif(i[0]==' '):
            result1+=i[2:]
        else:
            print(i)
    print("result1:",len(result1)//53,"\n",result1[:200])
    print("result2:",len(result2)//53,"\n",result2[:200])
    print("result3:",len(result3)//53,"\n",result3[:200])
    output(result1,"./deltas/1.png")
    output(result2,"./deltas/2.png")
    output(result3,"./deltas/3.png")

# /hex/bin.html
# butter
# fly

