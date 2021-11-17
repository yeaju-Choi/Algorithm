# 베스트 셀러

'''
김형택은 탑문고의 직원이다. 김형택은 계산대에서 계산을 하는 직원이다. 
김형택은 그날 근무가 끝난 후에, 오늘 판매한 책의 제목을 보면서 가장 많이 팔린 책의 제목을 칠판에 써놓는 일도 같이 하고 있다.

오늘 하루 동안 팔린 책의 제목이 입력으로 들어왔을 때, 가장 많이 팔린 책의 제목을 출력하는 프로그램을 작성하시오.

'''

'''
첫째 줄에 오늘 하루 동안 팔린 책의 개수 N이 주어진다. 이 값은 1,000보다 작거나 같은 자연수이다. 
둘째부터 N개의 줄에 책의 제목이 입력으로 들어온다. 책의 제목의 길이는 50보다 작거나 같고, 알파벳 소문자로만 이루어져 있다.
'''

'''
첫째 줄에 가장 많이 팔린 책의 제목을 출력한다. 만약 가장 많이 팔린 책이 여러 개일 경우에는 사전 순으로 가장 앞서는 제목을 출력한다.


'''



# from collections import Counter

# n = int(input())
# book = list()
# for _ in range(n):
#     book.append(input())


# book.sort()
# c = Counter(book).most_common(1)
# print(c[0][0])


'''
other solution

# 등장횟수를 셀때는 딕셔너리를 활용하면 좋다 
'''


n = int(input())
books = dict()

for i in range(n):
    book = input()
    if book not in books:
        books[book] = 1
    else:
        books[book] += 1


max_num = max(books.values())
arr = []

for k,v in books.items():
    if max_num == v:
        arr.append(k)
    

arr.sort()
print(arr[0])



