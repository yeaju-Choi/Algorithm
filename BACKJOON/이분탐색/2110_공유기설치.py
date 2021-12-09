'''
1. array라는 리스트에 집들의 좌표를 입력받은 후에 정렬.

2. start = 1, end = array[-1] - array[0] 으로 설정. ( 시작값은 최소 거리, 끝 값은 최대 거리 )

3. 앞 집부터 공유기 설치

4. 설치할 수 있는 공유기 개수가 c개를 넘어가면 더 넓게 설치할 수 있다는 이야기 이므로 설치거리를 mid + 1로 설정하여 다시 앞집부터 설치.

5. c개를 넘어가지 않는다면 더 좁게 설치해야 한다는 이야기 이므로 mid - 1로 설정.

 
 '''

import sys 
input = sys.stdin.readline
n,c = map(int,input().split()) 

house = list()
for i in range(n):
    house.append(int(input())) 

house.sort() 

# 좌표값의 최소값
start = 1
# 가장 높은 좌표와 가장 낮은 좌표의 차이
end = house[-1] - house[0]

result = 0

while (start <= end):
    mid = (start+end)//2 # 공유기의 간격 
    old = house[0]
    count = 1

    for i in range(1, len(house)):
        if house[i] >= old+mid: # gap 이상
            count+=1
            old = house[i]
    print('count : ',end =" ")
    print(count)
    if count >=c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)

