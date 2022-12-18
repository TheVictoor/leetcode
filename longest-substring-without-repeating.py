class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        streaks = []
        streak= []
        for x in range(len(s)):
            if x == 0 or s[x] not in streak:
                streak.append(s[x])
            else:
                streaks.append(streak.copy())
                streak = streak[streak.index(s[x])+1:]
                streak.append(s[x])
        streaks.append(streak.copy())
        max_streak = len(max(streaks, key=lambda i: len(i)))
        return max_streak

print(Solution().lengthOfLongestSubstring("dvdf"))
