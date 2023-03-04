import heapq


import heapq

# heap은 데이터를 꺼내는 경우에 우선순위가 높은 데이터를 우선적으로 꺼낸다

# min heap : 우선순위가 낮은 원소부터 먼저 꺼낸다


def heapSort(nums):
    h = []
    result = []

    for num in nums:
        heapq.heappush(h, -num)

    for _ in range(len(h)):
        # 우선순위가 가장 낮은 원소부터 꺼내서 result 배열에 append 한다
        result.append(-heapq.heappop(h))

    return result


ans = heapSort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(ans)
