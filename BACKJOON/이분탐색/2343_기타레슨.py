
'''
블루레이의 크기를 두고 이분탐색을 한다 
0~강의길이의 합 


'''


import sys 
input = sys.stdin.readline

n,m = map(int,input().split()) 
lectures = list(map(int,input().split()))  # 강의의 길이 

# 블루레이의 크기가 범위가 될거임 
start = 0
end = sum(lectures) 

answer = 0
while start <= end: 

    mid = (start + end) // 2 
    blueray = list()
    index = 0
    temp = 0
    for data in lectures: 
        # blueray[index] += data 
        

        temp += data
        if temp > mid: # 다음칸에 넣어야함 
            temp -= data
            blueray.append(temp)
            
            temp = data
        
    if temp:
        blueray.append(temp)

        # if temp <= data: # 지금 더 넣을 있음 
            
        
        # if blueray[index] > m:
        #     blueray[index] -= data
        #     index += 1 
        #     blueray[index] += data 
            
    # print("==> mid", end =" ")
    # print(mid)
    # print("==> dictronary", end =" ")
    # print(blueray)

    if len(blueray) > m:
        
        start = mid + 1
        
    
    elif len(blueray) <= m : # 줄여야함 
        answer = max(blueray) 
        end = mid - 1 
    

print(answer)
    
     
    


    
        
    