class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        prefix_common_array = [0] * n

        
        elements_in_A, elements_in_B = set(), set()

        
        for current_index in range(n):

            
            elements_in_A.add(A[current_index])
            elements_in_B.add(B[current_index])

            common_count = 0
            for element in elements_in_A:
                if element in elements_in_B:
                    common_count += 1
            prefix_common_array[current_index] = common_count
        return prefix_common_array