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
import os
def main():
    pass

if __name__ == '__main__':
    main()
def word_count(file):
    f = open(file,'r')
    countLine=0
    countWords=0
    countCharacters=0
    for line in f:
        countLine+=1
        countWords+=len(line.split())
        countCharacters+=len(line)
    f.close()
    print(f"file: {file} {countLine} Lines, {countWords} Words, {countCharacters} Characters.")

word_count("oliver_twist.txt")
