#!/usr/bin/env python3

def fact_gen():
    n= 1
    x= 1
    while True:
        yield x
        n += 1
        x = x*n
        
def fac1(n):
    if n == 0:
        return 1
    else:
        return n*fac1(n-1)
    
def fac2(n):
    i=1
    while n>=1:
        i = i * n
        n = n-1
    return i

def fac3(n):

    List=[]
    f = fact_gen()
    for _ in range(n):
        i = next(f)
        List.append(i)

    return (List[-1])

fac1(9)
fac2(9)
fac3(9)
#print(fac1())
#print(fac2())
#print(fac3())