#-*- coding:utf8 -*-
#author : Lenovo
#date: 2018/9/17

# class A:
#     def __int__(self,name):
#         self.name=name
#
# a=A()
# a.name='123'
# print(a.name)

#上述例子中类中的变量可以访问到

# class B(object):
#     def __int__(self):
#         self._name='sss'
#
# b=B()
# print(b._name)

#只是无法import ，其他方面和不加下划线一样

class C(object):
    def __int__(self):
        self.__name='sss'

c=C()
print(c.__name)


#私有变量 通过反射机制可以访问