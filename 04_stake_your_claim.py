#!/bin/python3


rows, cols = map(lambda x: int(x), input().split(' '))

grid = []

for _ in range(2 * rows + 1):
    grid.append(input())


def check(cell):
    return grid[cell[1]][cell[0]] == '.'

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def get_region(start):
    stack = []
    stack.append(start)

    region = set()

    while len(stack) > 0:
        current = stack.pop()

        if current in region:
            continue

        region.add(current)

        left = add(current, (-1, 0))
        if (left[0] > 1 and check(left)):
            stack.append(add(left, (-1, 0)))

        right = add(current, (1, 0))
        if (right[0] < 2*cols - 1 and check(right)):
            stack.append(add(right, (1, 0)))

        up = add(current, (0, -1))
        if (up[1] > 1 and check(up)):
            stack.append(add(up, (0, -1)))

        down = add(current, (0, 1))
        if (down[1] < 2*rows - 1 and check(down)):
            stack.append(add(down, (0, 1)))

    return region

regions = []

for i in range(cols):
    for j in range(rows):
        current = (2 * i + 1, 2 * j + 1)

        already_found = False

        for region in regions:
            if current in region:
                already_found = True
                break

        if not already_found:
            regions.append(get_region(current))

result = list(map(lambda r: len(r), regions))
result.sort(reverse=True)
for x in result:
    print(x, end=' ')
print()
