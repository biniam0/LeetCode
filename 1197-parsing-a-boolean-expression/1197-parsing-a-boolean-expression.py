class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        s = expression
        i = 0

        def helper():
            nonlocal i
            c = s[i]
            i += 1
            if c == "t":
                return True
            if c == "f":
                return False
            if c == "!":
                i += 1
                res = not helper()
                i += 1 
                return res
            
            sub_arr = []
            i += 1
            while s[i] != ")":
                if s[i] != ",": 
                    sub_arr.append(helper())
                else:
                    i += 1
            i += 1
            if c == "&":
                return all(sub_arr)
            if c == "|":
                return any(sub_arr)

        return helper()

