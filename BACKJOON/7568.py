# 덩치 

n = int(input())
people = []
for i in range(n):
    people.append(input().split())
# print(people)

for i in range(n):
    grade = 1
    for j in range(n):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            grade += 1
    print(grade,end=" ")


#print(*리스트) 



