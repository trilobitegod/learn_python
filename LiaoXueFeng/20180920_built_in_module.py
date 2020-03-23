# \usr\bin\env python3
# -*- coding: utf-8 -*-

from contextlib import contextmanager

class Query(object):
	
	def __init__(self,name):
		self.name=name
		
	def query(self):
		print('Query info about %s...' % self.name)
		
@contextmanager
def create_query(name):
	print('Begin')
	q = Query(name)
	yield q
	print('End')

#在代码执行前后自动执行yield前后代码	
with create_query(5) as q:
	q.query()
	print('hello')
	print('world')
	

	
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)