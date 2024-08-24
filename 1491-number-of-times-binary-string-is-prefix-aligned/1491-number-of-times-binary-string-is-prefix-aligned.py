class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        right_most = 0
        count = 0

        for i, flip in enumerate(flips):
            right_most = max(flip, right_most)

            if right_most == i + 1:
                count += 1

        return count