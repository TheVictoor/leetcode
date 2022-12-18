class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        s_reverse = s[::-1]

        if s == s_reverse:
            return True

        return False