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
l1 = (1,'hello',[2,4,6],['a','b','c','d'])
print(l1)
l1[2][1] = 10;
print(l1)
l2 = [(0,1,2,3)]
l1 = l1[:-1] + (tuple)(l2)
print(l1)