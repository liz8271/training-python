s=input()
x=0
for i in range(len(s)):
    x+=int(s[::-1][i])*2**i
print(x)

from fractions import Fraction
[a1,a2]=list(map(int,input().split()))
[b1,b2]=list(map(int,input().split()))
[c1,c2]=list(map(int,input().split()))
a=Fraction(a1,a2)
b=Fraction(b1,b2)
c=Fraction(c1,c2)
print(f"{float(b/a+b/(a+c)-c/(c-a)):0.4f}")

s=n=0
c=int(input())
while c!=0:
    s+=c
    n+=1 
    c=int(input())
print(n,s)

[b,q,a]=list(map(float,input().split()))
i=1
while b<a:
    b*=q
    i+=1
print(i)

[amount,period,rate]=list(map(float,input().split()))
rate_month = rate / 12.0 / 100.0
period*=12
csv_filename = 'output.csv'
with open(csv_filename, 'w') as csv_file:
    total_amount = amount
    loan_months = 1
    additional_sum =0
    labels = ("Месяц","Сумма на вкладе","Начисление")
    print(*labels, sep=',', file=csv_file)
    while loan_months<=period:
        additional_sum = total_amount * rate_month
        total_amount+=additional_sum
        print(f"{loan_months},{total_amount:0.2f},{additional_sum:0.2f}", file=csv_file)
        loan_months += 1

f = open('weights.txt')
f1 = open('team.txt','w')
a=sorted([i.split() for i in f.readlines()], key=lambda x: float(x[1]),reverse=True)
f1.writelines(' '.join(i)+'\n' for i in a[::2])
f1.writelines(' '.join(i)+'\n' for i in a[1::2])
f.close()
f1.close()

f = open('poe_unpublished.txt')
f1 = open('poe_decode_attempt.txt','w')
f1.writelines(' '.join(i)+'\n' for i in sorted([sorted(i.split(),key=len) for i in f.readlines()],key=len))
f.close()
f1.close()

f = open('med_research.txt')
f1 = open('output.txt','w')
a=[i.split() for i in f.readlines()]
for i in range(len(a[0])):
    for j in range(len(a)):
        f1.write(a[j][i]+' ')
    f1.write('\n')
f.close()
f1.close()

f = open('the_calls.txt')
f1 = open('calls.txt','w')
a=sorted([i.rstrip().split('\t') for i in f.readlines()],key=lambda x: int(x[1]), reverse=True)
f1.writelines('\t'.join(i)+'\n' for i in a if i[2]=='A')
f1.writelines('\t'.join(i)+'\n' for i in a if i[2]=='B')
f.close()
f1.close()