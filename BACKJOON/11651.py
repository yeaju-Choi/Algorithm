# 좌표정렬하기 2 

# 좌표 정렬하기 
# 좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

# 람다로 정렬하면 될듯 


n = int(input())

arr = [] 

for _ in range(n):
    a,b = map(int,input().split())
    arr.append([a,b])

arr.sort(key=lambda x: x[0])
arr.sort(key=lambda x: x[1])



for i in arr:
    print(*i)
