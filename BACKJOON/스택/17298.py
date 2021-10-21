# 오큰수 

'''
수열의 각 원소 Ai에 대해서 오큰수 NGE(i)를 구하려고 한다.
Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다.
그러한 수가 없는 경우에 오큰수는 -1이다.


총 N개의 수 NGE(1), NGE(2), ..., NGE(N)을 공백으로 구분해 출력한다.
'''

# n = int(input())

# arr = []

# arr = list(map(int,input().split()))

# 시간초과 

# for i in range(len(arr)):
#     if max(arr) == arr[i]: # 최대값이 올때는 -1 출력 
#         print(-1)
#     if arr[i] == arr[-1]: # 마지막 값일때도 -1 
#         print(-1)
#     else:
#         big = arr[i]
#         for j in range(i+1,len(arr)):
#             if big < arr[j]: # 더 큰게 나오면 프린트 찍어주기 
#                 big = arr[j]
#                 print(big)
#                 break

# 스택 이용해서 풀기 
'''
1. 입력의 속도를 줄이기 위해 import sys / input = sys.stdin.readline을 사용했다.

2. 스택은 값이 아닌 '인덱스'를 저장해야 한다는 것을 오랜 삽질 후에 깨달았다.

3. 기본적으로 오큰수가 없으면 -1을 출력해야 하므로 정답 배열 answer을 -1로 초기화해준다.

4. 입력받은 수들 배열 arr을 탐색

  4-1. stack이 비어있지 않고, arr[스택 맨위]가 arr[i]보다 작으면 반복

    4-1-1. answer의 stack.pop()한 인덱스 자리에 arr[i]를 넣는다.

  4-2. stack에 i를 넣는다.

5. 배열 print 

'''

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
stack = []
answer = [-1 for i in range(n)]

for i in range(len(arr)):
    while stack and arr[stack[-1]] < arr[i]:
        answer[stack.pop()] = arr[i]
    stack.append(i)
    
print(*answer)
            
    
            

            


