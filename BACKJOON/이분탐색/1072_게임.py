x,y = map(int,input().split())  # 전체게임 , 이긴 판 

start = 1
end = x-y 
answer = 0
z = (y*100//x)  # 현재 승률 
if z >= 99: # 이미 승률 100 % 
    print(-1)
    exit()

while start <= end:
    mid = (start + end ) // 2
    
    # mid+y -> 현재 승률이 바뀌었는지 확인 
    
    if ((y+mid)*100//(x+mid)) > z:
        
        answer = mid
        end = mid -1
        
    else:
        
        start = mid + 1

print(answer)
    
    