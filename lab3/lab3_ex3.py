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
def word_count(file):
    f = open(file,'r')
    count_line=0
    count_words=0
    count_characters=0
    for line in f:
        count_line+=1
        count_words+=len(line.split())
        count_characters+=len(line)
    f.close()
    print(f"file: {file} {count_line} Lines, {count_words} Words, {count_characters} Characters.")

word_count("oliver_twist.txt")
