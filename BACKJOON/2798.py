# 블랙잭 

n,m = map(int,input().split())

card = []
answer = 0

card = list(map(int,input().split()))

# 안겹치게 모든 경우의 수 돌기    
for i in range(0,len(card)-2,1):
    for j in range(i+1,len(card)-1,1):
        for k in range(j+1,len(card),1):
            if (card[i]+card[j]+card[k])<=m and (card[i]+card[j]+card[k])>answer:
                answer = card[i]+card[j]+card[k]

print(answer)
            
            

