class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        n, m = len(s), len(part)

        i = 0
        while i < n:
            sl = len(stack)
            if stack and stack[-1] == part[-1]:
                if "".join(stack[sl-m:]) == part:
                    l = m
                    while stack and l > 0:
                        stack.pop()
                        l -= 1
            stack.append(s[i])
            i += 1
        sl = len(stack)
        if "".join(stack[sl-m:]) == part:
            l = m
            while stack and l > 0:
                stack.pop()
                l -= 1
        return "".join(stack)
            
