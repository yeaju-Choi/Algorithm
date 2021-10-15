# 소트인사이드 

# 입력받은 문자열을 내림차순해야함 
# 리스트에 하나씩 옮기기 


n = input()
arr = []
result=''
for i in range(len(n)):
    arr.append(n[i])
arr.sort(reverse=True)

for i in range(len(arr)):
    result += arr[i]
print(result)