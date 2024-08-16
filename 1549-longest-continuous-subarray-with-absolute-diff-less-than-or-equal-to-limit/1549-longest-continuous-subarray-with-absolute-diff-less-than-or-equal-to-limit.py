class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        min_q = deque()
        max_q = deque()
        l = 0
        res = 0

        for r in range(len(nums)):
            while min_q and min_q[-1] > nums[r]:
                min_q.pop()
            while max_q and max_q[-1] < nums[r]:
                max_q.pop()

            min_q.append(nums[r])
            max_q.append(nums[r])

            while max_q[0] - min_q[0] > limit:
                if nums[l] == max_q[0]:
                    max_q.popleft()
                if nums[l] == min_q[0]:
                    min_q.popleft()
                l += 1

            res = max(res, r-l+1)

        return res
            