from itertools import groupby

def longest_subarray(nums: list[int]): 
    m = max(nums)
    res = 0
    for x, y in groupby(nums):
        y = list(y)
        print(m, x, y)
        if x == m:
            res = max(res, len(y))
    return res


def sort_by_heights(name, heights):
    l = [[i, j] for i, j in zip(heights, name)]
    l.sort(reverse=True)
    return [i[0] for i in l]
    ...


sort_by_heights(["ana", "joao", "maria", "paloma"], [169, 170, 168, 150])


