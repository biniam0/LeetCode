class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        name_height = list(zip(heights, names))

        for _ in range(n):
            for i in range(n-1, 0, -1):
                if name_height[i][0] > name_height[i-1][0]:
                    name_height[i], name_height[i -
                                                1] = name_height[i-1], name_height[i]
        return [n for h, n in name_height]
