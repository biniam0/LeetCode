class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        frequency = defaultdict(int)
        mini = 0

        for rab in answers:
            frequency[rab] += 1

        for answer, freq in zip(frequency.keys(), frequency.values()):
            total = ceil(freq / (answer + 1)) * (answer + 1)
            mini += total

        return mini