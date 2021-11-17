from collections import deque


def bfs(x,y):
    queue = deque()

    queue.append((x,y))  #시작 지점 

    while queue:
        a,b = queue.popleft() # 요소를 하나 꺼냄 

        # 꺼낸 요소로부터 네방향 탐색 
        for i in range(4):
            search_x = a + dx[i]
            search_y = b + dy[i]

            if search_x < 0 or search_x >= n or search_y < 0 or search_y >= m: # 미로를 벗어나면 
                continue

            if graph[search_x][search_y] == 0 : # 벽임 => 안가야함 
                continue

            if graph[search_x][search_y] == 1:
                queue.append((search_x,search_y))
                graph[search_x][search_y] = graph[a][b] + 1

    

    return graph[n-1][m-1]









n,m = map(int,input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input())))


dx = [-1,1,0,0]
dy = [0,0,-1,1]

print(bfs(0,0))

