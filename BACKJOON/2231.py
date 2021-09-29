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

# for else 

# 다른 풀이 


N = int(input())
lst = []

for num in range(N, 0, -1):  # num = 245
    sumn = 0
    strN = str(num)  # "245"
    for i in strN:  # "2", "4", "5"
        sumn += int(i)  # sumn = 2+4+5
    result = num + sumn  # result = 245+2+4+5
    if result == N:
        lst.append(num)

# print(lst)
if not lst:
    print(0)
else:
    print(min(lst))