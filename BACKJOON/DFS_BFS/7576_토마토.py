# 토마토 
from collections import deque

def bfs():

    
    while queue:
        

        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 1 or graph[nx][ny] == -1: # 이미 익거나 썩어있음 
                continue

            if graph[nx][ny] == 0:
                # 그 다음거 돌떄는 count 
                # graph[nx][ny] = 1 # 방문 처리 
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
            



m,n= map(int,input().split()) 
queue = deque()
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))




# 큐에 토마토 좌표 넣기 

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i,j))





dx = [-1,1,0,0]
dy = [0,0,-1,1]

bfs() 

answer = 0
# 그래프에서 제일 큰 숫자 찻기 , 만약에 0이 있음 -1 리턴 

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(-1)
            exit(0)
        
    answer = max(answer,max(graph[i]))     
        
        # answer = max(answer,graph[i][j]) 

print(answer-1)










