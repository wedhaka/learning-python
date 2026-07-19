import re

handle = open('regex_sum_2445173.txt')

numbersList = []
for line in handle:
    numbers = re.findall(r'\d+', line)
    if numbers:
        numbersList.extend(numbers)

sumNumber = 0
for numbers in numbersList:
    sumNumber = sumNumber + int(numbers)
    
print(sumNumber)
