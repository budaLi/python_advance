#-*- coding:utf8 -*-
#author : Lenovo
#date: 2018/9/17

#列表推导式

lis=[i for i in range(1,100,5)]
print(lis)

#字典推导式

dic={key :value for key,value in enumerate(lis)}
print(dic)