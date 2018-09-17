#-*- coding:utf8 -*-
#author : Lenovo
#date: 2018/9/17

a=1
print('a:{}'.format(id(a)))
def fun(a):
    a=2
    print('fun_a:{}'.format(id(a)))

fun(a)
print('a:{}'.format(id(a)))
print(a)

#上面代码可以看到a的值还是1  说明函数并没有对a起作用
#python中对象有两种 不可变对象 string tuple number 可变对象 list dict set
#当函数中对一个不可变对象赋值时 并不会发生改变



b=[]
def funb(b):
    b.append('b')

funb(b)
print(b)

#列表为可变的 对函数内的操作相当于对它进行操作 结果为['b']

#总结
#当一个引用传递给函数的时候，函数会复制一份引用，当值为不可变引用时，不会发生变化，除非在函数内部重新
#定义一个相同名称的变量覆盖 并return 在函数执行的时候接受 其值会发生改变

#而当引用的为可变对象时，对它的操作相当于定位了它的指针 其值会发生改变