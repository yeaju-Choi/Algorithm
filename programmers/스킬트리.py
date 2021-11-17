skill = "CBD"

skill_tress = ["BACDE", "CBADF", "AECB", "BDA"]

def solution(skill, skill_trees):
    answer = 0
    

    new_arr = [] 
    


    for skil in skill_trees:
        
        del_skill = ''.join(x for x in skil if x in skill) 
        new_arr.append(del_skill)
                
    for skil in new_arr:
        if skill.startswith(skil):
            answer += 1



    return answer       

'''

def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer

'''