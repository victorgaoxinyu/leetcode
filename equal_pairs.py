from typing import List

def equalPairs(grid: List[List[int]]) -> int:

    cnt = 0
    columns = []
        
    for row_idx in range(0, len(grid)):
        print(row_idx)
        tmp_list = []
        for col_idx in range(0, len(grid)):
            tmp_list.append(grid[col_idx][row_idx])
        columns.append(tmp_list)
    
    print(columns)
    for i in grid:
        for j in columns:
            if i == j:
                cnt += 1
    
    return cnt
        # m[str(tmp_list)] = m.get(str(tmp_list), 0) + 1


# grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
grid = [[13,13],[13,13]]

print(equalPairs(grid))