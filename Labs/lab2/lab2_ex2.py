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

def main():
    pass

if __name__ == '__main__':
    main()
def func2_1(l):
    i=0;
    l_even=list()
    l_odd = list()
    while(i<len(l)):
        if(l[i]%2):
            l_odd.append(l[i])
        else: l_even.append(l[i])
        i+=1;
    l1 = [l_even,l_odd]
    return l1

l=[0,3,23,435,1,7,65,3,2,8]
print(func2_1(l))

def func2_2(*l):
    i=0;
    l_even=list()
    l_odd = list()
    for num in l:
        if(num%2):
            l_odd.append(num)
        else: l_even.append(num)
    l1 = [l_even,l_odd]
    return l1
print(func2_2(1,2,5,4,3,7,10,23))

def func2_3(l):
    i=0;
    l_even_index=list()
    l_odd_index = list()
    while(i<len(l)):
        if(i%2):
            l_odd_index.append(l[i])
        else: l_even_index.append(l[i])
        i+=1;
    l1 = [l_even_index,l_odd_index]
    return l1
print(func2_3(l))

