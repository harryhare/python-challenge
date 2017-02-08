level_url='http://www.pythonchallenge.com/pc/return/uzi.html'
import time
import datetime
begin=1582
count=0
for i in range(1586,1996,10):
    if((i%4==0 and i%100!=0) or i%400==0):
        target=datetime.date(i,1,1)
        if(target.weekday()==3):
            print(target)
            count+=1
            if(count==2):
                break
#http://worldhistoryproject.org/1756/1/27
#https://en.wikipedia.org/wiki/Wolfgang_Amadeus_Mozart
#mozart
count=0
for year in range(1996,1016,-20):
    if(year%100==0 and year%400!=0):
        continue
    else:#leap year
        temp=datetime.date(year,1,1)
        if(temp.weekday()==3):
            print(count,temp)
            count+=1
