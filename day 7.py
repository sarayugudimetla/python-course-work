Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
t=()
t=tuple()
type(t)
<class 'tuple'>
t=(1,2,3,4,5)
t
(1, 2, 3, 4, 5)
t=(1)
t
1
t=()
t=(1,)
t
(1,)
t=(1,1,1)
t
(1, 1, 1)
(1,2,3)+(3,4,5)
(1, 2, 3, 3, 4, 5)
(1,2,3)*3
(1, 2, 3, 1, 2, 3, 1, 2, 3)
t
(1, 1, 1)
t=(1,2,3,4,6,7,8,1,4,5)
t[2]
3
t[3]
4
t[0]
1
t[-1]
5
t[:4]
(1, 2, 3, 4)
t[6:]
(8, 1, 4, 5)
t[::-1]
(5, 4, 1, 8, 7, 6, 4, 3, 2, 1)
t[-1:-5]
()
t
(1, 2, 3, 4, 6, 7, 8, 1, 4, 5)
8 in t
True
11 in t
False
t.index(3)
2
t.count(5)
1
sorted(t)
[1, 1, 2, 3, 4, 4, 5, 6, 7, 8]
max(t)
8
min(t)
1
sum(t)
41
len(t)
10
any((1,2,3,4))
True
any((1,0))
True
all((1,0))
False
all((1,0))
False
a,b,c=(1,2,3)
a
1
b
2
c
3
a=(1,2,3,4)
a
(1, 2, 3, 4)
w,x,y,z=a
w
1
x
2
y
3
z
4
t=(1,12.3,"string",[1,2,3],{1,2,3},(1,2,3),{1:1,2:2,3:3},false)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    t=(1,12.3,"string",[1,2,3],{1,2,3},(1,2,3),{1:1,2:2,3:3},false)
NameError: name 'false' is not defined. Did you mean: 'False'?
t=(1,12.3,"string",[1,2,3],{1,2,3},(1,2,3),{1:1,2:2,3:3},false,none)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    t=(1,12.3,"string",[1,2,3],{1,2,3},(1,2,3),{1:1,2:2,3:3},false,none)
NameError: name 'false' is not defined. Did you mean: 'False'?
t[0]
1
t[0]=12
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    t[0]=12
TypeError: 'tuple' object does not support item assignment
t=(1,12.3,"string",[1,2,3],{1,2,3},(1,2,3),{1:1,2:2,3:3},False,none)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    t=(1,12.3,"string",[1,2,3],{1,2,3},(1,2,3),{1:1,2:2,3:3},False,none)
NameError: name 'none' is not defined. Did you mean: 'None'?
t=(1,12.3,"string",[1,2,3],{1,2,3},(1,2,3),{1:1,2:2,3:3},False)
t
(1, 12.3, 'string', [1, 2, 3], {1, 2, 3}, (1, 2, 3), {1: 1, 2: 2, 3: 3}, False)
d={}
d=dict()
typr(d)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    typr(d)
NameError: name 'typr' is not defined. Did you mean: 'type'?
type(d)
<class 'dict'>
d[1]='int'
d[12.0]='flo'
d
{1: 'int', 12.0: 'flo'}
d["string"]='str'
d[1,2,3]='list'
d[2+3j]='com'
d[False]='bool'
d
{1: 'int', 12.0: 'flo', 'string': 'str', (1, 2, 3): 'list', (2+3j): 'com', False: 'bool'}
d[1]='integer'
d
{1: 'integer', 12.0: 'flo', 'string': 'str', (1, 2, 3): 'list', (2+3j): 'com', False: 'bool'}
d={}
d[1]=1
d[2]=12.3
d[3]='str'
d[4]=[1,2,3]
d[5]=(1,2,3)
d[6]={1,23}
d[7]={1:1,2:2}
d[8]=2+4j
d[9]=True
d[10]=None
d
{1: 1, 2: 12.3, 3: 'str', 4: [1, 2, 3], 5: (1, 2, 3), 6: {1, 23}, 7: {1: 1, 2: 2}, 8: (2+4j), 9: True, 10: None}
d[4]
[1, 2, 3]
d[5]
(1, 2, 3)
d[2]
12.3
d
{1: 1, 2: 12.3, 3: 'str', 4: [1, 2, 3], 5: (1, 2, 3), 6: {1, 23}, 7: {1: 1, 2: 2}, 8: (2+4j), 9: True, 10: None}
d.get(30)
d
{1: 1, 2: 12.3, 3: 'str', 4: [1, 2, 3], 5: (1, 2, 3), 6: {1, 23}, 7: {1: 1, 2: 2}, 8: (2+4j), 9: True, 10: None}
d[12]
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    d[12]
KeyError: 12
d.get(12)
d.get(30,'key is not present')
'key is not present'
d
{1: 1, 2: 12.3, 3: 'str', 4: [1, 2, 3], 5: (1, 2, 3), 6: {1, 23}, 7: {1: 1, 2: 2}, 8: (2+4j), 9: True, 10: None}
id(d)
1884933164608
d[4]=20
d
{1: 1, 2: 12.3, 3: 'str', 4: 20, 5: (1, 2, 3), 6: {1, 23}, 7: {1: 1, 2: 2}, 8: (2+4j), 9: True, 10: None}
id(d)
1884933164608
d[8]=40
d
{1: 1, 2: 12.3, 3: 'str', 4: 20, 5: (1, 2, 3), 6: {1, 23}, 7: {1: 1, 2: 2}, 8: 40, 9: True, 10: None}
d[5]=30
d
{1: 1, 2: 12.3, 3: 'str', 4: 20, 5: 30, 6: {1, 23}, 7: {1: 1, 2: 2}, 8: 40, 9: True, 10: None}
d[14]=90
d
{1: 1, 2: 12.3, 3: 'str', 4: 20, 5: 30, 6: {1, 23}, 7: {1: 1, 2: 2}, 8: 40, 9: True, 10: None, 14: 90}
d[15]=101
d
{1: 1, 2: 12.3, 3: 'str', 4: 20, 5: 30, 6: {1, 23}, 7: {1: 1, 2: 2}, 8: 40, 9: True, 10: None, 14: 90, 15: 101}
d.update({16:17,17:18})
d
{1: 1, 2: 12.3, 3: 'str', 4: 20, 5: 30, 6: {1, 23}, 7: {1: 1, 2: 2}, 8: 40, 9: True, 10: None, 14: 90, 15: 101, 16: 17, 17: 18}
d.popitem()
(17, 18)
d.popitem()
(16, 17)
d.popitem()
(15, 101)
d
{1: 1, 2: 12.3, 3: 'str', 4: 20, 5: 30, 6: {1, 23}, 7: {1: 1, 2: 2}, 8: 40, 9: True, 10: None, 14: 90}
d.pop(6)
{1, 23}
d
{1: 1, 2: 12.3, 3: 'str', 4: 20, 5: 30, 7: {1: 1, 2: 2}, 8: 40, 9: True, 10: None, 14: 90}
d.pop(14)
90
del d[3]
d
{1: 1, 2: 12.3, 4: 20, 5: 30, 7: {1: 1, 2: 2}, 8: 40, 9: True, 10: None}
del d[10]
d
{1: 1, 2: 12.3, 4: 20, 5: 30, 7: {1: 1, 2: 2}, 8: 40, 9: True}
d.clear()
d
{}
d.keys()
dict_keys([])
d={1: 1, 2: 12.3, 3: 'str', 4: 20, 5: 30, 7: {1: 1, 2: 2}, 8: 40, 9: True, 10: None, 14: 90}
d
{1: 1, 2: 12.3, 3: 'str', 4: 20, 5: 30, 7: {1: 1, 2: 2}, 8: 40, 9: True, 10: None, 14: 90}
d.keys()
dict_keys([1, 2, 3, 4, 5, 7, 8, 9, 10, 14])
>>> d.values()
dict_values([1, 12.3, 'str', 20, 30, {1: 1, 2: 2}, 40, True, None, 90])
>>> d.item()
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    d.item()
AttributeError: 'dict' object has no attribute 'item'. Did you mean: 'items'?
>>> sorted(d)
[1, 2, 3, 4, 5, 7, 8, 9, 10, 14]
>>> min(d)
1
>>> max(d)
14
>>> len(d)
10
>>> d
{1: 1, 2: 12.3, 3: 'str', 4: 20, 5: 30, 7: {1: 1, 2: 2}, 8: 40, 9: True, 10: None, 14: 90}
>>> m=d
>>> m[10]=13
>>> m
{1: 1, 2: 12.3, 3: 'str', 4: 20, 5: 30, 7: {1: 1, 2: 2}, 8: 40, 9: True, 10: 13, 14: 90}
>>> n=d.copy()
>>> n
{1: 1, 2: 12.3, 3: 'str', 4: 20, 5: 30, 7: {1: 1, 2: 2}, 8: 40, 9: True, 10: 13, 14: 90}
>>> n[70]=80
>>> n
{1: 1, 2: 12.3, 3: 'str', 4: 20, 5: 30, 7: {1: 1, 2: 2}, 8: 40, 9: True, 10: 13, 14: 90, 70: 80}
>>> d
{1: 1, 2: 12.3, 3: 'str', 4: 20, 5: 30, 7: {1: 1, 2: 2}, 8: 40, 9: True, 10: 13, 14: 90}
>>> d.serdefault(2)
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    d.serdefault(2)
AttributeError: 'dict' object has no attribute 'serdefault'. Did you mean: 'setdefault'?
>>> d.setdefault(2)
12.3
>>> d
{1: 1, 2: 12.3, 3: 'str', 4: 20, 5: 30, 7: {1: 1, 2: 2}, 8: 40, 9: True, 10: 13, 14: 90}
>>> d.setdefault(4,70)
20
>>> d.setdefault(30,70)
70
