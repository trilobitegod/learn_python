#!/usr/bin/env python3
# -*- coding: utf-8 -*-

L=['Bart','Lisa','Adam']
for name in L:
	print('Hello,',name)

#函数定义中的参数
def f1(a,b,c=0,*args,**kw):		#*args可变参数，**kw可变关键字参数
	sum=0
	for n in args:
		sum=sum+n
	if 'city' in kw:
		pass
	if 'job' in kw:
		pass
	print(a,b,c,sum,kw)
	return a,b
def f2(a,b,c=0,*,country,**kw):		#*后关键字参数
	print(a,b,c,country,kw)
	
nums=[1,2,3]
extra={'city':'BeiJing','job':'Student','addr':'12345'}
a,b=f1(1,2,3,*nums,**extra)
print(a,b)
f2(1,2,3,country='China',**extra)

#递归函数
def fact(n):
	if n==1:
		return 1
	return n*fact(n-1)
fact(5)