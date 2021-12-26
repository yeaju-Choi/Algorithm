'''
루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.


첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 
둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.
'''


import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())
graph = [[] for _ in range(N+1)]

#부모 노드 저장
parents = [0 for _ in range(N+1)]

# 트리 구조 입력
for _ in range(N-1) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
print(graph)
def DFS(start) :
    # 연결된 노드들부터 parents[i]의 부모가 없으면 부모 설정 해주고, DFS 돌린다.
    for i in graph[start] :
        if parents[i] == 0 :
            parents[i] = start
            DFS(i)


DFS(1)

for i in range(2, N+1) :
    print(parents[i])

print(parents)
