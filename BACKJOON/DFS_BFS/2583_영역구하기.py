'''
첫째 줄에 M과 N, 그리고 K가 빈칸을 사이에 두고 차례로 주어진다.
 M, N, K는 모두 100 이하의 자연수이다. 
 둘째 줄부터 K개의 줄에는 한 줄에 하나씩 직사각형의 왼쪽 아래 꼭짓점의 x, y좌표값과 오른쪽 위 꼭짓점의 x, y좌표값이 빈칸을 사이에 두고 차례로 주어진다. 
 모눈종이의 왼쪽 아래 꼭짓점의 좌표는 (0,0)이고, 오른쪽 위 꼭짓점의 좌표는(N,M)이다. 입력되는 K개의 직사각형들이 모눈종이 전체를 채우는 경우는 없다


첫째 줄에 분리되어 나누어지는 영역의 개수를 출력한다. 둘째 줄에는 각 영역의 넓이를 오름차순으로 정렬하여 빈칸을 사이에 두고 출력한다.

5 7 3
0 2 4 4
1 1 2 5
4 0 6 2

'''

import sys 
from collections import deque
input = sys.stdin.readline 


def mark_graph(position):  
    left_x,left_y,right_x,right_y = position  
    # right_x -= 1 
    # right_y -= 1 

    for x in range(left_x,right_x,1): 
        for y in range(left_y,right_y,1):
            graph[x][y] = 1 


    
def bfs(x,y): 
    queue = deque() 
    queue.append((x,y)) 
    
    graph[x][y] = 1  # 자기자신도 mark 
    count = 1
    while queue: 
        a,b = queue.popleft() 

        for i in range(4):
            cur_x = a + dx[i]
            cur_y = b + dy[i] 
            
            if cur_x >= 0 and cur_x < h and cur_y >= 0 and cur_y < w:
                if graph[cur_x][cur_y] == 0: 
                    graph[cur_x][cur_y] = 1
                    count += 1 
                    queue.append((cur_x,cur_y))


    return count 
    
        




w,h,k = map(int,input().split()) 

rect = list()  # 직사각형 좌표를 담을 리스트
for i in range(k): 
    
    rect.append(list(map(int,input().split()))) 


graph = list()  

for i in range(h):
    graph.append(list([0] * w )) 


for pos in rect:  # 직사각형 좌표를 그래프에 색칠
    mark_graph(pos)




dx = [0,0,1,-1]
dy = [1,-1,0,0]

answer = 0 
area_answer = list() 

for i in range(h):
    for j in range(w):
        if graph[i][j] == 0:
            area_result = bfs(i,j)
            answer += 1
            area_answer.append(area_result)
print(answer)
area_answer.sort() 
print(*area_answer)
