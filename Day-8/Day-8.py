Python 3.14.5 (v3.14.5:5607950ef23, May 10 2026, 07:38:09) [Clang 21.0.0 (clang-2100.0.123.102)] on darwin
Enter "help" below or click "Help" above for more information.
s=set{}
SyntaxError: invalid syntax
s=set()
type(s)
<class 'set'>
s={}
type(s)
<class 'dict'>
s={1,2,3,4,5,5,4,3,2,1}
s
{1, 2, 3, 4, 5}
s
{1, 2, 3, 4, 5}
s
{1, 2, 3, 4, 5}
s
{1, 2, 3, 4, 5}
s.ppend(1)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    s.ppend(1)
AttributeError: 'set' object has no attribute 'ppend'
s.append(1)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s.append(1)
AttributeError: 'set' object has no attribute 'append'
s
{1, 2, 3, 4, 5}
s
{1, 2, 3, 4, 5}
s.add(1)
s.add(1.2345)
s.add(3+8j)
s.add([1,2,3])
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    s.add([1,2,3])
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
s.add({1,23,4})
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    s.add({1,23,4})
TypeError: cannot use 'set' as a set element (unhashable type: 'set')
s.add((1,2))
s
{1, 2, 3, 4, 5, 1.2345, (1, 2), (3+8j)}
s.add(True)
s.add(False)
s
{False, 1, 2, 3, 4, 5, 1.2345, (1, 2), (3+8j)}
{False, 1, 2, 3, 4, 5, 1.2345, (1, 2), (3+8j)}
{False, 1.2345, 2, (1, 2), 1, 3, 4, 5, (3+8j)}
s
{False, 1, 2, 3, 4, 5, 1.2345, (1, 2), (3+8j)}
1 in s
True
(1,2) not in s
False
]
(1,2345,345) not is s
SyntaxError: invalid syntax
(1,2345,345) not in s
True
a=set()
o="raceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    s.add([1,2,3])
TypeError: cannot use 'list' as a set element (unhashable type: 'list')"
SyntaxError: unterminated string literal (detected at line 1)
s
{False, 1, 2, 3, 4, 5, 1.2345, (1, 2), (3+8j)}
o
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    o
NameError: name 'o' is not defined
hash(10)
10
hash("asdhgshj")
-6897090513713771952
hash("Python")
-596916059223226628
s
{False, 1, 2, 3, 4, 5, 1.2345, (1, 2), (3+8j)}
a={1,2,3}
b={4,5,6}
a|b
{1, 2, 3, 4, 5, 6}
b={4,5,6,1,2}
a
{1, 2, 3}
b
{1, 2, 4, 5, 6}
a & b
{1, 2}
b-a
{4, 5, 6}
a-b
{3}
{1,2}<=a
True
{1,2}>=a
False
a
{1, 2, 3}
b
{1, 2, 4, 5, 6}
c
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    c
NameError: name 'c' is not defined
a.union(b)
{1, 2, 3, 4, 5, 6}
a.union b
SyntaxError: invalid syntax
c=a.union(b)
c
{1, 2, 3, 4, 5, 6}
a,b,c
({1, 2, 3}, {1, 2, 4, 5, 6}, {1, 2, 3, 4, 5, 6})
>>> a{1}
SyntaxError: invalid syntax
>>> a
{1, 2, 3}
>>> b
{1, 2, 4, 5, 6}
>>> b.add(3)
>>> b
{1, 2, 3, 4, 5, 6}
>>> b.add(16)
>>> b
{16, 1, 2, 3, 4, 5, 6}
>>> b.update({11,456789,987654})
>>> b
{1, 2, 3, 4, 5, 6, 987654, 11, 16, 456789}
>>> b.delete()
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    b.delete()
AttributeError: 'set' object has no attribute 'delete'
>>> d.pop()
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    d.pop()
NameError: name 'd' is not defined. Did you mean: 'id'?
>>> b.remove()
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    b.remove()
TypeError: set.remove() takes exactly one argument (0 given)
>>> b.remove(1)
>>> b
{2, 3, 4, 5, 6, 987654, 11, 16, 456789}
>>> 
>>> 
>>> 
>>> b.pop()
2
>>> b
{3, 4, 5, 6, 987654, 11, 16, 456789}
>>> b.remove(2)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    b.remove(2)
KeyError: 2
>>> b.discard(2)
>>> b
{3, 4, 5, 6, 987654, 11, 16, 456789}
>>> 
>>> 

>>> 
>>> 

>>> 

... 
>>> 

>>> 

>>> 

>>> f=frozenset({1,2,3})
>>> f
frozenset({1, 2, 3})
>>> len(f)
3
>>> sum(f)
6
