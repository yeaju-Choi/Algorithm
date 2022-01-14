'''
오늘은 스타트링크에 다니는 사람들이 모여서 축구를 해보려고 한다. 축구는 평일 오후에 하고 의무 참석도 아니다.
축구를 하기 위해 모인 사람은 총 N명이고 신기하게도 N은 짝수이다.
이제 N/2명으로 이루어진 스타트 팀과 링크 팀으로 사람들을 나눠야 한다.

BOJ를 운영하는 회사 답게 사람에게 번호를 1부터 N까지로 배정했고, 아래와 같은 능력치를 조사했다.
능력치 Sij는 i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치이다.
팀의 능력치는 팀에 속한 모든 쌍의 능력치 Sij의 합이다. 
Sij는 Sji와 다를 수도 있으며, i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치는 Sij와 Sji이다.


i\j	1	2	3	4
1	 	1	2	3
2	4	 	5	6
3	7	1	 	2
4	3	4	5	 
예를 들어, 1, 2번이 스타트 팀, 3, 4번이 링크 팀에 속한 경우에 두 팀의 능력치는 아래와 같다.

스타트 팀: S12 + S21 = 1 + 4 = 5
링크 팀: S34 + S43 = 2 + 5 = 7
1, 3번이 스타트 팀, 2, 4번이 링크 팀에 속하면, 두 팀의 능력치는 아래와 같다.

스타트 팀: S13 + S31 = 2 + 7 = 9
링크 팀: S24 + S42 = 6 + 4 = 10
축구를 재미있게 하기 위해서 스타트 팀의 능력치와 링크 팀의 능력치의 차이를 최소로 하려고 한다. 
위의 예제와 같은 경우에는 1, 4번이 스타트 팀, 2, 3번 팀이 링크 팀에 속하면 스타트 팀의 능력치는 6, 
링크 팀의 능력치는 6이 되어서 차이가 0이 되고 이 값이 최소이다.
'''

'''
첫째 줄에 N(4 ≤ N ≤ 20, N은 짝수)이 주어진다. 
둘째 줄부터 N개의 줄에 S가 주어진다. 
각 줄은 N개의 수로 이루어져 있고, i번 줄의 j번째 수는 Sij 이다.
 Sii는 항상 0이고, 나머지 Sij는 1보다 크거나 같고, 100보다 작거나 같은 정수이다.
'''

'''
첫째 줄에 스타트 팀과 링크 팀의 능력치의 차이의 최솟값을 출력한다
'''

# 엥 어차피 능력치(Sij)는 1이상이니까 0인거 빼고 그냥 리스트에 때려박고 
# n/2개씩 뽑아서 비교해주면 되지 않을까?! 

import sys
input = sys.stdin.readline
from itertools import combinations 

team = list() 
n = int(input()) 
# for _ in range(n):  
#     team.append(list(map(int,input().split())))

# teamarr = sum(team, [])


# teamarr = [x for x in teamarr if x != 0]

# startTeam = 0
# linkTeam = 0 

# all = list(combinations(teamarr, n//2)) 

# tempMax = sum(all[0])

# answer = list()
# print(all)
# for i in range(1,len(all)-1):
    
#     answer.append(abs(tempMax - sum(all[i]))) 
#     print('all ->',end=" ")
#     print(all[i])

# print(min(answer))

def subsum(tp1, tp2):
    sumA, sumB = 0, 0
    for i in tp1:
        for j in tp1:
            sumA += S[i][j]
    for i in tp2:
        for j in tp2:
            sumB += S[i][j]
    return abs(sumA-sumB)


N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]  # Sij: 1~100

comb_lst = list(combinations(range(N), N//2))
res = sys.maxsize
for i in range(len(comb_lst)//2):
    tmp = subsum(comb_lst[i], comb_lst[len(comb_lst)-1-i])
    if tmp < res:
        res = tmp

print(res)






