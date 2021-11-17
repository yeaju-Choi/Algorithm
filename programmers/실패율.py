def fail_percent(arr,stage):
    
    all_ = 0
    not_clear = 0
    
    for i in arr:
        if i >= stage:
            all_ += 1   
        
    not_clear = arr.count(stage)
        

    
    return not_clear/all_
                

def solution(N, stages):
    answer = []
    result = []
    stage_dict = dict()
    for stage in range(N):
        
        # answer.append((stage+1,fail_percent(stages,stage+1)))
        
        stage_dict[stage+1] = 0 # 딕셔너리 초기화 
        stage_dict[stage+1] = fail_percent(stages,stage+1)
    
    
    
    # answer = sorted(answer, key=lambda x : (-x[1], x[0]))
    
    # for i,j in answer:
    #     result.append(i)
    # print(result)
    return sorted(stage_dict, key=lambda x : stage_dict[x], reverse=True)
    


solution(5,[2, 1, 2, 6, 2, 4, 3, 3]	)
# result [3,4,2,1,5]
    
        
        
        