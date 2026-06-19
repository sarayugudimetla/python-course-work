




# billing
'''
lis=list(map(int,input("Enter the prices:").split()))
bill=0
for i in lis:
    bill=bill+i
print("Bill:",bill)
'''



#Password security Analyzer
'''
pas=input(":")
upper=0
lower=0
num=0
spl=0
for i in pas:
    if i.isalpha():
        if i.isupper():
            upper=upper+1
        else:
            lower=lower+1
    elif i.isdigit():
        num=num+1
    else:
        spl=spl+1
print("upper count:",upper)
print("lower count:",lower)
print("Nums:",num)
print("special:",spl)
'''


#Netfilx watch histoty
'''
movies=input(":").split()
for i in range(len(movies)):
    print(i+1,movies[i])
'''


#Employee Salaey Analytics

'''
records=eval(input())
print(max(records.values()))
print(min(records.values()))
print(sum(records.values())/len(records))
'''


# Ipl

'''
runs=list(map(int,input().split()))
summ=0
fours=0
sixes=0
dot=0
for i in runs:
    summ=summ+i
    if i==4:
        fours=fours+1
    elif i==6:
        sixes=sixes+1
    elif i==0:
        dot=dot+1
print(summ)
print(fours)
print(sixes)
print(dot)
'''


# Email Domain Extraction

'''
email=input("Enter the Email_ID:").split()
for i in email:
    print(i.split("@")[1])
'''
# while loop
# ATM PIN

'''
pin=2307
attempt=0
while attempt<3:
    epin=int(input("Enter the PIN:"))
    if epin==pin:
        print("Acess Granted")
        break
    attempt+=1
else:
    print("Card Blocked")
'''
#Food Ordering

'''
count=0
while True:
    items=input("Enter the Items or exit:")
    if items=="exit":
        print(count)
        breakprint(max(records.values()))
        break
    count+=1
'''


# Gaming Life System

'''
crt="pythom"
attempt=0
while attempt<3:
    guess=input("Enter the Name:")
    if guess==crt:
        print("You Win")
        break
    attempt+=1
else:
    print("Game Over")
'''
#

s = input(":")
i = 0
j = len(s) - 1
while i < j:
    print(s[i] + s[j])
    i += 1
    j -= 1
if i == j:      
    print(s[i])
    
    
    


                       
