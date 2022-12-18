def deleteGreatestValue(grid: list[list[int]]) -> int:
        for row in grid: 
            row.sort()
            
        deleteds = []
            
        while len(grid[0]):
            max_deleted = 0
            for row in grid:
                max_value = row.pop()
                max_deleted = max(max_deleted, max_value)
            deleteds.append(max_deleted)
        
        return sum(deleteds)
                    
print(deleteGreatestValue([[1,2,4],[3,3,1]]))

[
    [1,2,4],
    [3,3,1]
]
