#-------------------------------------------------------------------------------
# Name:        Lab3
# Purpose:     Dictionary, Sets
#
# Author:      ofertzur
#
# Created:     26/10/2018
# Copyright:   (c) ofertzur 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

names = ['Alice', 'Bob', 'Cathy', 'Dan', 'Ed', 'Frank', 'Gary', 'Helen', 'Irene', 'Jack', 'Kelly', 'Larry']
ages  = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19]


# ex1 - write the following function to combine the two lists into a dictionary
def combine_lists(keys, values):
  # option I
    d = {}      # option II
    for i in range(len(keys)):
     d[keys[i]] = values[i]
    return d





d = combine_lists(names, ages)

print(d)


# ex2 - write a function that uses the dictionary to return a list of people
# that are in a certain age

def people(d, age):
    # d.keys()
    # d.values()
    # d.items()
    # for i in d:
    #    print i,

    # write the code here
    names = list()
    for key in d:
        if d[key] == age :
            names.append(key)

    # returning the result
    return names

def testbench1():
    d = combine_lists(names, ages)

    print( 'people 18 = ',people(d, 18))
    print( 'Dan in people(18) and Cathy in people(18)')
    print( 'Dan' in people(d,18) and 'Cathy' in people(d,18))
    print( 'people 19 = ',people(d,19))
    print( 'Ed in people(19) and Helen in people(19) and Irene in people(19) and Jack in people(19) and Larry in people(19)')
    print( 'Ed' in people(d,19) and 'Helen' in people(d,19) and 'Irene' in people(d,19) and 'Jack' in people(d,19) and 'Larry' in people(d,19))
    print( 'people 20 = ',people(d,20))
    print( 'Alice in people(20) and Frank in people(20) and Gary in people(20)')
    print( 'Alice' in people(d,20) and 'Frank' in people(d,20) and 'Gary' in people(d,20))
    print( 'people 21 = ',people(d,21))
    print( people(d,21) == ['Bob', 'Dan', 'Kelly'])
    print( 'people 22 = ', people(d,22))
    print( people(d,22) == ['Kelly'])
    print( people(d,23) == [])



def main():
    pass

if __name__ == '__main__':
    main()
    testbench1()
