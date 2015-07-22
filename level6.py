import pickle
level_url='http://www.pythonchallenge.com/pc/def/peak.html'
pfile=open('banner.p','r')
x=pickle.load(pfile)
str=''
for line in x:
    for elem in line:
        for i in range(0,elem[1]):
            str+=elem[0]
    print(str)
