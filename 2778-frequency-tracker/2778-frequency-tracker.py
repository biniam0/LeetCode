class FrequencyTracker:
    def __init__(self):
        self.occ = defaultdict(int)
        self.freq = defaultdict(int)

    def add(self, number: int) -> None:
        self.occ[number] += 1
        new_freq = self.occ[number]
        self.freq[new_freq] += 1
        self.freq[new_freq-1] -= 1


    def deleteOne(self, number: int) -> None:
        if self.occ[number] > 0:
            self.occ[number] -= 1
            f = self.occ[number]
            self.freq[f] += 1
            self.freq[f+1] -= 1        

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq[frequency] > 0
# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)