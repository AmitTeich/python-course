def Max3(file):
    f= open(file)
    #read file, split the file to list of numbers (string), casting to int
    numbers = [float(number) for number in f.read().split()]
    f.close()
    max3 = [float('-inf')]*3

    for number in numbers:
        if (number>max3[0]) :
            max3[2] = max3[1]
            max3[1] = max3[0]
            max3[0] = number
        elif (number>max3[1]):
            max3[2] = max3[1]
            max3[1] = number
        elif (number>max3[2]):
            max3[2] = number
    return max3


def main():
    print(Max3('data1.txt'))
    print(Max3('data2.txt'))
if __name__ == '__main__':
    main()







