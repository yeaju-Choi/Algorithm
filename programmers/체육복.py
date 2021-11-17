def solution(n, lost, reserve):
    answer = 0

    # 중복 제거 
    for i in list(reserve):
        if i in lost:
            del reserve[reserve.index(i)]
            del lost[lost.index(i)]

    print(lost)
    print(reserve)

    lost.sort()
    reserve.sort()

    answer = n - len(lost)

    for i in lost:
        if i-1 in reserve:
            del reserve[reserve.index(i-1)]
            answer += 1
        elif i+1 in reserve:        
            del reserve[reserve.index(i+1)]
            answer += 1    
        

    return answer


print(solution(8,[5,6],[4,5]))


'''
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)



'''