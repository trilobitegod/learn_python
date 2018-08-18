#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#generator
def YH(max):
	n=0
	b=[]
	while n<max:
		len_b=len(b)
		a=[]
		for bi in list(range(0,len_b+1)):
			if bi==0 or bi==len_b:
				a.append(1)
			else:
				a.append(b[bi-1]+b[bi])
		b=a
		n=n+1
		yield b
	return n
yh=YH(5)
while True:
	try:
		x=next(yh)
		print(x)
	except StopIteration as e:
		print('Generator return value:', e.value)
		break
		
#map,reduce,filter		
def is_palindrome(n):
	n_str=str(n)
	n_rev=n_str[::-1]
	return n_str==n_rev
	
a=list(filter(is_palindrome,[1221,12321,1123,'adfda','adf']))
print(a)

#decorator
def log(text):
	def decorator(func):
		def wrapper(*args,**kw):
			print('%s %s():' % (text,func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator
@log('execute')
def now():
	print('2018-08-17')
	
f=now
f()

#partial function
import functools
int3=functools.partial(int,base=3)		#输入参数int为base=3进制
print(int3('1000000'))