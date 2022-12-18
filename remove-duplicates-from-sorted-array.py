class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        d = {}
        r = []
        e = []
        for n in enumerate(nums):
            if not d.get(n):
                d[n] = 1
                r.append(n)
            else:
                e.append("_")

        nums.clear()
        nums.extend(r)
        nums.extend(e)    
        
        return len(r)

print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))