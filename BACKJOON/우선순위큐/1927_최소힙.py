from sys import stdin
import heapq

min_heap = []
n = int(stdin.readline())

for i in range(n):
    data = int(stdin.readline())
    if data == 0:
        print(heapq.heappop(min_heap) if min_heap else 0)
    else:
        heapq.heappush(min_heap,data)

