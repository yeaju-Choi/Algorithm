import sys 

input = sys.stdin.readline

t = int(input())  # 테스트 케이스 갯수 

def binarysearch(data,start,end):
    while start <= end:
        mid = (start + end) // 2 

        if note1[mid] == data:
            return 1
        
        elif data > note1[mid]:
            start = mid + 1
        
        else:
            end = mid - 1 
    return 0 


for i in range(t):
    n = int(input()) # 수첩 1 에 적어놓은 정수의 갯수 
    note1 = list(map(int,input().split()))  
    m = int(input()) # 수첩 2 에 적어놓은 정수의 갯수 
    note2  = list(map(int,input().split()))  # note1에 이숫자들이 있는지 찾아야함

    note1.sort() 

    start = 0
    end = len(note1) - 1 

    for data in note2:
        if binarysearch(data,start,end):
            print(1)
        else:
            print(0)



        