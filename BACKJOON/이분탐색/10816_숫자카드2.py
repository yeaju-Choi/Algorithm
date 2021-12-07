# import sys
# input = sys.stdin.readline

# def binary_search(arr,find):
#     count = 0
#     start = 0

#     end = len(arr) - 1
#     while start <= end:

#         mid = (start + end) // 2 

#         if arr[mid] == find:
#             count += 1
#             del arr[mid]
            

#         elif arr[mid] > find:
#             end = mid - 1
            
#         else:
#             start = mid + 1



# n = int(input()) 
# card = list(map(int,input().split())) 

# m = int(input())
# find = list(map(int,input().split())) 


# card.sort()

# answer = [] 

# for data in find:
#     answer.append(binary_search(card,data)) 

# for i in answer:
#     print(i,end=" ")


##########################################
##########################################

# from collections import Counter

# N = int(input())

# Card_list = list(map(int, input().split()))   

# M = int(input())

# Card = list(map(int, input().split()))

# Card_counter = Counter(Card_list)

# print(Card_counter)

# for i in Card:
#     print(Card_counter[i], end=' ')
    


##########################################
##########################################

