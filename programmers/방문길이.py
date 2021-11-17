def solution(dirs):
    answer = 0
    
    row, col = 5, 5  # 처음 캐릭터가 있는 위치
 
    row_visited = [[False] * 11 for _ in range(11)] # 가로줄
    col_visited = [[False] * 11 for _ in range(11)] # 세로줄
    print(col_visited)
 
    for command in dirs:
        if command == 'U':  
            if row == 0:     # 맨 위 
                continue
 
            row -= 1        # 한 칸 위로 이동하고 
            if col_visited[row][col]:  #  이미 방문했을 경우 
                continue
            else:
                col_visited[row][col] = True # 아니면 방문처리
                answer += 1 # answer 증가
 
        elif command == 'L':
            if col == 0:
                continue
 
            col -= 1
            if row_visited[row][col]:
                continue
            else:
                row_visited[row][col] = True
                answer += 1
 
        elif command == 'R':
            if col == 10:
                continue
 
            col += 1
            if row_visited[row][col]:
                continue
            
            else:
                row_visited[row][col] = True 
                answer += 1
 
        else:
            if row == 10:
                continue

            row += 1
            if col_visited[row][col]:
                continue
            else:
                col_visited[row][col] = True
                answer += 1
    # print(col_visited)
    return answer


print(solution("ULURRDLLU"))


'''
def solution(dirs):
    answer = 0
    dx = {"U" : 0, "D" : 0, "R" : 1, "L" : -1}
    dy = {"U" : -1, "D" : 1, "R" : 0, "L" : 0}
    prev = (0, 0)
    footprint = set()
    
    for d in dirs:
        _x, _y = prev
        x = _x + dx[d]
        y = _y + dy[d]
        if -5 <= x <= 5 and -5 <= y <= 5:
            foot = tuple(sorted([(_x, _y), (x, y)])) 
            footprint.add(foot)
            prev = (x, y)
    answer = len(footprint)

    return answer
    
'''