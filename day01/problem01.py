#!/bin/python3
file1 = open('input01.txt', 'r')
max = 0
current = 0
for line in file1.readlines():
    if not line.strip():
        if current > max:
            max = current
        current = 0
    else:
        current += int(line.strip())
    
if current > max:
    max = current
print(max)