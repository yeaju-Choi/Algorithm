import sys
from collections import deque
sys.setrecursionlimit(10000)
input = sys.stdin.readline

# 상하좌우대각선 
dx = [0,0,-1,-1,-1,1,1,1]
dy = [1,-1,0,-1,1,0,-1,1] 

def dfs(graph,x,y,w,h): 

    if x < 0 or x >= h or y >= w or y < 0:
        # print("false")
        return False 
    # print("=",x,":",y)
    if graph[x][y] == 1:
        graph[x][y] = 0
        for i in range(len(dx)):
            
            dfs(graph,x+dx[i],y+dy[i],w,h) 
            
        return True
    # print("-----")
    # for i in graph:
    #     print(i)
    
    return False 

while True:

    w,h = map(int,input().split()) 
   
    if w == 0 and h == 0:  # 입력 종료 조건 
        break  

    graph = list() 
    for i in range(h):
        graph.append(list(map(int,input().split())))

    # print(graph)
    result = 0
    for i in range(h):
        for j in range(w):
            
            if graph[i][j] == 1:
                dfs(graph,i,j,w,h)
                result += 1
            # if dfs(graph,i,j,w,h) == True:
            #     result += 1

    print(result)
