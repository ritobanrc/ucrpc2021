#!/bin/python3

pieces, lines = map(lambda x: int(x), input().split(' '))

team1 = pieces
team2 = pieces

i = 0

for i in range(lines):
    a, b, c, d = map(lambda x: int(x), input().split(' '))
    team2 -= a * b
    team1 -= c * d

    if team1 <= 0 or team2 <= 0:
        break

if team2 <= 0 and team1 > 0:
    print(f'Team 1 wins at round {i + 1}!')
elif team1 <= 0 and team2 > 0:
    print(f'Team 2 wins at round {i + 1}!')
elif team1 <= 0 and team2 <= 0:
    print(f'It\'s a tie at round {i + 1}!')
else:
    print('Oh no!')
