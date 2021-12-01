
def dfs(graph,n,visited):  
    stack = list() 
    stack.append(n)

    visited[n] = True 
    while stack:
        now = stack.pop()  # 맨위에 요소를 뺌 
        
        for i in graph[now]:
            if not visited[i]: #아직 방문 안했다면 
                dfs(graph,i,visited) 


         


n,m = map(int,input().split()) 

graph = [[] for i in range(n+1)]

for i in range(m): # 초기화 
    a,b = map(int,input().split()) 

    graph[a].append(b)
    graph[b].append(a)


print(graph)

visited = [False] * n 

