
def matchingAnswer(answers,arr):
    count = 0
    length_a = len(arr)
    index = 0
    for i in range(len(answers)):
        
        if i != 0 and (i%length_a == 0): 
            index = 0
    
        if answers[i] == arr[index]:
            count +=1


        index += 1
    

    return count 


def solution(answers):
    answer = []
    answer_dict = dict()
    
    
    giveupMath = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    for index,item in enumerate(giveupMath):
        # answer.append([index+1,matchingAnswer(answers,item)])
        answer_dict[index+1] = matchingAnswer(answers,item)

    max_answer = max(answer_dict.values())
    print(max_answer)
    print(answer_dict)


    for k,v in answer_dict.items():
        if max_answer == v:
            answer.append(k)

    return answer



print(solution([1,3,2,4,2]))