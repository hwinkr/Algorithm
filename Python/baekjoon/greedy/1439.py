# 뒤집기

s = input()

zero_s = s.split("0")
one_s = s.split("1")

zero = 0
one = 0

for x in zero_s:
    if(x != ''):
        zero += 1
for x in one_s:
    if(x != ''):
        one += 1

if(zero > one):
    print(one)
else:
    print(zero)
