import heapq 
from sys import stdin 
import copy

mid_heap = [] 
n = int(stdin.readline())

def return_mid(heap):
    temp_mid = copy.copy(heap)
   
    if len(temp_mid) == 1 or len(temp_mid) == 2:
        return heap[0]
        
    if len(temp_mid) % 2 == 0:
        length = int(len(temp_mid)/2)
    else :
        length = int(len(temp_mid)/2)+1

    
    mid = 0

    for i in range(length):
        mid = heapq.heappop(temp_mid)        
    return mid 


for i in range(n):

    data = int(stdin.readline())
    heapq.heappush(mid_heap,data)
    print(return_mid(mid_heap))
    
    
