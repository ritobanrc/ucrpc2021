lines = int(input())

arr = list(range(1, 6))

for _ in range(lines):
    a, b = map(lambda x: int(x), input().split(' '))
    arr[a - 1], arr[b - 1] = arr[b - 1], arr[a - 1]

print(arr.index(3) + 1)
