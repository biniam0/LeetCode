class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        lock = []
        unlocked = []

        for i in range(len(s)):
            if locked[i] == "0":
                unlocked.append(i)
            elif s[i] == "(":
                lock.append(i)
            else:
                if lock:
                    lock.pop()
                elif unlocked:
                    unlocked.pop()
                else:
                    return False
        while lock and unlocked and lock[-1] < unlocked[-1]:
            lock.pop()
            unlocked.pop()
        if lock:
            return False
        return True