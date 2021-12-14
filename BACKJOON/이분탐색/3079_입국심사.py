import sys 
import heapq
input = sys.stdin.readline

n,m = map(int,input().split()) # 심사대 개수와, 상근이와친구들 수 
arr = list()

# for i in range(n):
#     item = int(input())
#     arr.append((item,item))


# # print(arr)
# for i in range(m-1):
#     item,original = heapq.heappop(arr)
#     answer += item 
#     heapq.heappush(arr,(item+original,original))
#     # print(arr)


# print(arr[0][0])

for i in range(n):
    arr.append(int(input()))

start = 0
end = m * max(arr) # 걸릴수 있는 최대 시간 
answer = 0

# print(arr)
while start <= end:
    mid = (start + end) // 2
    print(" mid ==> ", end = " ")
    print(mid)
    judgedPeople = 0

    # 나온 인원수가 m명보다 많으면 그 시간이 가능
    #  나온 인원수가 m명보다 적으면 그 시간은 불가능 

    for item in arr:
        judgedPeople += mid // item
    

    print(" people ==> ", end = " ")
    print(judgedPeople)
    if judgedPeople < m:
        start = mid + 1
    else:
        answer = mid
        end = mid - 1



'''
예를 들어, 두 심사대가 있고, 심사를 하는데 걸리는 시간이 각각 7초와 10초라고 하자. 줄에 서 있는 사람이 6명이라면,

 가장 첫 두 사람은 즉시 심사를 받으러 가게 된다. 7초가 되었을 때, 첫 번째 심사대는 비어있게 되고,
  세 번째 사람이 그곳으로 이동해서 심사를 받으면 된다. 10초가 되는 순간, 네 번째 사람이 이곳으로 이동해서 심사를 받으면 되고, 14초가 되었을 때는 다섯 번째 사람이 첫 번째 심사대로 이동해서 심사를 받으면 된다. 20초가 되었을 때, 두 번째 심사대가 비어있게 된다. 하지만, 여섯 번째 사람이 그 곳으로 이동하지 않고, 1초를 더 기다린 다음에 첫 번째 심사대로 이동해서 심사를 받으면, 모든 사람이 심사를 받는데 걸리는 시간이 28초가 된다. 만약, 마지막 사람이 1초를 더 기다리지않고, 첫 번째 심사대로 이동하지 않았다면, 모든 사람이 심사를 받는데 걸리는 시간이 30초가 되게 된다.


'''