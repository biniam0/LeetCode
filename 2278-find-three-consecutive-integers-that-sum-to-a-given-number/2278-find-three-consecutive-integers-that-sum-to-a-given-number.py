class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        x = num / 3

        if x == num//3:
            return [int(x-1), int(x), int(x+1)]
        else:
            return []