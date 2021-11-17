
def solution(nums):
    answer = 0

    # 3개의 수를 더했을때 소수가 되는 경우의 수 
    
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                print(i,j,k)
                total = nums[i] + nums[j] + nums[k]
                
                if total > 1:
                    for l in range(2,total):
                        if total % l == 0:
                            continue
                        else:
                            answer += 1
                            break
                print(answer)
                
                
        

    return answer

solution([1,2,3,4,5,6,7])


# 다른 풀이 


def solution(nums):
    from itertools import combinations as cb
    answer = 0
    for a in cb(nums, 3):
        cand = sum(a)
        for j in range(2, cand):
            if cand%j==0:
                break
        else:
            answer += 1
    return answer
    