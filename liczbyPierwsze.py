import json
import time
# import aiohttp
from math import sqrt

with open("values.json", encoding="UTF-8")as file:
    encode = json.load(file)

enc1 = [[2, 10],
        [3, 13],
        [9, 50]
        ]
output = []


def save_data_to_file(outputList, fileName):
    with open(fileName, "w", encoding="UTF-8") as file:
        for item in outputList:
            file.write(str(item[0]) + "\n")


def first_number_check(checkNumber):
    if checkNumber < 2:
        return False

    if checkNumber == 2:
        return True

    for nm in range(2, int(sqrt(checkNumber)) + 1):
        if checkNumber % nm == 0:
            return False
    return True


def first_number_counter(startNumber, endNumber):
    counter = 0
    start = time.perf_counter()
    for number in range(startNumber, endNumber + 1):
        if first_number_check(number):
            counter += 1
    end = time.perf_counter()
    difference = end - start
    return counter, difference


def function_performance_check(function):
    start = time.perf_counter()
    function()
    end = time.perf_counter()
    difference = end - start
    return difference


for line in enc1:
    output.append(first_number_counter(line[0], line[1]))

print(output)
save_data_to_file(output, "output.txt")
# print(first_number_counter(7250931, 9227290))
