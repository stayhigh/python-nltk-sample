# -*- coding: utf-8 -*-
from functools import partial 

def f(a, b, c, d):
    print (a, b, c, d)
    
g = partial(f,1,2,3)
g(4)


print "NOW, LET CURRY IT!"
def f1(a,b,c):
    def f2(b,c):
        print "b is the Manager"
        def f3(c):
            print "c is the employee"
        return f3(c)
    print "a is the boss."
    return f2(b,c)

f1("Patric", "Harry","John")


#decorator usage
def my_wrapper(f):
    arg1 = 1
    arg2 = 2
    print "f(arg1,arg2):",f(arg1,arg2)
    print "arg1:",arg1
    print "arg2:",arg2
    

@my_wrapper
def firstf(a,b):
    print "a:",a
    print "b:",b
    
#Incremental binding sample code
import functools
def simpleFunc(a,b,c,d,e,f,g = 100):
    print (a,b,c,d,e,f,g)

""" 
def curry(func, *args, **kwargs):
    def curried(*args, **kwargs):
        if not args and not kwargs:
            return func()
        return functools.partial(func, *args, **kwargs)
    return curried
"""

#generic curry in python
def curry(func):
    def g(*myArgs, **myKwArgs):
        def f(*args, **kwArgs):
            if len(args) or len(kwArgs):    # some more args!
                newArgs = myArgs + args
                newKwArgs = dict.copy(myKwArgs);
                newKwArgs.update(kwArgs)
                return g(*newArgs, **newKwArgs)
            else:                           # time to evaluate...
                func(*myArgs, **myKwArgs)
        return f
    return g




print "----curry the function------"
f = curry(simpleFunc) # curry the 1st parameter into function c1
c1 = f(1)
c2 = c1(2, d = 4)               # Note that c is still unbound
c3 = c2(3)(f = 6)(e = 5)        # now c = 3
c3()                            # () forces the evaluation              <====
                                #   it prints "1 2 3 4 5 6 100"
c4 = c2(30)(f = 60)(e = 50)     # now c = 30
c4()                            # () forces the evaluation              <====
                                #   it prints "1 2 30 4 50 60 100"

