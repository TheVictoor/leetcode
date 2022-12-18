
def maxPoints(grid: list[list[int]], queries: list[int]) -> list[int]:

    def get_points(spot, grid, item, visited, tokens):
        line, column = spot
        if spot in visited:
            return 0
        
        if grid[line][column] < item:
            tokens.append(1)
            # print(line, column, item, grid[line][column], visited, tokens)
            visited.append(spot)
            
            if line > 0:
                get_points([line-1, column], grid, item, visited, tokens)
    
            if line + 1 < len(grid):
                get_points([line+1, column], grid, item, visited, tokens)

            if column + 1 < len(grid[0]):
                get_points([line, column+1], grid, item, visited, tokens)

            if column > 0:
                get_points([line, column-1], grid, item, visited, tokens)
        else:
            visited.append(spot)

    points = []
    for q in queries:
        tokens = []
        get_points([0,0], grid, q, [],tokens)
        points.append(len(tokens))
    return points

    
print(maxPoints())