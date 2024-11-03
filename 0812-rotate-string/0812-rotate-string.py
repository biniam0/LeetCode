class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        s = deque(s)
        for i in range(len(s)+1):
            if s == deque(goal):
                return True
            tmp = s.popleft()
            s.append(tmp)
            
        return False