
# -*- coding: utf-8 -*-
# 회의실 배정  
print("hello") 

n = int(input())

meeting = []

for _ in range(n):
    s, e = map(int, input().split())
    meeting.append([s, e])

print(meeting)