# /usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal(object):
	def run(self):
		print('Animal is running...')
		
class Dog(Animal):
	
	def run(self):
		print('Dog is running...')
		
	def eat(self):
		print('Eating meat...')
	
class Cat(Animal):
	pass
	
def run_twice(animal):
	animal.run()
	animal.run()
	
dog=Dog()
dog.run()
run_twice(Animal())
run_twice(Dog())

print(isinstance(dog,Animal))
print(isinstance(dog,Dog))
print(isinstance(dog,Cat))


class Student(object):
	def __init__(self,name):
		self.name=name
s=Student('Bob')
s.score=90
s.city=BeiJing