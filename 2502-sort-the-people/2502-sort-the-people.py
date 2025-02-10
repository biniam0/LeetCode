class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Using Bubble Sort
        n = len(names)
        name_height = list(zip(heights, names))

        # for _ in range(n):
        #     for i in range(n-1, 0, -1):
        #         if name_height[i][0] > name_height[i-1][0]:
        #             name_height[i], name_height[i -
        #                                         1] = name_height[i-1], name_height[i]
        # return [n for h, n in name_height]

        # Using Selection Sort
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if name_height[i][0] < name_height[j][0]:
        #             name_height[i], name_height[j] = name_height[j], name_height[i]

        # return [name for _, name in name_height]

        # Using Count Sorting
        max_h = max(heights)
        memo = [0]*(max_h+1)

        for h, n in name_height:
            memo[h] = (h, n)

        ans = []
        for i in range(len(memo)-1, -1, -1):
            if memo[i] != 0:
                ans.append(memo[i][1])

        return ans
        
