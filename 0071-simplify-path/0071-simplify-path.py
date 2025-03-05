class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []

        for i in range(len(path)):
            if stack and path[i] == "..":
                stack.pop()
            elif path[i] == "." or path[i] == "" or path[i] == "..":
                continue
            else: stack.append(path[i])

        return "/" + "/".join(stack)

        
