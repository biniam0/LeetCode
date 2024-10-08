class Solution:
    def minSwaps(self, s: str) -> int:
        extra_closing = 0
        max_ = 0
        for char in s:
            if char == "]":
                extra_closing += 1
            else:
                extra_closing -= 1
            max_ = max(max_, extra_closing)
        return (max_+1)//2