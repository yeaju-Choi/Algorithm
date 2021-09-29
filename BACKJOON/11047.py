# 동전 

n,m = map(int,input().split())
coins = []
answer = 0
for _ in range(n):
    
    coins.append(int(input()))

coins.reverse()

# coin이 m보다 작을때만 카운트 
# 몫을 더해주고 그 나머지를 가지고 다시 계산 

for coin in coins:
    if coin <= m:
        answer += m // coin   
        m = m % coin
        
    else:
        continue

    
print(answer)

    