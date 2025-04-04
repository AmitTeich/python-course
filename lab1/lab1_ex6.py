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
A = (list)(range(0,13))
print(A)
B = A[::2]
print(B)
C =  B + A[1::2]
print(C)
C1 = [B] + [A[1::2]]
print(C1)