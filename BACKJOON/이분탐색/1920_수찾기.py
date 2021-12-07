
def binary_search(arr,find):
    
    start = 0
    end = len(arr)-1

    while start <= end:
        mid = (start+end) // 2 
        
        if arr[mid] == find:
            return 1
        
        elif arr[mid] > find: # 왼쪽에 있음 
            end = mid -1

        else:
            start = mid + 1
        
    return 0



n = int(input())

arr = list(map(int,input().split()))
arr.sort() 

m = int(input()) 
find = list(map(int,input().split()))

for data in find:
    answer = binary_search(arr,data)
    print(answer)

