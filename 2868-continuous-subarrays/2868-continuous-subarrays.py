class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        n = len(nums)
        max_deque = deque()
        min_deque = deque()
        l = 0
        ans = 0

        for r in range(n):
            while max_deque and nums[max_deque[-1]] <= nums[r]:
                max_deque.pop()
            max_deque.append(r)

            while min_deque and nums[min_deque[-1]] >= nums[r]:
                min_deque.pop()
            min_deque.append(r)

            while nums[max_deque[0]] - nums[min_deque[0]] > 2:
                l += 1
                if max_deque[0] < l:
                    max_deque.popleft()
                if min_deque[0] < l:
                    min_deque.popleft()

            ans += (r - l + 1)

        return ans
