'''
wish=lambda name:f'welcome to the course,{name}'
print(wish('chandhini'))
print(wish('sarayu'))
'''
'''
greater=lambda a,b: a if a>b else b
print(greater(10,3))
print(greater(1,34))
print(greater(40,90))
'''
'''
avg=lambda a,b,c:(a+b+c)/3
print(avg(10,20,30))
print(avg(80,60,30))
'''
'''
gst=lambda p:p+p*0.18
print(gst(1000))
print(gst(100))
'''
'''
from functools import reduce

l=(1,2,3,4,5)
res1=list(map(lambda i:i+10,l))
print(res1)

s=[12,23,45,56,67,78]
res2=list(filter(lambda i:i%3==0,s))
print(res2)

k=[10,20,30,40]
res3=reduce(lambda sum,i:sum+i,k)
print(res3)
'''
'''
from functools import reduce

l={'laptop':50000,'phone':100000,'charger':2000,'mouse':800}
res1=dict(map(lambda i:(i[0],i[1]+i[1]*0.18),l.items()))
print(res1)

h2l=dict(sorted(l.items(),key=lambda i:i[1],reverse=True))
print(h2l)
l2h=dict(sorted(l.items(),key=lambda i:i[1]))
print(l2h)

l={'laptop':50000,'phone':100000,'charger':2000,'mouse':800}
res2=list(filter(lambda i:l[i]!=0,l))
print(res2)
'''
'''


r=reels()
print(next(r))
print(next(r))
print(next(r))
print(next(r))
'''
'''
def reels():
    l=['1..50','51..100','101..200','201..250']
    for i in range(len(l)):
        yield l[i]
r=reels()

while True:
    try:
        print(next(r))
    except StopIteration:
        break
'''
'''
def factors(n):
    return[i for i in range(1,n+1) if n%i==0]

def generators(res):
    for i in res:
        yield i

res=factors(30)
f=generators(res)

for i in range(len(res)):
    print(next(f))
'''
def fib(n):
    if n==1:
        return [0]
    elif n==2:
        return [0,1]
    elif n>2:
        res=[0,1]
        a,b=0,1
        for i in range(n-2):
            c=a+b
            res.append(c)
            a,b=b,c
        return res

def generators(res):
    for i in res:
        yield i

res=fib(13)
f=generators(res)

for i in range(len(res)):
    print(next(f))

