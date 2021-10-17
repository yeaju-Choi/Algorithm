# 단어 정렬 

'''
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

1. 길이가 짧은 것부터
2. 길이가 같으면 사전 순으로

* 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력한다. 
=> set을 써서 중복을 제거해야 할듯 
'''

n = int(input())

arr = []
for _ in range(n):
    arr.append(input())

arr = list(set(arr)) # 중복 제거 
print(arr)
answer = [] 
min = arr[0]
for i in range(1,len(arr)+1):
    if len(min) > len(arr[i]):
        min = i
    answer.append(min)
    del arr[arr.index(min)]
# print(answer)





