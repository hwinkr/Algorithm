import sys
input = sys.stdin.readline

str = input()
cnt = dict()

for c in str[: -1]:
    if c.islower():
        c = c.upper()
    if c in cnt:
        cnt[c] += 1
    else:
        cnt[c] = 1


def get_key(val):
    for key, value in cnt.items():
        if val == value:
            return key


cnt_lst = list(cnt.values())
if cnt_lst.count(max(cnt_lst)) >= 2:
    print('?')
else:
    print(get_key(max(cnt_lst)))
