class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1 = candidate1 = count2 = candidate2 = 0

        for num in nums:
            if count1 == 0 and num != candidate2:
                count1 = 1
                candidate1 = num
            elif count2 == 0 and  candidate1 != num:
                count2 = 1
                candidate2 = num

            elif num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1

        
        result = []
        threshold = len(nums)//3
        cnt1 = cnt2 = 0
        for num in nums:
            if num == candidate1:
                cnt1 += 1
            elif candidate2 == num:
                cnt2 += 1
        
        if cnt1 > threshold:
            result.append(candidate1)
        if cnt2 > threshold:
            result.append(candidate2)

        return result

        
        