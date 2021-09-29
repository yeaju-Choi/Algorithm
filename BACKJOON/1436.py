# 영화감독 숌 

n = int(input())

# 계속 돌아야될듯
# 숫자를 다 돌고 문자열로 체크?
count = 0
num = 666
while True:
    if "666" in str(num):
        count += 1
        if count == n:
            print(num)
            break
    num += 1
