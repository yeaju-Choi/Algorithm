import sys 

input = sys.stdin.readline

a,b = map(int,input().split()) 
lan = list()
for i in range(a):
    data = int(input()) 
    lan.append(data) 

lan.sort() 

end = sum(lan) // b 
start = 1
answer = 0
while start <= end:
    mid = (start+end)// 2 # 중간값
    

    count = 0
    for n in lan:
        count += n // mid
    if count >= b:
        start = mid + 1
    else:
        end = mid - 1 

print(end)


