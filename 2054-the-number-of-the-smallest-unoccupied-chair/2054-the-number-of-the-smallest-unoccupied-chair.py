class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        # Step 1: Sort times by arrival time
        times_with_indices = sorted(enumerate(times), key=lambda x: x[1][0])
    
        # Step 2: Min-heap for available chairs
        available_chairs = []
        for i in range(len(times)):
            heapq.heappush(available_chairs, i)
        
        # Step 3: Min-heap for friends leaving (to release chairs)
        leaving_heap = []
        
        # Step 4: Process arrivals and departures
        for i, (arrival, leaving) in times_with_indices:
            # Release any chairs from friends who have already left
            while leaving_heap and leaving_heap[0][0] <= arrival:
                _, chair = heapq.heappop(leaving_heap)
                heapq.heappush(available_chairs, chair)
            
            # Assign the smallest available chair to the current friend
            assigned_chair = heapq.heappop(available_chairs)
            
            # If this is the target friend, return their chair number
            if i == targetFriend:
                return assigned_chair
            
            # Push this friend's leaving time and assigned chair to the leaving heap
            heapq.heappush(leaving_heap, (leaving, assigned_chair))