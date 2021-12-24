import sys 
from collections import deque


input = sys.stdin.readline 


def bfs(v): 
    queue = deque() 
    queue.append(v) 

    while queue: 
        node = queue.popleft() 
        for i in graph[node]: 
            if visited[i] == False : # 아직 방문 안한것만 방문
            #     visited[i] = True # 방문처리 
            #     queue.append(i)
                visited[i] = visited[node] + 1 
                queue.append(i)



n = int(input()) 
a,b = map(int,input().split())  # 촌수를 계산해야할 두 사람의 번호 
m = int(input()) 

graph = [[] for i in range(n+1)] 


for _ in range(m): 
    p1,p2 = map(int,input().split()) 
    graph[p1].append(p2)
    graph[p2].append(p1)

visited = [0] * (n+1)  

bfs(a) 

answer = visited[b] 

print(answer if answer > 0 else -1 )