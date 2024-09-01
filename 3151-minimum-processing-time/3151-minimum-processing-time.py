class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks = sorted(tasks, reverse=True)
        processorTime = sorted(processorTime)

        p_idx = 0
        ans = 0

        for p in processorTime:
            curr_max = 0 
            taskcount = 0

            while p_idx < len(tasks) and taskcount < 4:
                curr_max = max(curr_max, p + tasks[p_idx])
                p_idx += 1
                taskcount += 1

            ans = max(ans, curr_max)
        
        return ans