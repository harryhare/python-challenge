level_url='http://www.pythonchallenge.com/pc/return/bull.html'
start=[1]

def fun(start):
    count=1
    prev=start[0]
    current=[]
    for x in start[1:]:
        if(prev==x):
            count+=1
        else:
            current.append(count)
            current.append(prev)
            prev=x
            count=1
    current.append(count)
    current.append(prev)
    return current

print(0,start)
for i in range(1,31):
    start=fun(start)
    print(i,len(start))
print(len(start))
