

def dfs(graph,v,visited,count):

    visited[v] = True
    count.append(1)

    graph[v].sort()

    for item in graph[v]:
        
        if visited[item] == False:
            dfs(graph,item,visited,count)
    

n = int(input())  # 정점 
m = int(input()) # 연결수 
count = []
graph = [[] for i in range(n+1)]  # 비어있는 그래프 리스트 만들기 
print(graph)

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)

visited = [False] * (n+1)

dfs(graph,1,visited,count)
print(len(count)-1)
print(count)




