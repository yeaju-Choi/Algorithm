'''
첫째 줄에는 어떤 지역을 나타내는 2차원 배열의 행과 열의 개수를 나타내는 수 N이 입력된다.
 N은 2 이상 100 이하의 정수이다.
 
둘째 줄부터 N개의 각 줄에는 2차원 배열의 첫 번째 행부터 N번째 행까지 순서대로 한 행씩 높이 정보가 입력된다. 
각 줄에는 각 행의 첫 번째 열부터 N번째 열까지 N개의 높이 정보를 나타내는 자연수가 빈 칸을 사이에 두고 입력된다. 
높이는 1이상 100 이하의 정수이다.


첫째 줄에 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 출력한다
'''

# 비의 양을 range로 두어 비교해야함 -> 0~ data최대값

import sys 
from collections import deque
input = sys.stdin.readline 

def bfs(x,y,limit,visited): 
    queue = deque() 
    queue.append((x,y)) 
    visited[x][y] = 1  # 방문 표시 

    while queue: 

        a,b = queue.popleft() 
        # graph[a][b] = -9999
        # print("=> visited : ",end = " ")
        # print(visited)
        
        for i in range(4): 

            cx = a + dx[i]
            cy = b + dy[i] 
            
            if cx >= 0 and cx < n and cy >= 0 and cy < n and (graph[cx][cy]) > limit :
                if visited[cx][cy] == 0:
                    # print("=> now cx,cy : ",end = " ")
                    # print(cx,",", cy)
                    queue.append((cx,cy))
                    visited[cx][cy] = 1

n = int(input())
graph = list() 

dx = [-1,1,0,0]
dy = [0,0,1,-1]

for _ in range(n):
    graph.append(list(map(int,input().split()))) 

answer = 0 
max_height = 0

for items in graph:
    for height in items:
        max_height = max(max_height,height)

# print(max_height)

for limit in range(max_height):
    
    count = 0
    # visited = list() # 방문 여부를 체크하기 위한 리스트
    visited = [[0] * n for _ in range(n)] 

    for i in range(n): 
        for j in range(n):
            if graph[i][j] > limit and visited[i][j] == 0:
                bfs(i,j,limit,visited)
                count += 1

    answer = max(answer,count)

print(answer)
            
