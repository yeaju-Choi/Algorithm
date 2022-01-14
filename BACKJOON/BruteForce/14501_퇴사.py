'''

상담원으로 일하고 있는 백준이는 퇴사를 하려고 한다.

오늘부터 N+1일째 되는 날 퇴사를 하기 위해서, 남은 N일 동안 최대한 많은 상담을 하려고 한다.

백준이는 비서에게 최대한 많은 상담을 잡으라고 부탁을 했고, 비서는 하루에 하나씩 서로 다른 사람의 상담을 잡아놓았다.

각각의 상담은 상담을 완료하는데 걸리는 기간 Ti와 상담을 했을 때 받을 수 있는 금액 Pi로 이루어져 있다.

N = 7인 경우에 다음과 같은 상담 일정표를 보자.

 	1일	2일	3일	4일	5일	6일	7일
Ti	3	5	1	1	2	4	2
Pi	10	20	10	20	15	40	200

1일에 잡혀있는 상담은 총 3일이 걸리며, 상담했을 때 받을 수 있는 금액은 10이다. 5일에 잡혀있는 상담은 총 2일이 걸리며, 받을 수 있는 금액은 15이다.

상담을 하는데 필요한 기간은 1일보다 클 수 있기 때문에, 모든 상담을 할 수는 없다. 예를 들어서 1일에 상담을 하게 되면, 2일, 3일에 있는 상담은 할 수 없게 된다. 2일에 있는 상담을 하게 되면, 3, 4, 5, 6일에 잡혀있는 상담은 할 수 없다.

또한, N+1일째에는 회사에 없기 때문에, 6, 7일에 있는 상담을 할 수 없다.

퇴사 전에 할 수 있는 상담의 최대 이익은 1일, 4일, 5일에 있는 상담을 하는 것이며, 이때의 이익은 10+20+15=45이다.

상담을 적절히 했을 때, 백준이가 얻을 수 있는 최대 수익을 구하는 프로그램을 작성하시오.

'''

'''
첫째 줄에 N (1 ≤ N ≤ 15)이 주어진다.

둘째 줄부터 N개의 줄에 Ti와 Pi가 공백으로 구분되어서 주어지며, 1일부터 N일까지 순서대로 주어진다. (1 ≤ Ti ≤ 5, 1 ≤ Pi ≤ 1,000)

'''
'''
첫째 줄에 백준이가 얻을 수 있는 최대 이익을 출력한다.
'''

# 어차피 n의 갯수가 15이하이기때문에 전체를 돌아도 시간이 충분할 거라고 생각함.
# 상담 날짜를 1일부터 n일까지 시작하는 범위를 다 체크해보기 
# 아 꼭 상담끝난 후 날짜에 바로 해야하는거 x -> 중간에 비워도 됌 

import sys 
input = sys.stdin.readline

n = int(input()) 
schedule = list() 

# def calculteProfit(day):
#     profit = 0
#     index = day
#     while index < n and (schedule[index][0] + index) < n:  
#         profit += schedule[index][1] 
#         index += schedule[index][0] 
#         if index > n:
#             break

#     return profit


for _ in range(n):
    t,p = map(int,input().split())
    schedule.append([t,p])


# answer = 0
# for i in range(0,n):
#     answer = max(calculteProfit(i),answer)

# print(answer)


# DP 방식으로 해결해야한다고 한다.. 
# 상담이 끝나는 날이 n을 넘어가게 되면 일을 못함 -->  answer[i] = answer[i+1]
# 현재일을 맡았을때 들어오는 보상 + 현재 일을 끝낸 다음에 쌓여있는 보상 
# 일을 맡지 않을 경우 보상 
# -> 둘 비교 

answer = [0] * (n + 1)
                   

for i in range(n - 1, -1, -1):
    if schedule[i][0] + i > n:
        answer[i] = answer[i + 1]
    else:
        answer[i] = max(schedule[i][1] + answer[i + schedule[i][0]], answer[i + 1])
        
print(answer[0])