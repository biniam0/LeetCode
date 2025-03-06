class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in {"+", "-", "*", "/"}:
                stack.append(int(t))
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append(int(eval(f"{b}{t}{a}")))

        return stack[-1]
                