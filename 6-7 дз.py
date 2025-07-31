from collections import Counter
print(Counter(input()).most_common(1)[0][0])

f = open('input.txt')
a=set()
for i in f.readlines():
    a.add(i.split()[1])
print('\n'.join(sorted(a,key=len)))

f = open('input.txt')
a=set()
b=set()
for i in f.readlines():
    if i.split()[2]=='male': a.add(i.split()[1])
    else: b.add(i.split()[1])
if len(a.intersection(b))==0: print(0)
else: print('\n'.join(sorted(a.intersection(b),key=len)))

from collections import Counter
a=[]
with open('input.txt') as f:
    for i in f.readlines():
        a.append(i.split()[1])
for i in range(len(Counter(a).most_common())):
    print(Counter(a).most_common()[i][0], '-', Counter(a).most_common()[i][1])

a={}
with open('input.txt') as f:
    for i in f.readlines():
        a.setdefault(i.split()[1],[]).append(i.split()[0])
for i in sorted(a.keys(),key=len):
    print(i,': ', ', '.join((sorted(a[i]))),sep='')

def bin_search(lst):
    low = 0
    high = len(lst)-1
    while low <= high:
        mid = (low + high)//2
        if int(lst[mid]) == 1415: return mid
        if int(lst[mid]) > 1415: high = mid - 1
        else: low = mid + 1
        
import numpy as np
f = open('input.txt')
f1 = open('output.txt','w')
a=np.linspace(float(f.readline()),float(f.readline()),int(f.readline()))
a[::7]=a[::7]/3
a[4::7]=a[4::7]*2
f1.writelines(f'{i:.2f}'+'\n' for i in list(a))
f.close()
f1.close()