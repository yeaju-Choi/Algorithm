# 통계학
# 산술평균 
# 중앙값 
# 최빈값
# 범위(최대값 - 최소값)

from collections import Counter
n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input())) 

#1. 산술 평균 
avg = sum(arr)/n

print("%.f"%avg)

# 2
arr.sort()
print(arr[n//2])

#3. 

# 최빈값


#4. 
print(arr[-1] -  arr[0])


