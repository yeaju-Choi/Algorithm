def sol12919():
    s = input()
    t = input()

    

    def appendA(arr): 
        if arr == t: 
            return 1
        if arr.count >= t.count:
            return 0
        
        temp = arr
        temp + 'A'
        return temp 


    def appendBAndReversed(arr): 
        
        if arr == t:
            return 1
        if arr.count >= t.count_: 
            return 0
        temp = arr 
        temp + 'B'
        temp.reverse()
        return temp 
        
      
    print(s.count)
    print(t.count)  
        
    # print(appendA(s) + appendBAndReversed(s))
    
    
sol12919()