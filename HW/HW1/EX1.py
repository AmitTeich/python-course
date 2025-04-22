


def Max3(file):
    f= open(file)
    #read file, split the file to list of numbers (string), casting to int
    numbers = [float(number) for number in f.read().split()]
    f.close()
    maxNumbers = [float('-inf')]*3

    for number in numbers:
        if (number>maxNumbers[0]) :
            maxNumbers[2] = maxNumbers[1]
            maxNumbers[1] = maxNumbers[0]
            maxNumbers[0] = number
        elif (number>maxNumbers[1]):
            maxNumbers[2] = maxNumbers[1]
            maxNumbers[1] = number
        elif (number>maxNumbers[2]):
            maxNumbers[2] = number

    # for i in range(3):
    #     for number in numbers:
    #         if (maxNumbers[i]<number and number not in maxNumbers):
    #             maxNumbers[i]=number
    return maxNumbers


def main():
    print(Max3('data1.txt'))
    print(Max3('data2.txt'))
if __name__ == '__main__':
    main()







