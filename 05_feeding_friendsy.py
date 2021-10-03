#!/bin/python3

import bisect
import io,os

input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

time, upper, lower = map(lambda x: int(x), input().split(b' '))

upper_starts = []
upper_stops = []
lower_starts = []
lower_stops = []

for _ in range(upper):
    start, stop, rainbow = map(lambda x: int(x), input().split(b' '))
    upper_starts.append(start)
    upper_stops.append((stop, rainbow == 1))

for _ in range(lower):
    start, stop, rainbow = map(lambda x: int(x), input().split(b' '))
    lower_starts.append(start)
    lower_stops.append((stop, rainbow == 1))

def get_points(t, starts, stops):
    idx1 = bisect.bisect_left(starts, t)
    idx2 = idx1 - 1

    if idx1 < len(starts) and t >= starts[idx1] and t <= stops[idx1][0]:
        return 3 if stops[idx1][1] else 1
    elif idx2 < len(starts) and t >= starts[idx2] and t <= stops[idx2][0]:
        return 3 if stops[idx2][1] else 1
    else:
        return 0


total_points = 0
for t in range(time):
    p1 = get_points(t, upper_starts, upper_stops)
    p2 = get_points(t, lower_starts, lower_stops)

    total_points += max(p1, p2)

print(total_points)
