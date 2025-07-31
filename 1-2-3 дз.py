n=int(input())
for i in range(n):
    print('*'*n)

s=input()
print(len(s))

s=input()
print(s[::-1])

s=input()
print(s[:s.find('@')])

print(input().split('"')[1])

s=input()
print(s.split()[1],s.split()[0])

s=input()
s=s.replace(' ','')
s=s.replace('(','')
s=s.replace(')','')
s=s.replace('-','')
print(s)

s=input()
for c in s:
    if c.isalpha():
        c=chr(ord(c)+1)
    print(c,end='')

f = open('input.txt')
for i in f.readline().split(' '):
    print(i[::-1],end=' ')

f = open('input.txt')
for i in f.readlines():
    if 'ё' in i: print(i,end='')

f = open('input.txt')
for i in f.readlines():
    print(" ".join(i.split()[::2]))

f = open('input.txt')
f1 = open('output.txt','w')
n=int(f.readline())
l=f.readlines()
for i in range(n):
    f1.write(l[i].replace('\n','')+'\t'+l[i+n])
f.close()
f1.close()

import itertools as it
f = open('studygroup.txt')
j=list(it.combinations(f.readline().split(), 3))
for i in range(len(j)):
    print('1: '+j[i][0]+' 2: '+j[i][1]+' 3: '+j[i][2])
f.close()
