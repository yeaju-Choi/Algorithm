# 2로 나누어 떨어지면 순간이동 홀수일 경우는 1칸을 움직여야하기때문에 1개의 건전지를 쓴다.


def solution(n):
    ans = 1
    while n != 1:
        if n % 2 != 0:
            ans += 1
            n -= 1
        else:
            n /= 2

    return ans



'''
def solution(n):
    return bin(n).count('1')
    
'''