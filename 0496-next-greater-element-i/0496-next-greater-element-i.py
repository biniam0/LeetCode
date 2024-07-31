class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next = defaultdict(lambda:-1)
        
        for num in nums2:
            while stack and stack[-1] < num:
                next[stack.pop()] = num
            stack.append(num)
        
        return [next[num] for num in nums1]
        
        
        
        
        # res = []

        # l = 0
        # while l < len(nums1):
        #     for r in range(len(nums2)):
        #         if nums1[l] == nums2[r]:
        #             if r+1 == len(nums2):
        #                 res.append(-1)
        #             elif nums2[r] < nums2[r+1]:
        #                 res.append(nums2[r+1])
        #             else:
        #                 res.append(-1)
        #     l += 1
        # return res