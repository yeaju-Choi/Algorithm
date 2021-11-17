def solution(n, words):
    answer = [0,0]
    temp = list()    

    count = 2
    around = 1

    temp.append(words[0])
    for word in range(1,len(words)):


        if (words[word][0] != words[word-1][-1]) or words[word] in temp:
            # 종료조건 
            # print(count,round) 
            answer = [count,around]
            return answer

        temp.append(words[word])    

        if count == n:
            count = 1
            around += 1
        else:
            count += 1 

    return answer
