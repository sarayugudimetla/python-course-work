Python 3.14.5 (v3.14.5:5607950ef23, May 10 2026, 07:38:09) [Clang 21.0.0 (clang-2100.0.123.102)] on darwin
Enter "help" below or click "Help" above for more information.

================================================================================================ RESTART: /Users/abhi/Documents/Day-9.py ===============================================================================================
Traceback (most recent call last):
  File "/Users/abhi/Documents/Day-9.py", line 3, in <module>
    n=int(input("enter",i,"number:"))
TypeError: input expected at most 1 argument, got 3

================================================================================================ RESTART: /Users/abhi/Documents/Day-9.py ===============================================================================================
enter the number:1
enter the number:2
enter the number:3
enter the number:4
enter the number:
Traceback (most recent call last):
  File "/Users/abhi/Documents/Day-9.py", line 3, in <module>
    n=int(input("enter the number:"))
ValueError: invalid literal for int() with base 10: ''

================================================================================================ RESTART: /Users/abhi/Documents/Day-9.py ===============================================================================================
0
1
2
3
4

================================================================================================ RESTART: /Users/abhi/Documents/Day-9.py ===============================================================================================
j
g
d
h
w
j
e
d
u
h
g
s
v
b

================================================================================================ RESTART: /Users/abhi/Documents/Day-9.py ===============================================================================================
1
2
3
4
5
for i in range(11):
    print(i)

    
0
1
2
3
4
5
6
7
8
9
10
for i in range(2,1001,2):
    print(i)

    
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
42
44
46
48
50
52
54
56
58
60
62
64
66
68
70
72
74
76
78
80
82
84
86
88
90
92
94
96
98
100
102
104
106
108
110
112
114
116
118
120
122
124
126
128
130
132
134
136
138
140
142
144
146
148
150
152
154
156
158
160
162
164
166
168
170
172
174
176
178
180
182
184
186
188
190
192
194
196
198
200
202
204
206
208
210
212
214
216
218
220
222
224
226
228
230
232
234
236
238
240
242
244
246
248
250
252
254
256
258
260
262
264
266
268
270
272
274
276
278
280
282
284
286
288
290
292
294
296
298
300
302
304
306
308
310
312
314
316
318
320
322
324
326
328
330
332
334
336
338
340
342
344
346
348
350
352
354
356
358
360
362
364
366
368
370
372
374
376
378
380
382
384
386
388
390
392
394
396
398
400
402
404
406
408
410
412
414
416
418
420
422
424
426
428
430
432
434
436
438
440
442
444
446
448
450
452
454
456
458
460
462
464
466
468
470
472
474
476
478
480
482
484
486
488
490
492
494
496
498
500
502
504
506
508
510
512
514
516
518
520
522
524
526
528
530
532
534
536
538
540
542
544
546
548
550
552
554
556
558
560
562
564
566
568
570
572
574
576
578
580
582
584
586
588
590
592
594
596
598
600
602
604
606
608
610
612
614
616
618
620
622
624
626
628
630
632
634
636
638
640
642
644
646
648
650
652
654
656
658
660
662
664
666
668
670
672
674
676
678
680
682
684
686
688
690
692
694
696
698
700
702
704
706
708
710
712
714
716
718
720
722
724
726
728
730
732
734
736
738
740
742
744
746
748
750
752
754
756
758
760
762
764
766
768
770
772
774
776
778
780
782
784
786
788
790
792
794
796
798
800
802
804
806
808
810
812
814
816
818
820
822
824
826
828
830
832
834
836
838
840
842
844
846
848
850
852
854
856
858
860
862
864
866
868
870
872
874
876
878
880
882
884
886
888
890
892
894
896
898
900
902
904
906
908
910
912
914
916
918
920
922
924
926
928
930
932
934
936
938
940
942
944
946
948
950
952
954
956
958
960
962
964
966
968
970
972
974
976
978
980
982
984
986
988
990
992
994
996
998
1000

s={"fdgshdjhb","sfhwjsdh","wekdjfhgbe",1,2,4}
for i in s:
    print(i)

    
1
2
4
sfhwjsdh
wekdjfhgbe
fdgshdjhb
d={"abhi":10,"prannu":20}
for i in d:
    print(i)

    
abhi
prannu
for i in d:
    print(i,d[i])

    
abhi 10
prannu 20
#range---> (start,stop+1,step)

n=0
while n<10:
    print(n)
    n=n+1

    
0
1
2
3
4
5
6
7
8
9
n=1
while n<11:
    print(n)
    n=n+2
    
SyntaxError: multiple statements found while compiling a single statement
n=1
while n<11:
    print(n)
    n=n+2
    

SyntaxError: multiple statements found while compiling a single statement
for i in range(5,101,5):
    print(i)

    
5
10
15
20
25
30
35
40
45
50
55
60
65
70
75
80
85
90
95
100
alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(len(alpha)):
    print(i,alpha[i])

    
0 A
1 B
2 C
3 D
4 E
5 F
6 G
7 H
8 I
9 J
10 K
11 L
12 M
13 N
14 O
15 P
16 Q
17 R
18 S
19 T
20 U
21 V
22 W
23 X
24 Y
25 Z
alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(len(alpha)+1):
    print(i,alpha[i])
    
SyntaxError: multiple statements found while compiling a single statement

alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(len(alpha)):
    print(i,alpha[i])
    
SyntaxError: multiple statements found while compiling a single statement
alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(len(alpha)):
    print(i,alpha[i])
    
SyntaxError: multiple statements found while compiling a single statement
a="123456789"
for i in enumerate(a):
    print(i)

    
(0, '1')
(1, '2')
(2, '3')
(3, '4')
(4, '5')
(5, '6')
(6, '7')
(7, '8')
(8, '9')
a=["1","2","3",4]
for i in enumerate(a):
    print(i)

    
(0, '1')
(1, '2')
(2, '3')
(3, 4)
for i in range(1,11):
    if i=3
    
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>> for i in range(1,11):
...     if i=3:
...         
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>> for i in range(1,11):
...     if i==3:
...         continue
... 
...     
>>> 
>>> 
>>> 
================================================================================================ RESTART: /Users/abhi/Documents/Day-9.py ===============================================================================================
1
3
5
7
9
11
13
15
17
19
>>> 
================================================================================================ RESTART: /Users/abhi/Documents/Day-9.py ===============================================================================================
Enter the Pin Number:1234
Incorrect Pin
Incorrect Pin
Incorrect Pin
Incorrect Pin
Incorrect Pin
>>> 
================================================================================================ RESTART: /Users/abhi/Documents/Day-9.py ===============================================================================================
Enter the Pin Number:1234
Incorrect Pin
Enter the Pin Number:1234
Incorrect Pin
Enter the Pin Number:2307
Incorrect Pin
Enter the Pin Number:2307
Incorrect Pin
Enter the Pin Number:2307
Incorrect Pin
>>> 
================================================================================================ RESTART: /Users/abhi/Documents/Day-9.py ===============================================================================================
Enter the Pin Number:12345
Incorrect Pin
Enter the Pin Number:2345
Incorrect Pin
Enter the Pin Number:123
Unlock the Phone
Try After 5 Minutes
>>> 
================================================================================================ RESTART: /Users/abhi/Documents/Day-9.py ===============================================================================================
Enter the Pin Number:1234
Incorrect Pin
Enter the Pin Number:1234
Incorrect Pin
Enter the Pin Number:1234
Incorrect Pin
Enter the Pin Number:1234
Incorrect Pin
Enter the Pin Number:1234
Incorrect Pin
Try After 5 Minutes
>>> 
================================================================================================ RESTART: /Users/abhi/Documents/Day-9.py ===============================================================================================
Enter the Pin Number:123
Unlock the Phone
