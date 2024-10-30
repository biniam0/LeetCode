class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)

        h_index = 0

        for cit in citations:
            if h_index + 1 > cit:
                break
            h_index += 1
        return h_index