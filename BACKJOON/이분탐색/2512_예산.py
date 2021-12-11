import sys 
input = sys.stdin.readline

n = int(input()) 
budget_list = list(map(int,input().split())) 
max_budget = int(input()) 

start = 0
end = max(budget_list) 

while start<=end:
    mid = (start + end) // 2  # 예산 상한액 
   
    total_budget = 0
    for data in budget_list: 
        total_budget += min(data,mid)  # 상한액보다 높을 순 x 
    

    if total_budget <= max_budget: # 지출양이 최대값보다 작음 
        start = mid + 1 
    else:
        end = mid - 1 


print(end) 



