import sys
input = sys.stdin.readline

n,m = map(int,input().split()) 
trees = list(map(int,input().split()))

start = 0
end = max(trees) 
answer = 0 
while start<=end:
    mid = (start+end) // 2 
    count = 0

    for tree in trees:
        if mid < tree:  # 나무길이가 더 길때 
            count += tree - mid 
    
    if count >= m:  
        answer = mid 
        start = mid + 1

    else:
        end = mid - 1 

print(answer)