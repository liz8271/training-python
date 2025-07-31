import pandas as pd
df=pd.read_csv('input.csv')
a=df.dropna(subset=['name'])['score'].mean()
s=df.dropna(subset=['name']).fillna(a)
s.to_csv('output.csv')

import pandas as pd
df=pd.read_csv('input.csv')
a=df['temperature_c'].apply(lambda x:round(x*1.8+32))
df['temperature_f']=a
df.to_csv('output.csv')

import pandas as pd
df=pd.read_csv('input.csv')
if df.empty:df.drop(columns=['ID','Тип операции']).to_csv('output.csv',index=False,encoding='utf8')
else:
    df.loc[df['Тип операции']=='Вывоз','Объем груза']=df['Объем груза']*(-1)
    df.drop(columns=['ID','Тип операции']).groupby("Фамилия водителя").sum().sort_values(by='Объем груза', ascending=False).to_csv('output.csv',encoding="utf8")

import pandas as pd
df=pd.read_csv('input.csv')
df['Уникальных маршрутов']=df['Город отправления']+df['Город прибытия']
df=df.drop(columns=['ID','Город отправления','Город прибытия'])
if df.empty: df.to_csv('output.csv',index=False,encoding='utf8')
else:
    sum=df.groupby(['Номер борта']).nunique()
    res=pd.DataFrame()
    res['Номер борта']=list(sum.index)
    res['Уникальных маршрутов']=sum.values[:,0]
    res.sort_values(by=['Уникальных маршрутов','Номер борта'],ascending=(False,True)).to_csv('output.csv',encoding='utf8',index=False)

class Incapsulator:
    def __init__(self,value=0):
        self.__value=value
    def set_value(self,num):
        self.__value=num
    def get_value(self):
        return self.__value

class Student:
    def __init__(self,name,age):
        self._name=name
        self._age=float(age)
    def __str__(self):
        return "Student "+self._name+" of age "+str(self._age)
    def __repr__(self):
        return f"Student({self._name}, {self._age})"

class SpyingNumber:
    count=0
    def __init__(self,val):
        self.__val=val
    def __str__(self):
        return str(self.__val)
    def __repr__(self):
        return f"SpyingNumber({self.__val})"
    def _inc(func):
        def inte(cls, *args, **kwargs):
            result = func(cls, *args, **kwargs)
            cls.increase()
            return result
        return inte
    @_inc
    def __add__(self, other):
        if isinstance(other, (int, float)):
            other = SpyingNumber(other)
        return SpyingNumber(self.__val+other.__val)
    @_inc
    def __sub__(self, other):
        if isinstance(other, (int, float)):
            other = SpyingNumber(other)
        return SpyingNumber(self.__val-other.__val)
    @_inc
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            other = SpyingNumber(other)
        return SpyingNumber(self.__val*other.__val)
    @_inc
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            other = SpyingNumber(other)
        return SpyingNumber(self.__val/other.__val)
    @classmethod
    def  increase(cls):
        cls.count+=1
    @classmethod
    def  get_global_counter(cls):
        return cls.count
    @classmethod
    def reset_global_counter(cls):
        cls.count=0
        return cls.count

