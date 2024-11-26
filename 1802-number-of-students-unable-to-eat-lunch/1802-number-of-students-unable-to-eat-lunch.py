class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stud_queue = deque(students)
        sandwiches.reverse()
        no_count_change = 0

        while stud_queue:
            popped_stud = stud_queue.popleft()
            if sandwiches[-1] == popped_stud:
                sandwiches.pop()
                no_count_change = 0
            else:
                stud_queue.append(popped_stud)
                no_count_change += 1

            if no_count_change == len(stud_queue):
                break

        return no_count_change
