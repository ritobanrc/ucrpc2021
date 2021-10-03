#!/bin/python3

from collections import defaultdict
import heapq

lines, banana = map(lambda x: int(x), input().split(' '))

grid = []

for _ in range(lines):
    grid.append(input())

start = (0, 0)
goal = (lines - 1, lines - 1)

def heuristic(node):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

open_set = [(heuristic(start), start)]
came_from = {}
g_score = defaultdict(lambda: float('inf'))
g_score[start] = 0

# f_score = defaultdict(lambda: float('inf'))
# f_score[start] = heuristic(start)

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

while len(open_set) > 0:
    _, current = heapq.heappop(open_set)
    if current == goal:
        break

    neighbors = [
            add(current, (-1, 0)),
            add(current, (1, 0)),
            add(current, (0, -1)),
            add(current, (0, 1)),
    ]

    for neighbor in neighbors:
        if neighbor[0] < 0 or neighbor[0] >= lines or neighbor[1] < 0 or neighbor[1] >= lines:
            continue

        weight = 1 + banana if grid[neighbor[1]][neighbor[0]] == 'b' else 1
        tentative_g_score = g_score[current] + weight

        if tentative_g_score < g_score[neighbor]:
            came_from[neighbor] = (current, weight)
            g_score[neighbor] = tentative_g_score
            f_score = tentative_g_score + heuristic(neighbor)
            heapq.heappush(open_set, (f_score, neighbor))


current = goal
path_len = 0
while current != start:
    current, weight = came_from[current]
    path_len += weight

print(path_len)
