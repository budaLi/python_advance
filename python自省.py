#-*- coding:utf8 -*-
#author : Lenovo
#date: 2018/9/17

#自省就是面向对象的语言所写的程序在执行时，能知道对象的类型，也就说在运行时能知道对象的类型
#比如 type(),dir(),getattr(),hasattr(),isinstance()

a=1
b='ss'
print(type(a))
print(dir(b))   #得到b可使用的一些函数
print(isinstance(a,str))
print(hasattr(a,'name'))    #判断对象是否有某种属性
print(getattr(a,'imag'))
