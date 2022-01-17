# 연산자 문자열로 순열 만들기 

import sys 
from itertools import permutations 

input = sys.stdin.readline


n = int(input()) 
numbers = list(map(int,input().split()))
operator_input = list(map(int,input().split())) 

operator = ('+'*operator_input[0])+('-'*operator_input[1])+('*'*operator_input[2])+('/'*operator_input[3])

# print(operator)

p = list(permutations(operator, sum(operator_input)))
# print(p)
# 최대 10억 최소 -10억 
max_value = -1000000000 
min_value = 1000000000 


for i in p:
    total = numbers[0] # 첫번째 숫자는 넣고 시작 

    for j in range(0,len(numbers)-1):
        if (i[j]=='+'):
            total += numbers[j+1] 
        elif (i[j]=='-'):
            total -= numbers[j+1]
        elif (i[j]=='*'):
            total *= numbers[j+1]
        else :  # / 
            if (total < 0): # 양수로 바꾼뒤 몫을 취하고, 그 몫을 음수로 바꾸기
                
                total = (abs(total) // numbers[j+1]) * -1
            else:
                total = total // numbers[j+1]
        

    if (total > max_value):
        max_value = total 
    
    if ( total < min_value):
        min_value = total 


print(max_value)
print(min_value)
        








