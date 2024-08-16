class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res = [0]*len(temperatures)
        stack = [] 
        
        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackT, stackidx = stack.pop()
                res[stackidx] = idx - stackidx 
            
            stack.append((temp, idx))

        return res
            