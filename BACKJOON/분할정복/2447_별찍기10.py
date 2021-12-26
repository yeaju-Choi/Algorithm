# # n = 3^i 일때는 가운데를 비워두고 n = 3^(i-1) 일때의 별 배열이 찍힘 

# def draw_star(n): # n = 9 
#     global Map 

#     if n == 3: 
#         Map[0][:3] = Map[2][:3] = [1]*3
#         Map[1][:3] = [1,0,1]
#         return 
    
#     a = n // 3 

#     draw_star(n//3)   # draw_star(3)
#     for i in range(3):
#         for j in range(3):
#             if i == 1 and j == 1:  # i = 0, j = 0
#                 continue 
#             for k in range(a): 
#                 Map[a*i+k][a*j:a*(j+1)] = Map[k][:a]
#     # map[3*0+0][3*0 ~ 3*1] = map[0][2] (1,1,1)
#     # map[3*0,1][]
    

# n = int(input())
# Map = [[0 for i in range(n)] for i in range(n)] 

# # print(Map)
# draw_star(n)
# for i in Map:
#     for j in i:
#         if j:
#             print("*", end='')
#         else:
#             print(' ',end='')
#     print()

import sys 
sys.setrecursionlimit(10**6) 
def append_star(LEN): 
    if LEN == 1: 
        return ['*'] 
    Stars = append_star(LEN//3) 
    L = [] 
    print(Stars)
    for S in Stars:
        print('=>',Stars)
        L.append(S*3) 
        print(L)
    for S in Stars: 
        L.append(S+' '*(LEN//3)+S) 
    for S in Stars: 
        L.append(S*3) 
        
    return L 
    

n = int(sys.stdin.readline().strip()) 
print('\n'.join(append_star(n)))

