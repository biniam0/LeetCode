class Solution(object):
    def smallestNumber(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return num
        if num > 0:
            num = list(str(num))
            num.sort()
            l = 0
            for r in range(1, len(num)):
                if num[l] == "0" and num[r] != "0":
                    num[l], num[r] = num[r], num[l]
                    break
            return int("".join(num))
        else:
            num = str(num).lstrip("-")
            num = sorted(num, reverse=True)
            num = int("".join(num))
            return num - 2*num
                
            
            