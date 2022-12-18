from itertools import permutations

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
            elif len(opened) and c == opened[-1]:
                opened.pop()
            else:
                return False


        return True if len(opened) == 0 else False


    def generateParenthesis1(self, n: int) -> list[str]:
        s = ("("*n)+(")"*n)
        p = permutations(s, n*2)
        st = set(p)
        a = ["".join(l) for l in st]
        return [l for l in a if self.isValid(l)]

    def generateParenthesis(self, n: int) -> list[str]:
        p = set()

        def permute(l, r, s, c):
            if l == 0 and r == 0:
                p.add(c)
                return
            if l > 0:
                permute(l-1, r, s+1, c+"(")
            if r > 0 and s > 0:
                permute(l, r-1, s-1,c+")")    

        permute(n, n, 0, "")

        return list(p)

print(Solution().generateParenthesis(8))
