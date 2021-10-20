# 스택 수열 
'''
입력된 수열을 만들기 위해 필요한 연산을 한 줄에 한 개씩 출력한다. 
push연산은 +로, pop 연산은 -로 표현하도록 한다. 
불가능한 경우 NO를 출력한다.
'''

# n값 될때까지 1부터 차례대로 스택에 넣고, + 넣기 .
# 입력된 수열 값이 차례대로 넣고 있었던 숫자보다 작다면 stack의 가장 위에 해당 수열값이 있는지 찾는다.
# 만약 맨 위의 값이 n이랑 같다면 pop을 한 후 -넣고  
# 그게 아니라면 만약 스택에 맨위값과 내가 지금 얻고 싶은 입력값 a가 다르다면 false를 준다.

n = int(input())

stack = []
result = []
count = 1
boolean = True

for _ in range(n): 

    num = int(input())   

    while count <= num: # 
        stack.append(count) # push함
        result.append("+") 
        count += 1


    if stack[-1] == num: # 마지막거랑 같으면 pop
        stack.pop()
        result.append("-")
    else:
        boolean = False
        break

if boolean == False:
    print("NO")
else:
    for i in result:
        print(i)