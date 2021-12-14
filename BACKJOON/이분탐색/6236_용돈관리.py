'''
현우는 용돈을 효율적으로 활용하기 위해 계획을 짜기로 하였다.
 현우는 앞으로 N일 동안 자신이 사용할 금액을 계산하였고, 
 
돈을 펑펑 쓰지 않기 위해 정확히 M번만 통장에서 돈을 빼서 쓰기로 하였다. 
현우는 통장에서 K원을 인출하며, 통장에서 뺀 돈으로 하루를 보낼 수 있으면 그대로 사용하고, 
모자라게 되면 남은 금액은 통장에 집어넣고 다시 K원을 인출한다. 

다만 현우는 M이라는 숫자를 좋아하기 때문에, 
정확히 M번을 맞추기 위해서 남은 금액이 그날 사용할 금액보다 많더라도 남은 금액은 통장에 집어넣고 다시 K원을 인출할 수 있다. 
현우는 돈을 아끼기 위해 인출 금액 K를 최소화하기로 하였다. 현우가 필요한 최소 금액 K를 계산하는 프로그램을 작성하시오
'''

'''
1번째 줄에는 N과 M이 공백으로 주어진다. (1 ≤ N ≤ 100,000, 1 ≤ M ≤ N)

2번째 줄부터 총 N개의 줄에는 현우가 i번째 날에 이용할 금액이 주어진다. (1 ≤ 금액 ≤ 10000)
'''

'''
첫 번째 줄에 현우가 통장에서 인출해야 할 최소 금액 K를 출력한다
'''
import sys

input = sys.stdin.readline

n,m = map(int,input().split())  
spendarr = list()

for i in range(n):
    spendarr.append(int(input()))

# print(sum(spendarr)/m)

start = max(spendarr)
end = sum(spendarr) 

answer = 0

while start <= end:
    mid = (start + end) // 2  # 한번에 인출할 돈 
    
    temp = 0
    arr = list() 

    for data in spendarr: 
        temp += data 

        if temp > mid: # 오늘 쓴 돈이 인출한 돈을 초과함 
            temp -= data


            arr.append(temp) 
            temp = data  
    # 마지막 데이터가 안들어감 

    if temp: # 임시 데이터에 아직 데이터가 남아있다면 
        arr.append(temp)
    print("=> mid ", end = " ")
    print(mid)
    print(arr)

    if len(arr) > m:  # 오늘 쓸 금액을 늘려야함 
        
        start = mid + 1 
    
    else:
        answer = mid
        end = mid -1 


print(answer)
    

