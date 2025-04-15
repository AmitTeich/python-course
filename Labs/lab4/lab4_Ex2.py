import string
import pickle
from lab4.lab4_Ex1 import sorted_items
#A:
highFreq=0;
theWord=''
for key in sorted_items:
    if (len(key) == 4) :
        highFreq=sorted_items[key]
        theWord=key
        break
print(f'the word: {theWord} apper {highFreq} time.')
#B:
mostFreqWords = ['1','2','3','4','5','6','7','8','9','10']
for key in sorted_items.keys():
    match len(key):
        case 1:
            if len(mostFreqWords[0]) != 1 : continue
            mostFreqWords[0]+=f' {key}'
        case 2:
            if len(mostFreqWords[1]) != 1: continue
            mostFreqWords[1] += f' {key}'
        case 3:
            if len(mostFreqWords[2]) != 1: continue
            mostFreqWords[2] += f' {key}'
        case 4:
            if len(mostFreqWords[3]) != 1: continue
            mostFreqWords[3] += f' {key}'
        case 5:
            if len(mostFreqWords[4]) != 1: continue
            mostFreqWords[4] += f' {key}'
        case 6:
            if len(mostFreqWords[5]) != 1: continue
            mostFreqWords[5] += f' {key}'
        case 7:
            if len(mostFreqWords[6]) != 1: continue
            mostFreqWords[6] += f' {key}'
        case 8:
            if len(mostFreqWords[7]) != 1: continue
            mostFreqWords[7] += f' {key}'
        case 9:
            if len(mostFreqWords[8]) != 1: continue
            mostFreqWords[8] += f' {key}'
        case 10:
            if len(mostFreqWords[9]) != 2: continue
            mostFreqWords[9] += f' {key}'
        case _: continue

print(mostFreqWords)

#C:
mostFreqWords_3=list()
for i in range(1,11):
    words = list()
    for key in sorted_items:
        if len(key) == i  :
            words.append(key)
        if len(words) >= 3 :
            mostFreqWords_3.append(words)
            break
print(mostFreqWords_3)

