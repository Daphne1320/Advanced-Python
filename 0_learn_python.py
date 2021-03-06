# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 22:21:31 2018

@author: zouco
"""

this_string = '''dkljglakg:
dgfakdgja
    dfj'gadg'
"jdlfkaj"
'''
print(this_string)   


# v2:  int, long, float, complex
y = 1+2j
type(y)
print(y.real)
print(y.imag)

print(36/7)
print(36%7)

# v3:   int, float, complex
# int is unlimited
print(36//7)


# self learn of python
dir()
dir('__builtins__')
help(repr)
a='dgadf dga'
print(a)
repr(a)
eval(repr(a))==a

a='dgadfag'
dir(a)


# math
import math
dir(math)
math.ceil(3.4)


# non-trial -> True
int(True)

# random
import random

# uniform
for i in range(100):
    print(random.random())

for i in range(100):
    print(random.uniform(1,10))

print(random.randint(5))
print(random.choice(['a','b','c']))


# normal
random.normalvariate(0,1)




# simples IO
input_1 = input('pls input something:\n')
print(input_1)


# function input
def cm(f=0,i=0):
    print(f+i)
    return f+i

cm(3)
cm(i=1)


# set
set1=set()
set1.add(1)
set1.remove(2)
set1.discard(2) # without error

set2={3,4,5}
set1.union(set2)
set1.intersection(set2)

# dictionary
dikt = {}
dikt.get('dg', None)
dikt.keys()


# yield
def generator():
    for i in range(10):
        yield i

# use 1
g=generator()
print(next(g))
print(next(g)) 

# use 2
for i in g:
    print(i)
    
    
# simple version of yield
g = (i for i in range(10))
print(list(g))


# tuple is smaller
import sys
a = (1,2,3,4,5)
sys.getsizeof(a)

# tuple assignment, works also for list
q,w,e,r,t = a
print(w)


# use lambda to create function generator
def qua(a,b,c):
    return lambda x: a*x**2 +b*x+c

f = qua(2,1,3)
f(2)    



# filter
filter(lambda x: x>2, list_x)  # return qualified ones, same as map it do not return list
filter(None, list_x)
print(x, file=f)







# datetime
import datetime
gvr = datetime.date(1993,8,8)
lauch_time = datetime.time(23,12,10)

# print time
print(gvr)
print(gvr.strftime('%A, %B %d'))

print(datetime.datetime.strptime('07/20/1969', '%m/%d/%Y'))
print(datetime.datetime.strptime('07:06:05', '%H:%M:%S'))
print(datetime.datetime.strptime('07:06:05', '%X'))

print(gvr.day)
gvr + 100
gvr + datetime.timedelta(days=100)
gvr + datetime.timedelta(seconds=100000)

(datetime.datetime.today()-gvr).days





# logging
import logging
logging.basicConfig(filename='logger01.log')
logger1=logging.getLogger()
logger1.info('what')
print(logger1.level)

# levels : debug, Info, warning, error, critical
logging.basicConfig(filename='logger01.log', level = logging.DEBUG)
logger1=logging.getLogger()
logger1.info('what')

log_format = '%(levelname)s %(asctime)s - %(message)s'
logging.basicConfig(filename='logger01.log',  file_mode = 'a', level = logging.DEBUG, format = log_format)
logger1=logging.getLogger()
logger1.info('what')






# recursive function
def fibonacci(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    elif n>=2:
        return fibonacci(n-1) + fibonacci(n-2)


fibonacci_cache = {0:1, 1:1}

def fibonacci_fast(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    
    if n>=2:
        value = fibonacci(n-1) + fibonacci(n-2)
        # enlarge the cache
        fibonacci_cache[n] = value
        return value

from functools import lru_cache

@lru_cache(maxsize=1000)
def fibonacci_fast2(n):
    # check the input...
    # ...
    
    if n==0:
        return 1
    elif n==1:
        return 1
    elif n>=2:
        value = fibonacci(n-1) + fibonacci(n-2)
        return value


# class
# class can take variable out of definition






# JSON is slight different defined dictionary in Python
    
import json
with open('... .txt','w',encoding = 'utf-8') as f:
    json.dump(a_dict, f, ensure_ascii = False)
with open('... .txt','r',encoding = 'utf-8') as f:
    a_dict = json.load(f)



# change between json_file_string and dict
json.loads(a_string_of_json_file) # this will output a dict
json.dumps(a_dict, ensure_ascii = False, sort_keys=True, indent=4) # this will output a json_file_string








import winsound
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)


####################################################################
# simplify the program by math:
def is_prime(n):
    if n==1:
        return False
    
    if n==2:
        return True
    
    if n >2 and n%2 == 0:
        return False
    
    max_divisor = math.floor(math.sqrt(n))
    for d in range(3, 1 + max_divisor, 2):
        if n%d == 0:
            return False
    return True
###################################################################