#ATM

#  리스트를 오름차순으로 정렬
# 누적해서 더한값을 출력

n= int(input())


time = list(map(int,input().split()))
time.sort()

total = 0
answer = 0
for i in time:
    total += i
    answer += total

    

print(answer)
