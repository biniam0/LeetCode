class NumArray():
    def __init__(self, nums):
        self.nums = nums
        self.prefix_sum = []

        cur_sum = 0
        for num in self.nums:
            cur_sum += num
            self.prefix_sum.append(cur_sum)

    def sumRange(self, left, right):
        if left == 0:
            return self.prefix_sum[right]
        else:
            return self.prefix_sum[right] - self.prefix_sum[left-1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)