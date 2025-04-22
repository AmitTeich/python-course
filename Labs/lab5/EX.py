#-------------------------------------------------------------------------------
# Name:        lab5
#-------------------------------------------------------------------------------
# You are given a file "data.log". This is a text file where every line
# contains a time stamp and a temperature reading from a sensor.
#
#   00:00:32  27.12
#   00:01:07  33.51
#
# You have to read the file and return the following information:
# 1. Min temperature over the day
# 2. Times where the min temperature was read
# 3. Max temperature over the day
# 4. Times where the max temperature was read
# 5. Average temperature over the day


# you should get:
# min temp:  9.95
# min times:  ['00:02:29']
# max temp:  46.5
# max times:  ['03:39:20', '07:06:30', '11:20:18', '15:21:09']
# avg: 32.02

# f = open('data.log')
# min_temp = float('inf')
# min_list = list()
# max_temp = float('-inf')
# max_list = list()
# for line in f:
#     l = line.split()
#     if l[1] >= max_temp :
#         max_list.append(l[::-1])
#         max_temp = l[1]
#     if l[1] < min_temp:
#         min_list.append(l[::-1])
#         min_temp = l[1]
# f.close()


def main():
    f = open('data.log')
    min_temp = float('inf')
    min_list = list()
    max_temp = float('-inf')
    max_list = list()
    avg_temp = 0
    counter_number_of_temp = 0
    for line in f:
        l = line.split()
        temp = float(l[1])
        avg_temp+=temp
        counter_number_of_temp+=1
        if temp > max_temp:
            max_list = [l[0]]
            max_temp = temp
        elif temp == max_temp:
            max_list.append(l[0])
        if temp < min_temp:
            min_list = [l[0]]
            min_temp = temp
        elif temp == min_temp:
            min_list.append(l[0])
    avg_temp/=counter_number_of_temp
    f.close()

    print("min temp: ",min_temp)
    print("min times: ",min_list)
    print("max temp: ",max_temp)
    print("max times: ",max_list)
    print(f"avg: {avg_temp:.2f}")


if __name__ == '__main__':
    main()