#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ofertzur
#
# Created:     02/12/2021
# Copyright:   (c) ofertzur 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def ordered_func(first,second=""):
    print(f"first = {first}")
    print(f"second = {second}")

def tuple_func_test(*args):
    print("in tuple_func_test")
    print(f"args: {args}")

def tuple_func(*args):
    print("in tuple_func")
    print("args: ",args)
    print(f"first = {args[0]}")
    print(f"second = {args[1]}")

def tuple_func2(x1="",x2="",x3=""):
    print("in tuple_func2")
    print(f"x1={x1}, x2={x2}, x3={x3}")


def dict_func(**args):
    print("in dict_func")
    print("args: ",args)
    print(f"first = {args['first']}")
    print(f"second = {args['second']}")

def dict_func2(first="",second=""):
    print("in dict_func2")
    print(f"first = {first}")
    print(f"second = {second}")
def main():
    x = int(input())
    if(x ==1):
        ordered_func('first_arg','second_arg')
        ordered_func(second='second_arg',first='first_arg')
        ordered_func("first_arg",second='second_arg')
    elif x == 2:
        l = ['first_arg','second_arg']
        tuple_func_test(1,2,3,4,5)
        tuple_func_test(1, 2, 3)
        tuple_func_test(l)
    elif x == 3:
        l = ['first_arg','second_arg','third_arg','forth']
        tuple_func(*l)
        tuple_func2(1,2,3)
        tuple_func2(l)
        tuple_func2(*l)
    elif x == 4:
        d = {'second':'second_arg','first':'first_arg'}
        dict_func(**d)
        dict_func2(**d)
##    func()
##    func(second='myname')
    # func(**d)
    #
if __name__ == '__main__':
    main()
