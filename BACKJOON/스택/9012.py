# 괄호

'''
출력은 표준 출력을 사용한다.
 만일 입력 괄호 문자열이 올바른 괄호 문자열(VPS)이면 “YES”,
  아니면 “NO”를 한 줄에 하나씩 차례대로 출력해야 한다.  
'''

# (을 스택에 넣고 ) 가 나올때 pop
# 마지막에 괄호가 남아있다면 no

n = int(input())


arr = []
stack = []

for _ in range(n):
    arr.append(input())
    
for str in arr:
  for element in str:
    
    if element == '(': 
      stack.append(element) # (가 들어오면 스택에 추가 
      
    else:  # ) 가 들어올때 
      if len(stack) == 0: # 스택이 비어있으면 
        stack.append("end")
        break
        
      else: 
        del stack[-1] # 마지막요소 삭제 ()

     
  if stack: # 안에 뭐가 남아있음 NO
    print("NO")
  else: # 암것두 없으면 YES
    print("YES")
  stack = []
  



