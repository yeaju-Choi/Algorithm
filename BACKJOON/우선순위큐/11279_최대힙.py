import heapq
from sys import stdin
max_heap = []
n = int(stdin.readline())

for i in range(n):
    data = int(stdin.readline())
    
    if data == 0:
        if max_heap:
            print(heapq.heappop(max_heap)[1])
        else:
            print(0)
    
    else:
        heapq.heappush(max_heap,(-data,data))
