#-*- coding:utf8 -*-
#author : Lenovo
#date: 2018/9/17

S=[i for i in range(1,10)]
print(S)

#[1, 2, 3, 4, 5, 6, 7, 8, 9]
#列表

#思考 将列表生成式中的[]改为()数据结构是否会发生改变？

#---------------------------------------------------------


#会发生改变 从列表变为生成器

SS=(i for i in range(1,10))
print(SS)
for one in SS:
    print(one)
#<generator object <genexpr> at 0x0000000002C83A68>

#通过列表生成式，可以直接创建一个列表 ，但由于内存限制 ，列表的容量肯定是有限的，
#这样我们可以通过生成器