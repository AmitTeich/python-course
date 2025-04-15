import string
import pickle


def word_frequency(file) :
    wordAppears = {}
    f=open(file)
    for line in f:
        l=''
        for char in line:
                if char in string.punctuation:
                    l+=' '
                else: l+=char.lower()
        cleanedWords=l.split()
        for word in cleanedWords:
            if word not in wordAppears:
                wordAppears[word] = 1
            else:
                wordAppears[word] += 1
    f.close()
    return wordAppears

wordFrequency = word_frequency('oliver_twist.txt')
#print(wordFrequency['and'])
#print(wordFrequency['to'])
sorted_items = dict(sorted(wordFrequency.items(), key = lambda item: item[1],reverse=True))
print(sorted_items)




