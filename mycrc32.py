from zlib import crc32

def mycrc(input):
    x=inverse32(0x04c11db7)
    init=0xffffffff
    t=init
    for i in input:
        t=t^ord(i)
        for j in range(8):
            mask=1
            if(mask&t!=0):
                t=(t>>1)^x
            else:
                t=(t>>1)
    return t^0xffffffff

def inverse8(x):
    y=0
    for i in range(8):
        y=(y<<1)|(x&1)
        x=x>>1
    return y

def inverse32(x):
    r=0x00000000
    for i in range(32):
        r=(r<<1)|(x&1)
        x=x>>1
    return r

def creat_table1():
    x=0x04c11db7
    init=0
    l=[0L]*256
    for i in range(256):
        t=init^(i<<24)
        for j in range(8):
            mask=1<<31
            if(mask&t!=0):
                t=(t<<1)^x
            else:
                t=(t<<1)
        l[i]=t
    return l

def creat_table3():#table1 inverse
    l1=creat_table1()
    l3=[0L]*256
    for i in range(256):
        j=inverse8(i)
        l3[j]=inverse32(l1[i])
    return l3

def creat_table2():
    x=inverse32(0x04c11db7)
    init=0
    l=[0]*256
    for i in range(256):
        t=init^i
        for j in range(8):
            mask=1
            if(mask&t!=0):
                t=(t>>1)^x
            else:
                t=(t>>1)
        l[i]=t
    return l

def test():
    assert (0==inverse8(0))
    assert (0x80==inverse8(1))
    assert (0x40==inverse8(2))
    assert (0xc0==inverse8(3))
    assert (0==inverse32(0))
    assert (0x80000000==inverse32(1))
    assert (0x40000000==inverse32(2))
    assert (0xc0000000==inverse32(3))
    l1=creat_table1()
    l2=creat_table2()
    l3=creat_table3()
    assert (l2==l3)
    for i in range(256):
        i=chr(i)
        assert (mycrc(i)&0xffffffff==crc32(i)&0xffffffff)
    # for i in range(256):
    #     print(bin(i),bin(inverse8(i)))
    # l=l2
    # for i in range(0,256,4):
    #     print(hex((l[i])&0xffffffff),hex((l[i+1])&0xffffffff),hex((l[i+2])&0xffffffff),hex((l[i+3])&0xffffffff))

if __name__=="__main__":
    test()