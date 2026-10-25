import numpy as np

array = [1, 2, 3, 4, 5]


# print(array_length)

#array.insert(1, 3)
array.append(6)

array_length = len(array)

for num in array:
    print(num, end=" ")
    if num < array_length:
        print("->", end=" ")


maximum = array[0]
for i in range(1, len(array)):
    if array[i] > maximum:
        maximum = array[i]
print(maximum)