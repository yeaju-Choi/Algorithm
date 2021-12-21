
# def dfs(graph,n,visited):  
#     stack = list() 
#     stack.append(n)

#     visited[n] = True 
#     while stack:
#         now = stack.pop()  # 맨위에 요소를 뺌 
        
#         for i in graph[now]:
#             if not visited[i]: #아직 방문 안했다면 
#                 dfs(graph,i,visited) 


         


# n,m = map(int,input().split()) 

# graph = [[] for i in range(n+1)]

# for i in range(m): # 초기화 
#     a,b = map(int,input().split()) 

#     graph[a].append(b)
#     graph[b].append(a)


# print(graph)

# visited = [False] * n 



import sys 
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(graph,v,visited): 
    
    visited[v] = True

    
    for i in graph[ㅍ]:
        if not visited[i]: # False 일때 
            
            flag = True 
            dfs(graph,i,visited,flag)

    return flag 

n,m = map(int,input().split()) 
graph = [[] for i in range(n+1)] 

for i in range(m): 
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)

answer = 0

for i in range(1,n+1):
    
    if visited[i] == False: # 방문하지 않았을 때만 방문 
        answer += 1 
        dfs(graph,i,visited) 

print(answer)

