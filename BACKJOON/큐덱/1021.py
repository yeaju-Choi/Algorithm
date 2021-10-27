# 회전하는 큐 

'''
큐에 처음에 포함되어 있던 수 N이 주어진다. 
그리고 지민이가 뽑아내려고 하는 원소의 위치가 주어진다.
 (이 위치는 가장 처음 큐에서의 위치이다.) 
 이때, 그 원소를 주어진 순서대로 뽑아내는데 드는 
'''

# position 에서 0번째 요소와 q에서 leftpop한게 같은게 비교 
# 
from collections import deque

q = deque()

n,m = map(int,input().split())
position = list(map(int,input().split()))

for i in range(1,n+1):
    q.append(i)

answer = 0

while position:
    
    if q[0] == position[0]: # 맨앞에 있음 popleft
        q.popleft()
        del position[0]


    else:  # 회전해야함 1) 반으로 나눴을때 왼쪽 2) 오른쪽
        
        find_index = q.index(position[0])

        if find_index > len(q) / 2 : # 뒤쪽에 있을때  
            while q[0] != position[0]: # 같지 않을동안 계속 찾음
                q.rotate(1)
                answer += 1

        else:
            while q[0] != position[0]:
                q.rotate(-1)
                answer += 1




print(answer)
