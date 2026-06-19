Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
name=input()
sarayu
name
'sarayu'
age=int(input())
21
age
21
gpa=float(input())
8.8
gpa
8.8
name=input().split()
sarayu pujith
name
['sarayu', 'pujith']
name=tuple(input().split())
sarayu sai
name
('sarayu', 'sai')
name=list(map(int,input().split()))
sarayu sai
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    name=list(map(int,input().split()))
ValueError: invalid literal for int() with base 10: 'sarayu'
name=list(map(int,input().split()))
12,33,42
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    name=list(map(int,input().split()))
ValueError: invalid literal for int() with base 10: '12,33,42'
marks=list(map(int,input().split()))
2 3 45 6
marks
[2, 3, 45, 6]
marks=tuple(map(int,input().split()))
1 2 34
marks
(1, 2, 34)
marks=set(map(int,input().split()))
34 54 34
marks
{34, 54}
marks=list(map(float,input().split()))
56.7 87.6
marks
[56.7, 87.6]
marks=tuple(map(float,input().split()))
12.3 43.2
marks
(12.3, 43.2)
KeyboardInterrupt
marks=set(map(float,input().split()))
56.7 87.6
marks
{56.7, 87.6}
marks=eval(input().split())
12 34
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    marks=eval(input().split())
TypeError: eval() arg 1 must be a string, bytes or code object
marks=eval(input())
6
marks
6
type(marks)
<class 'int'>
marks=eval(input())
sarayu
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    marks=eval(input())
  File "<string>", line 1, in <module>
NameError: name 'sarayu' is not defined
name=eval(input())
sarayu
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    name=eval(input())
  File "<string>", line 1, in <module>
NameError: name 'sarayu' is not defined
marks=eval(input())
"sarayu"
marks
'sarayu'
username,password=input().split()
abc abc123
username
'abc'
password
'abc123'
a,b,c=list(map(int,input().split()))
3 4 5
a
3
b
4
c
5
a='python'
b=12
c=78.9
print9a,b,c)
SyntaxError: unmatched ')'
print(a,b,c)
python 12 78.9
print('a=',a,'b=',b,'c=',c)
a= python b= 12 c= 78.9
>>> print('a=',a,'b=',b,'c=',c,sep='')
a=pythonb=12c=78.9
>>> print('a=',a,'b=',b,'c=',\n)
SyntaxError: unexpected character after line continuation character
>>> print('a=',a,'b=',b,'c=',c,'\n')
a= python b= 12 c= 78.9 

>>> print('a=',a,'b=',b,'c=',c,sep='\n)
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print('a=',a,'b=',b,'c=',c,sep='\n')
...       
a=
python
b=
12
c=
78.9
>>> print('a=',a,'b=',b,'c=',c,sep='\t')
...       
a=	python	b=	12	c=	78.9
>>> print('a=',a,'b=',b,'c=',c,sep='\t',end='@@@')
...       
a=	python	b=	12	c=	78.9@@@
>>> print('a=',a,'b=',b,'c=',c,sep='\t',end='\n\n\n')
...       
a=	python	b=	12	c=	78.9


>>> print(f'a={a} b={b} c={c}')
...       
a=python b=12 c=78.9
>>> print('a = %s b=%d c=%f'%(a,b,c))
...       
a = python b=12 c=78.900000
>>> print('a={} b={} c={}'.format(a,b,c))
...       
a=python b=12 c=78.9
>>> print('a={2} b={0} c={1}'.format(a,b,c))
...       
a=78.9 b=python c=12
