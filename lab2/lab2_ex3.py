#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Amit
#
# Created:     25/03/2025
# Copyright:   (c) Amit 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math
def main():
    pass

if __name__ == '__main__':
    main()
def integrate(f, a, b, n=1000):
    dx= (b-a)/n
    sum=0
    x=a
    while(x<b):
        sum+=dx*f(x)
        x+= dx;
    return sum
def f1(x):
    return x**3

def f2(x):
    return x**3*math.sin(x**2)

print(integrate(f1,0,5))
print(integrate(f2,0,2,10000))