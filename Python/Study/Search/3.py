# 왕실의 나이트
# 나이트가 이동할수 있는 모든 좌표를 출력
# 행 1~8 , 열 a~h

point = input()

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

x = int(point[1])
y = alphabet.index(point[0]) + 1

answer = 0

for i in range(len(dx)):
    nx = x + dx[i]
    ny = y + dy[i]
    if(nx < 1 or nx > 8 or ny < 1 or ny > 8):
        continue
    answer += 1

print(answer)

# function ord : 문자 -> 아스키코드

input_location = input()

location_row = int(input_location[1])
location_col = int(ord(input_location[0])) - int(ord('a')) + 1

possCnt = 0

moves = [(-1, -2), (-2, -1), (-2, 1), (-1, 2),
         (1, 2), (2, 1), (2, -1), (1, -2)]

for move in moves:
    next_row = location_row + move[0]
    next_col = location_col + move[1]

    if(next_row < 1 or next_row > 8 or next_col < 1 or next_col > 8):
        continue

    possCnt += 1

print(possCnt)
