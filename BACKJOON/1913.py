
# -*- coding: utf-8 -*-
# 회의실 배정  

n = int(input())

meeting = []

for _ in range(n):
    s, e = map(int, input().split())
    meeting.append([s, e])


meeting.sort(key=lambda x: (x[1], x[0]))




lastTime = 0
count = 0
for biginTime, endTime in meeting:
  if biginTime >= lastTime:
    count += 1
    lastTime = endTime

print(count)

