class Solution:
    def isValid(self, s: str) -> bool:
        opened = []
        match = {
            "(" : ")",
            "{": "}",
            "[": "]"
        }
        for c in s:
            if c in ["(", "[", "{"]:
                opened.append(match.get(c))
            elif len(open) and c == opened[-1]:
                opened.pop()
            else:
                return False

        return True if len(opened) == 0 else False


print(Solution().isValid("("))
