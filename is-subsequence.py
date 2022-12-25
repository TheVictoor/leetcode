class Solution:
    def isSubsequece(self, s: str, t: str):
        ps = 0 

        for i in range(len(t)):
            if t[i] == s[ps]:
                ps+=1
                if ps == len(s):
                    return True
            
        return False


print(Solution().isSubsequece('axc', 'ahbgdc'))