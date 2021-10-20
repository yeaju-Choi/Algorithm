# 균형잡힌 세상 

'''
하나 또는 여러줄에 걸쳐서 문자열이 주어진다. 
각 문자열은 영문 알파벳, 공백, 소괄호("( )") 대괄호("[ ]")등으로 이루어져 있으며, 길이는 100글자보다 작거나 같다.

입력의 종료조건으로 맨 마지막에 점 하나(".")가 들어온다.



각 줄마다 해당 문자열이 균형을 이루고 있으면 "yes"를, 아니면 "no"를 출력한다.


'''

# stack 하나로 관리 
# (와 [가 들어오면 push
# )와 ]가 들어오면 이전에 짝이 맞는게 있는지 확인하고 pop
# ) ] 가 stack이 비어있는데 들어오면  NO 

# 마지막에 스택이 비어있음 YES // 뭐 있음 YES 

arr = []

while(True):
    string = input()
    if string == '.':  # .이 들어오면 입력 끝
        break 
    arr.append(string) 


stack = []  # () 임시 저장공간 

for str in arr:
    for element in str:

        if element == "(" or element == "[":
            stack.append(element)

        if element == ")":

            if not stack: # 스택이 비어있는데 ) 들어오면 ㄴㄴ 
                stack.append(")")
                
                
            if stack[-1] == "(": #마지막거랑 짝이 맞을때만 삭제 
                del stack[-1] 
            else:
                break

        elif element == "]":
            if not stack:
                stack.append("[")
            
            if stack[-1] == "[":
                del stack[-1]
            else: 
                break

    if stack:
        print("no")
    else:
        print("yes")
    stack = [] # 스택 초기화
        


        

    
    

    

