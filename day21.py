'''
import random

print(random.random())
print(random.randint(12,20))
print(random.uniform(12,20))

l=['java','c++','python','c','html']

print(random.choice(l))
print(random.choices(l,k=3))

print(l)
random.shuffle(l)
print(l)
'''
#password
'''
import random

name=input("Enter the name:")
spe_chars=['!','@','#','$','%','^','&','*']
sample1=random.choices(name,k=4)+random.choices(spe_chars,k=2)
sample2=(''.join(sample1)).title()

print(sample2+str(random.randint(1111,9999)))
'''
#time date day
'''
from datetime import date,time,datetime,timedelta

d=date.today()
print(d)
print(d.day)
print(d.month)
print(d.year)
print(d.weekday())
print(d.isoweekday())
'''

'''
from datetime import date,time,datetime,timedelta

d=date(2026,12,28)
print(d)
'''
'''
from datetime import date,time,datetime,timedelta

d=datetime.now()

print(d)
print(d.day)
print(d.month)
print(d.year)
print(d.weekday())
print(d.isoweekday())
print(d.hour)
print(d.minute)
print(d.second)
'''
'''
from datetime import date,time,datetime,timedelta

d=datetime.now()

print(d.strftime('%d/%m/%y'))
print(d.strftime('%d/%m/%y %H:%M:%s'))
print(d.strftime('%d/%m/%y %I:%M:%s%p'))
print(d.strftime('%d %b %y %I:%M:%s%p'))
print(d.strftime('%d %B %y %I:%M:%s%p'))
print(d.strftime('%a %d %B %Y %I:%M:%s%p'))
print(d.strftime('%A %d %B %Y %I:%M:%s%p'))
'''
'''
from datetime import date,time,datetime,timedelta

d=datetime.now()

d7=d+timedelta(days=60)
print(d7)

m15=d-timedelta(minutes=15)
print(m15)

s15=d+timedelta(seconds=15)
print(s15)
'''
'''
from itertools import combinations,permutations

res1=list(combinations('abc',2))
res2=list(permutations('abc',2))

print([''.join(i) for i in res1])
print([''.join(i) for i in res2])
'''
'''
from collections import Counter,defaultdict,deque

s='python programming'
l=[1,1,2,3,4,2,1,3,23,1,21]
print(Counter(s))
print(Counter(l))
'''
'''
from collections import Counter,defaultdict,deque

s='python programming'
l=[1,1,2,3,4,2,1,3,23,1,21]

d=defaultdict(int)
for i in s:
    d[i]+=1

print(d)
'''
from collections import deque

d=deque([])

d.append(10)
d.append(20)
d.append(30)
d.append(40)
d.popleft()
d.popleft()
d.append(50)
d.append(60)
d.append(70)
d.popleft()

print(d)
