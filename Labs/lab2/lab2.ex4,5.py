#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Amit
#
# Created:     04/04/2025
# Copyright:   (c) Amit 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def main():
    pass

if __name__ == '__main__':
    main()
List1 = [x**2 for x in range(5,12)]
List2 = [x+y for x in [10,20,30,40] for y in [1,2,3,4]]
print(List1)
print(List2)
sentence = "The students have to use list comprehension to make the code shorter"
words = sentence.split()
word_lengths = [len(word) for word in words if word != 'list']
##word_lengths = []
##for word in words:
##    if word != "list":
##        word_lengths.append(len(word))
print(word_lengths)