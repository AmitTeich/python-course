def Contains(sublist, lst):
    index = 0
    for num in sublist:
        found = False
        for i in range(index, len(lst)):
           if num == lst[i]:
               index = i+1
               found = True
               break
        if not found:
            return  False
    return True

def main():
    print(f"[1,2],[0,1,5,4,3,1,2,3]:")
    print(Contains([1,2],[0,1,5,4,3,1,2,3]))
    print(f"[2,1],[0,1,5,4,3,1,2,3]:")
    print(Contains([2,1],[0,1,5,4,3,1,2,3]))
    print(f"[1,1],[0,1,5,4,3,1,2,3]:")
    print(Contains([1,1],[0,1,5,4,3,1,2,3]))
    print(f"[4,4],[0,1,5,4,3,1,2,3]:")
    print(Contains([4,4],[0,1,5,4,3,1,2,3]))
    print(f"[],[0,1,5,4,3,1,2,3]:")
    print(Contains([],[0,1,5,4,3,1,2,3]))

if __name__ == '__main__':
    main()