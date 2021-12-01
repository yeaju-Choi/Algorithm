from collections import deque


def bfs():


    while queue:

        
        a,b = queue.popleft()

        for i in range(len(dx)):
            nx = a + dx[i]
            ny = b + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[a][b] + 1 
                queue.append((nx,ny))

            if graph[nx][ny] == -1: #도착지점 
                graph[nx][ny] = graph[a][b] + 1 
                return graph[nx][ny]

    

             
t = int(input())
answer = [] 

for i in range(t):

    n = int(input()) # 배열 크기  n*n 

    graph = list() # 리스트 초기화 

    for i in range(n):
        graph.append(list(0 for _ in range(n)))

    x,y = map(int,input().split()) # 시작 위치 
    dest_x, dest_y = map(int,input().split()) # 도착 위치

    graph[dest_x][dest_y] = -1

    if x == dest_x and y == dest_y:
        answer.append(0)
        continue
    
    dx = [-2,-1,1,2,-2,-1,1,2]
    dy = [1,2,2,1,-1,-2,-2,-1]


    # +1 한값 가지고 오기 
    queue = deque() 
    queue.append((x,y))

    answer.append(bfs())

    # result = 0
    # for i in graph:

    #     result = max(result,max(i))
    # answer.append(result)

for i in answer:
    print(i)