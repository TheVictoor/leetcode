def longestSquareStreak(nums: list[int]) -> int:
    nums.sort(reverse=True)
    print(nums)
    d = {}
    for i in nums:
        d[i] = d.get(i*i, 0) + 1
    t = max(d.values())
    return t if t >= 2 else -1



# def longestSquareStreak(nums: list[int]) -> int:
#     nums.sort()

#     hash_t = {}
#     visited = {}

#     for n in nums:
#         hash_t[n] = 1

#     streak = 0

#     for n in nums:
#         if n not in visited:
#             visited[n] = 1
#             strk = 1
#             while 1:
#                 new = n*n
#                 if hash_t.get(new):
#                     strk+=1
#                     visited[new] = 1
#                     n = new
#                 else:
#                     break

#             streak = max(streak, strk)

#     return -1 if streak <= 1 else streak

print(longestSquareStreak([2,3,4,5,6,16,24]))