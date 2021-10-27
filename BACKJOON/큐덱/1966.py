# 프린터 큐 

'''
현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.
예를 들어 Queue에 4개의 문서(A B C D)가 있고, 중요도가 2 1 4 3 라면 C를 인쇄하고, 다음으로 D를 인쇄하고 A, B를 인쇄하게 된다.

여러분이 할 일은, 현재 Queue에 있는 문서의 수와 중요도가 주어졌을 때, 어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것이다. 예를 들어 위의 예에서 C문서는 1번째로, A문서는 3번째로 인쇄되게 된다.
'''

'''
테스트케이스의 첫 번째 줄에는 문서의 개수 N(1 ≤ N ≤ 100)과,
 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수 M(0 ≤ M < N)이 주어진다. 
 이때 맨 왼쪽은 0번째라고 하자. 두 번째 줄에는 N개 문서의 중요도가 차례대로 주어진다.
  중요도는 1 이상 9 이하의 정수이고, 중요도가 같은 문서가 여러 개 있을 수도 있다.
'''

# m(몇번째 놓여있는지)을 따로 리스트로 저장?  
# 큐에서 꺼낸값이 최대값일때 - 아닐때 
# 최대값일때 꺼낸값이 내가 찾아야하는 doc
# 최대값일때 꺼낸값이 내가 찾는게 아닐때 

# 최대값아닐때 
# rotate 

from collections import deque


a = int(input())
for _ in range(a):
    n,m = map(int, input().split())
    q = deque(map(int, input().split()))
    index = []  # 내가 찾을 인덱스를 저장할 리스트 
    for i in range(n):
        index.append(0)
    
    index[m] = 1  # 내가 찾아야하는 인덱스만 mark 
    answer = 1 
    while True: 
        if q[0] == max(q):  # 큐에서 꺼낸 값이 최대값일때 
            if index[0] == 1:
                break
            else: 
                q.popleft()
                index.pop(0)
                answer += 1
        else:
            q.append(q.popleft())
            index.append(index.pop(0))
    print(answer)





