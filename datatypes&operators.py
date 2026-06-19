Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
myvar=10
MYVAR=10
my_var=10
_myvar=10
my var=10
SyntaxError: invalid syntax
1myvar=10
SyntaxError: invalid decimal literal
a=b=c=10
a
10
b
10
c
10
a,b,c=10,20,30
a
10
b
20
c
30
a,b=b,a
a=10
type(a)
<class 'int'>
b=12.4
type(b)
<class 'float'>
c=4+9j
type(c)
<class 'complex'>
a=10
b=20
a+b
30
a-b
-10
a//b
0
a/b
0.5
a**b
100000000000000000000
a<b
True
a>b
False
a==b
False
a!=b
True
a<=b
True
a>=b
False
a=b
a+=b
a=10
b=20
a+=b
a
30

a*=b
b
20
a/=b
b
20
a**=b
a
3.486784401e+29
b
20
a//=b
a
1.7433922004999998e+28
b
20
s[0]=='p'
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    s[0]=='p'
NameError: name 's' is not defined
s="python"
s[0]=='p'
True
s[0]=='p'and s[-1]=='n'
True
s[0]=='p'or s[-1]=='n'
True
s[0]=='p'not s[-1]=='n'
SyntaxError: invalid syntax
s[0]=='p' not
SyntaxError: invalid syntax
not s[-1]=='n'
False
'python' in s
True
'java' in s
False
l=[1,3,5,6,7]
5 in l
True
2 in l
False
t=("one","two","three")
one in l
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    one in l
NameError: name 'one' is not defined. Did you mean: 'None'?
one in t
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    one in t
NameError: name 'one' is not defined. Did you mean: 'None'?
t
('one', 'two', 'three')
one in t
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    one in t
NameError: name 'one' is not defined. Did you mean: 'None'?
t=(1,2,3)
1 in t
True
4 in t
False
s={1,"one",2,"two"}
one in s
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    one in s
NameError: name 'one' is not defined. Did you mean: 'None'?
"one" in s
True
three in s
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    three in s
NameError: name 'three' is not defined
>>> "three" in s
False
>>> d={"name":"sarayu","age":"21"}
>>> name in d
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    name in d
NameError: name 'name' is not defined
>>> "name" in d
True
>>> "sarayu" in d
False
>>> l=[1,2,3,4]
>>> m=[1,2,3,4]
>>> 1==m
False
>>> l is m
False
>>> l=m
>>> l==m
True
>>> id(l)
1896097287232
>>> id(m)
1896097287232
>>> 11 & 12
8
>>> 11 | 12
15
>>> 11 ^ 12
7
>>> ~12
-13
>>> ~29
-30
>>> ~70
-71
