# 1
# N = int(input())

# direction = input().split()

# x = 1
# y = 1

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
# # 공간을 벗어나는 이동은 무시
# for dir in direction:
#     x_index = 0
#     y_index = 0
#     if(dir == "U"):
#         x_index = dx[0]
#         y_index = dy[0]
#     elif(dir == "R"):
#         x_index = dx[1]
#         y_index = dy[1]
#     elif(dir == "D"):
#         x_index = dx[2]
#         y_index = dy[2]
#     else:
#         x_index = dx[3]
#         y_index = dy[3]

#     if(x + x_index > 0 and x + x_index < N and y + y_index > 0 and y + y_index < N):
#         x += x_index
#         y += y_index

# print(x, y)

# 2
N = int(input())

move = input().split()

x, y = 1, 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

move_type = ['U', 'R', 'D', 'L']

for dir in move:
    for i in range(move_type):
        if(dir == move_type[i]):
            new_x = x + dx[i]
            new_y = y + dy[i]

    if(new_x < 1 or new_x > N or new_y < 1 or new_y > N):
        continue

    x = new_x
    y = new_y

print(x, y)
