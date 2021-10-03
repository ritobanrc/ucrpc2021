#!/bin/python3

(lines, _) = input().split(' ')

s = 0
for _ in range(int(lines)):
    s += len(list(filter(lambda c: c == 't', input())))

print(s)
