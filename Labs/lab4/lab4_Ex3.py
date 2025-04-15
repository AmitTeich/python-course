from lab4.lab4_Ex1 import sorted_items
countUp1000=0
for key in sorted_items:
    if sorted_items[key] <= 1000 : break
    countUp1000+=1
print(countUp1000)