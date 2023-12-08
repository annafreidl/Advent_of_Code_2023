from typing import List

input1 = open('Tag 1/input.txt', 'r')
lines = input1.readlines()

gesamtsumme = 0
for line in lines:
    array = []
    for char in line:
        if char.isdigit():
            array.append(char)
    summe = array[0] + array[len(array) - 1]
    gesamtsumme += int(summe)
print("Tag 1:" + str(gesamtsumme))
