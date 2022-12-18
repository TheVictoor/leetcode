class Solution:
    def maxJump(self, stones: list[int]) -> int:
        if len(stones) > 2:
            diff = []
            for i in range(len(stones)-2):
                diff.append(abs(stones[i] - stones[i+2]))
        else:
            diff = stones

        return max(diff) 
    