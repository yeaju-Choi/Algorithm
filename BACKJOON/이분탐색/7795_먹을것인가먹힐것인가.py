'''
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 
각 테스트 케이스의 첫째 줄에는 A의 수 N과 B의 수 M이 주어진다.
둘째 줄에는 A의 크기가 모두 주어지며, 셋째 줄에는 B의 크기가 모두 주어진다.
크기는 양의 정수이다. (1 ≤ N, M ≤ 20,000
'''

'''
각 테스트 케이스마다, A가 B보다 큰 쌍의 개수를 출력한다.
'''

import sys 
input = sys.stdin.readline
t = int(input()) 

def binary_search(data,start,end):
    
    # print("now data => ", end =" ")
    # print(data)
    answer = 0
    while start <= end:
        mid = (start + end) // 2 

        if prey[mid] < data:
            # answer = len(prey[:mid+1]) 
            # answer = len(prey[:mid+1]) 
            answer = mid + 1
            start = mid + 1
        else:
            end = mid - 1 


        # print("answer => ", end =" ")
        # print(answer)
    return answer 
        

for i in range(t):
    n,m = map(int,input().split()) 
    predator = list(map(int,input().split())) 
    prey = list(map(int,input().split())) 
    prey.sort() 

    start = 0
    end = len(prey) - 1 


    answer = 0

    for i in predator:
        answer += binary_search(i,start,end)

    print(answer)


