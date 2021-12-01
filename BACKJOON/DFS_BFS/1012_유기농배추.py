# from collections import deque

# def bfs(x,y,count):
    
#     queue = deque() 

#     queue.append((x,y))

#     while queue:

#         a,b = queue.popleft()

        
#         # 네방향으로 가면서 탐색 
#         for i in range(4):
#             nx = a + dx[i]            
#             ny = b + dy[i]

#             if nx < 0 or nx >= m or ny < 0 or ny >= n:
#                 continue
            
#             if graph[nx][ny] == 0:
#                 continue

#             if graph[nx][ny] == 1:
#                 count.append(True)
#                 graph[nx][ny] = 0
#                 queue.append((nx,ny))

#     print(count)
    




def dfs(graph,x,y,n,m):
    
    if x < 0 or x >= n or y < 0 or y >= m:
        return False 
    
    if graph[x][y] == 1:
        graph[x][y] = 0

        dfs(graph,x-1,y,n,m)
        dfs(graph,x+1,y,n,m)
        dfs(graph,x,y-1,n,m)
        dfs(graph,x,y+1,n,m)


        return True
    return False


def organic():

    n,m,k = map(int,input().split())

    graph = list()

    for i in range(n):
        graph.append(list(0 for i in range(m)))

    for i in range(k):
        a,b = map(int,input().split())
        graph[a][b] = 1


    answer = 0

    for i in range(n):
        for j in range(m):
            
            result = dfs(graph,i,j,n,m)
            if result:
                answer += 1

    return answer



t = int(input()) #테스트 케이스 개수 
answer = []

for i in range(t):
    answer.append(organic())

for i in answer:
    print(i)









