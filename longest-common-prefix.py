class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs2 = [list(s) for s in strs]
        streak = []
        for chars in zip(*strs2):
            if len(set(chars)) != 1:
                break
            streak.append(chars[0])
        return "".join(streak) 
        
        
print(Solution().longestCommonPrefix(["flitch","fly","flin"]))
