def solution(n, arr1, arr2):
    answer = []
    
    
    for i in range(n):
        
        a = list((bin(arr1[i])))
        b = list(bin(arr2[i]))
        
        a = a[2:]
        b = b[2:]
        
        while len(a) != n:
            a.insert(0,'0')

        while len(b) != n:
            b.insert(0,'0')

        # print(a)
        # print(b)

        temp = []
        for i in range(n):
            if a[i] == '1' or b[i] == '1' : # 벽임 
                temp.append("#")
            else:
                temp.append(" ")
        
        answer.append("".join(temp))

        # print(answer)

    return answer


# solution(5,[9, 20, 28, 18, 11],	[30, 1, 21, 17, 28])


'''

def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer
    
'''