#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ofertzur
#
# Created:     06/11/2018
# Copyright:   (c) ofertzur 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import re
import string
#print(string.punctuation)
##################################################################
# You must write the right pattern in each exercise
##################################################################

#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ofertzur
#
# Created:     06/11/2018
# Copyright:   (c) ofertzur 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import re


# st = "<> <a> b <c> <de> <> <>  dsafasf sda fsd"
# match = re.search(r'<.+?>', st)
# print(match)
# print(re.findall(r'<.+?>',st))
# print(re.findall(r'(?:(<\w>.+))<\w>',st))
#
# exit(1)

# \w =  A-Za-z0-9_
# \W = ^\w

#EX1
st = "EX1: Please, clean this :   sentence_from all signs, like _,.:; etc but leave @ alone"
desired_output = "EX1 Please clean this sentence from all signs like etc but leave @ alone"

# use the sub function
pattern = r'\s*[_,.:;]+\s*'
replace_st = ' '
match = re.sub(pattern,replace_st,st)
print(match)
assert match == desired_output,'EX1: strings do not match'

#EX2
st = "EX2:    Please   clean  this   sentence    from   all  spaces      but     leave @ alone."
desired_output = "EX2: Please clean this sentence from all spaces but leave @ alone."
# use the sub function
pattern = r'\s+'
replace_st = ' '
match = re.sub(pattern,replace_st,st)
print(match)
assert match == desired_output,'EX2: strings do not match'

#EX3 - one/two spaces remain. More than 2 spaces, replaced to one space
st = "EX3:    Please   clean  this      sentence    from   all  spaces   that    appear  more than       2   but leave @  alone."
desired_output = "EX3: Please clean  this sentence from all  spaces that appear  more than 2 but leave @  alone."
# use the sub function
pattern = r'\s\s\s+'
replace_st = ' '
match = re.sub(pattern,replace_st,st)
print(match)
print(desired_output)
assert match == desired_output,'EX3: strings do not match'

#EX4
st = "EX4:    Please   clean  this      sentence    from   all  signs   like  etc .:;_  but leave @ alone."
desired_output = "EX4 Please clean this sentence from all signs like etc but leave @ alone."
# use the sub function
pattern = r'\s*[_,.:; ]+\s*(?!$)'
replace_st = ' '
match = re.sub(pattern,replace_st,st)
print(match)
print(desired_output)
assert match == desired_output,'EX4: strings do not match'

#EX5
st = "EX5:    Please   clean  this      sentence    from   all  signs   like  etc .:;_  but leave @ alone."
desired_output = "EX5: Please clean this sentence from all signs like etc but leave @ alone."
# use the sub function
match = re.sub(r'(?<!5)\s*[_,.:; ]+\s*(?!$)',' ',st)
print(match)
print(desired_output)
assert match == desired_output,'EX5: strings do not match'

#EX6
st = "EX6: Please, clean this :   sentence_from all signs, like _,.:; etc. but leave @ alone."
desired_output = "EX6 Please clean this sentence from all signs like etc but leave @ alone."

# use the re.split function
pattern = r'\s*[_,.:; ]+\s*(?!$)'
match = ' '.join(re.split(pattern,st))
print(match)
assert match == desired_output,"EX6, strings do no match"

#EX6B
desired_output = "EX6 Please clean this sentence from all signs like etc but leave @ alone"
pattern = r'\s*[_,.:; ]+\s*(?!$)'
strip_pattern = r'.'
match = ' '.join(re.split(pattern,st.strip(strip_pattern)))
#or
#match = (' '.join(re.split(pattern,st))).strip()

print(match)
assert match == desired_output

# EX7
#          To find                                  NOT to find
st = 'pit spot spate respite peat                slap two pt Pot part'
pattern = r'\b[psr]\w+[te](?!$)'
match = re.findall(pattern,st)
if match:
    print(match)
assert match == ['pit', 'spot', 'spate', 'respite', 'peat']


# EX8
st = "rap them\ntrapeth\nrapth\nwrap/try\nsap tray\n87rap9th\nrapothecary\n"
st_not_to_find = 'aleht\nhappy them\ntarpth\nApt\npeth\ntarreth\nddapdg\nshape the\n'
fullst = st + st_not_to_find
pattern = r'.*rap.*|.*sap.*'
match = re.findall(pattern,fullst)
if match:
    print(match)
    print(st.strip().split('\n'))
assert match == st.strip().split('\n')

print("You finished. Good work!!!")
#blblblb
if match:
    print(match)

def main():
    pass

if __name__ == '__main__':
    main()
