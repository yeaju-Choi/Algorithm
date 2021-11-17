# -*- coding: utf-8 -*- 

from collections import deque 


def bfs(a,b):
    
    queue = deque() 
    queue.append((a,b)) 

    while queue:
        x,y = queue.popleft() 
        # 현위치서 4가지 방향 확인  

        for i in range(4): 
            nx = x + dx[i]  
            ny = y + dy[i]

            # 예외처리 

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 0: #  벽인 경우 무시 
                continue
        
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))


            print(nx,ny)
            print(graph)
    return graph[n-1][m-1] #가장 오른쪽 아래까지 최단 거리 반환 


n,m = map(int,input().split())
# n = int(input())
# m = int(input())

graph = [] 

for i in range(n):
    graph.append(list(map(int,input())))

print(graph)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

print(bfs(0,0))



