# 30의 배수중 가장 큰 수 만들기
# 조건을 만족 하는 경우 내림차순 으로 정렬하는것이 제일 큼
import sys
input = sys.stdin.readline
N = input()

if(N.count("0") == 0 or int(N) % 3 != 0):
    print("-1")
else:
    new_N = sorted(N, reverse=True)
    print(''.join(new_N))

# 문자열도 정렬 가능 sorted 함수 : sort 된 배열을 반환해준다
arr = [1, 2, 3, 4, 5]
new_arr = sorted(arr, reverse=True)
print(new_arr)

str = "85123"
new_str = sorted(str, reverse=True)
print(''.join(new_str))
