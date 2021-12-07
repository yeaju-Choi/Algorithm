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
    
##########################
import heapq
from sys import stdin

n = int(stdin.readline())

leftheap = [] # 최대힙 
rightheap = []
answer = []

for i in range(n):
    data = int(stdin.readline())

    if len(leftheap) == len(rightheap):
        heapq.heappush(leftheap,(-data,data)) 
    else:
        heapq.heappush(rightheap,(data,data)) 

    if rightheap and leftheap[0][1] > rightheap[0][0]:   # left에 더 큰 값이 들어감 
        min = heapq.heappop(rightheap)[0] 
        max = heapq.heappop(leftheap)[1] 
        heapq.heappush(leftheap,(-min,min))
        heapq.heappush(rightheap,(max,max)) 

    answer.append(leftheap[0][1]) 

for i in answer:
    print(i)





