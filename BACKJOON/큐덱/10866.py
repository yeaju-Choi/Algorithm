# 덱

'''
push_front X: 정수 X를 덱의 앞에 넣는다.
push_back X: 정수 X를 덱의 뒤에 넣는다.
pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 덱에 들어있는 정수의 개수를 출력한다.
empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

'''

from collections import deque
from sys import stdin 

n = int(stdin.readline()) 
q = deque()

for _ in range(n):

    cmd = stdin.readline().split()

    if cmd[0] == "push_front":
        q.insert(0,cmd[1])
    
    elif cmd[0] == "push_back":
        q.append(cmd[1])
    
    elif cmd[0] == "pop_front":
        if q:
            print(q.popleft())
        else:
            print(-1)
    
    elif cmd[0] == "pop_back":
        if q:
            print(q.pop())
        else:
            print(-1)
    
    elif cmd[0] == "size":
        print(len(q))

    elif cmd[0] == "empty":
        if q:
            print(0)
        else:
            print(1)

    elif cmd[0] == "front":
        if q:
            print(q[0])
        else:
            print(-1)
    
    elif cmd[0] == "back":
        if q:
            print(q[-1])
        else:
            print(-1)


