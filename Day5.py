Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s='python program'
fname='sarayu'
lname='gudimetla'
fname+lname
'sarayugudimetla'
s
'python program'
s*10
'python programpython programpython programpython programpython programpython programpython programpython programpython programpython program'
'sai'*100
'saisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisai'
s='sarayu sai pranavi pujith'
s
'sarayu sai pranavi pujith'
s[0]
's'
s[4]
'y'
s[9]
'i'
s[-1]
'h'
s-8]
SyntaxError: unmatched ']'
s[-8]
'i'
s[:6]
'sarayu'
s[7:10]
'sai'
s[8:15]
'ai pran'
s[20;]
SyntaxError: invalid syntax
s[20:]
'ujith'
s[21:]
'jith'
s[19:]
'pujith'
s[12:]
'ranavi pujith'
s[11:]
'pranavi pujith'
s[-6:]
'pujith'
s[-1:-6:-1]
'htiju'
s[-7:14]
''
s[-7:-14]
''
s[::2]
'sry a rnv uih'
s[1::2]
'aausipaaipjt'
len(s)
25
ord('a')
97
ord('z')
122
ord('A'\)
    
SyntaxError: unexpected character after line continuation character
sorted(s)
    
[' ', ' ', ' ', 'a', 'a', 'a', 'a', 'a', 'h', 'i', 'i', 'i', 'j', 'n', 'p', 'p', 'r', 'r', 's', 's', 't', 'u', 'u', 'v', 'y']
min(s)
    
' '
max(s)
    
'y'
s.upper()
    
'SARAYU SAI PRANAVI PUJITH'
s.lower()
    
'sarayu sai pranavi pujith'
s.swapcase()
    
'SARAYU SAI PRANAVI PUJITH'
s.captilize()
    
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    s.captilize()
AttributeError: 'str' object has no attribute 'captilize'. Did you mean: 'capitalize'?
s.capitalize
    
<built-in method capitalize of str object at 0x00000263E01443F0>
s.capitalize()
    
'Sarayu sai pranavi pujith'
s.tittle()
    
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    s.tittle()
AttributeError: 'str' object has no attribute 'tittle'. Did you mean: 'title'?
s.title()
    
'Sarayu Sai Pranavi Pujith'
s.center(60,'-')
    
'-----------------sarayu sai pranavi pujith------------------'
s.ljust(60,'_')
    
'sarayu sai pranavi pujith___________________________________'
s.rjust(60,'_')
    
'___________________________________sarayu sai pranavi pujith'
'50'.zfill(4)
    
'0050'
'200'.zfill(3)
    
'200'
'400'.zfill(4)
    
'0400'
s.find('a')
    
1
s.find('p')
    
11
s.find('z')
    
-1
s.rfind('s')
    
7
s.index('p')
    
11
s.rindex('u')
    
20
s.count('i')
    
3
s.count('a')
    
5
s.split()
    
['sarayu', 'sai', 'pranavi', 'pujith']
s.split(' ',2)
    
['sarayu', 'sai', 'pranavi pujith']
s.rsplit(' ',2)
    
['sarayu sai', 'pranavi', 'pujith']
s.partition(' ')
    
('sarayu', ' ', 'sai pranavi pujith')
s.partition('A')
    
('sarayu sai pranavi pujith', '', '')
s=['multi','line','comment']
    
''.join(s)
    
'multilinecomment'
'@'.join(s)
    
'multi@line@comment'
>>> s='     hello    world     '
...     
>>> s.strip()
...     
'hello    world'
>>> s.lstrip()
...     
'hello    world     '
>>> s.rstrip()
...     
'     hello    world'
>>> s='python'
...     
>>> s.replace('python','java')
...     
'java'
>>> s.replace('p'.'*')
...     
SyntaxError: invalid syntax
>>> s.replace('p','*')
...     
'*ython'
>>> s.maketrans('aeiou','******')
...     
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    s.maketrans('aeiou','******')
ValueError: the first two maketrans arguments must have equal length
>>> s.maketrans('aeiou','*****')
...     
{97: 42, 101: 42, 105: 42, 111: 42, 117: 42}
>>> s.translate(s.maketrans('aeiou','*****'))
...     
'pyth*n'
>>> s='Hello@'
...     
>>> s.encode()
...     
b'Hello@'
>>> s.decode()
...     
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    s.decode()
AttributeError: 'str' object has no attribute 'decode'. Did you mean: 'encode'?
>>> b'Hello@'.decode()b'Hello@'
...     
SyntaxError: invalid syntax
