#분해합 

n = int(input())
answer = 0
for i in range(1,n+1,1):
    num = list(map(int,str(i)))  # 하나씩 나눠서 리스트에 넣기 
    sum_num = sum(num) + i
    if sum_num == n:
        answer = i
        break
print(answer)

