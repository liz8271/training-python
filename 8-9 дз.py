import numpy as np
f = open('C:\\Users\\LIZA\\Desktop\\ml\\input.txt',encoding='utf-8')
f1 = open('C:\\Users\\LIZA\\Desktop\\ml\\output.txt','w')
a=np.array(f.readline().split(),float)
f1.writelines(f'{np.median(a):.2f}'+' '+f'{np.mean(a):.2f}'+' '+f'{np.std(a):.2f}')
f.close()
f1.close()

import numpy as np
with open("input.csv", 'r') as table, open("output.txt", 'w') as fout:
    data = np.array([list(map(int, line.rstrip().split(','))) for line in table.readlines()])
    fout.write(str(np.argmax(np.sum(data, axis = 0)) + 1))

import numpy as np
with open('input.csv') as table:
    data = np.array([list(map(int, line.rstrip().split(','))) for line in table.readlines()])
    c=0
    n=np.std(data,axis=1)
    for i in n:
        c+=int(abs(i)<=4)
    print(int(c<=(len(n)-c))+1)

import numpy as np
with open("input.csv", 'r') as fin, open("output.csv", 'w') as fout:
    data = np.array([list(map(float, line.rstrip().split(','))) for line in fin.readlines()])
    data[::2, 1::2] /= 2
    data[1::2, ::2] /= 2
    np.savetxt(fout, data, fmt="%g", delimiter=",")

import numpy as np
with open("C:\\Users\\LIZA\\Desktop\\ml\\test.csv", 'r') as fin, open("output.csv", 'w') as fout:
    data = np.array([list(map(float, line.rstrip().split(','))) for line in fin.readlines()])
    avg_wins = np.mean(data, axis=0) 
    data[0, :] = np.floor(avg_wins * 1.5)
    np.savetxt(fout, data,fmt="%d", delimiter=',')

import itertools
B = (False, True)
count = 0
for K, L, M in itertools.product(B, B, B):
    if (not K and L and not M)or(not K and L and M)or(K and not L and not M): print(K, L, M)

import pandas as pd
with open('input.csv') as f:
    df=pd.read_csv(f,names=['1','2','3','4','5','6','7','8','9','10'])
    print(int(df.columns.values[df.mean().values.argmin()]))

import pandas as pd
data = pd.read_csv("input.csv")
df = pd.DataFrame(data)
print(data.columns.values[df.mean().values.argmax()])

import pandas as pd
with open('input.csv') as f:
    df=pd.read_csv(f)
    a=df.sum().values.sum()
    if a>=8000000:print(1, end=' ')
    else:print(0, end=' ')
    print(df.columns.values[df.sum().values.argmax()])

import pandas as pd
data = pd.read_csv("C:\\Users\\LIZA\\Desktop\\ml\\demodata.csv")
print(data[(data.weekdays == 'Thu') & (data.prices > 2000000)])
#print(data[data.weekdays == 'Thu' & data.prices > 2000000]) 
#print(data[(weekdays == 'Thu') & (prices > 2000000)])
print(data.query('weekdays == "Thu" and prices > 2000000'))

import pandas as pd
with open('input.csv') as f:
    df=pd.read_csv(f)
    a=df[(df.a+df.b>df.c)&(df.a+df.c>df.b)&(df.b+df.c>df.a)==True]
    print(a.count()[0])


    