
# # 모든 집을 돌면서 만약 집이 있다면 없는데로 바꾸고 연결되어있는곳 계속 탐색 

# countarr = []

# def dfs(x,y):

#     global count

#     if x < 0 or x >= n or y < 0 or y >= n:
#         return False

#     if graph[x][y] == 0:
#         return False

#     if graph[x][y] == 1:
#         count += 1  # 빈집일때마다 count를 셈 

#         graph[x][y] = 0

#         dfs(x-1,y)
#         dfs(x+1,y)
#         dfs(x,y-1)
#         dfs(x,y+1)
        
#         return True

#     return False   
    

# n = int(input())
# graph = []
# result = 0
# count = 0
# for i in range(n):
#     graph.append(list(map(int,input())))

# #print(graph)

# for i in range(n):
#     for j in range(n):
#         count = 0
#         bool_ = dfs(i,j)
        
#         if bool_ == True:
#             result += 1 
#             countarr.append(count)

# print(result)
# countarr.sort()
# for i in countarr:
#     print(i)




#2667 단지번호붙이기
import sys



def apart_sol(matrix,cnt,x,y):
    dx=[-1,0,1,0]
    dy=[0,-1,0,1]
    matrix[x][y]=0
    queue=[]
    queue.append((x,y))

    while queue:
        x,y=queue.pop()
        for i in range(4):
            temp_x=x+dx[i]
            temp_y=y+dy[i]
            if temp_x < 0 or temp_y < 0 or temp_x >= n or temp_y >= n:
                continue

            if matrix[temp_x][temp_y]==1:
                cnt+=1
                matrix[temp_x][temp_y]=0
                queue.append((temp_x,temp_y))

    return cnt

n = int(sys.stdin.readline())

lines=[]

for i in range(n):
    line = list(map(int, sys.stdin.readline().strip()))
    lines.append(line)

cnt=1
ans=[]
for i in range(n):
    for j in range(n):
        value=int(lines[i][j])

        if value==1:
            ans.append(apart_sol(lines,cnt,i,j))
        else:
            continue

print(len(ans))
for i in sorted(ans):
    print(i)

