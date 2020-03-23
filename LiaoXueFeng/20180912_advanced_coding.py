# /usr/bin/env python3
# -*- coding: utf-8 -*-

from types import MethodType

class Student(object):
	__slots__ = ('name','age','set_age')	#tuple定义允许绑定的属性名称
	pass
	
def set_age(self,age):
	self.age=age
	
s=Student()
s.name='Michael'
s.set_age=MethodType(set_age,s)
s.set_age(25)
print(s.age)