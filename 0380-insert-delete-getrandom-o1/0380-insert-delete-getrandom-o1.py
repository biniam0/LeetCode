class RandomizedSet:

    def __init__(self):
        self.num_map = {}
        self.nums = []


    def insert(self, val: int) -> bool:
        res = val not in self.num_map

        if res:
            self.num_map[val] = len(self.nums)
            self.nums.append(val)
        return res

    def remove(self, val: int) -> bool:
        res = val in self.num_map
        if res:
            idx = self.num_map[val]
            last_val = self.nums[-1]

            self.nums[idx] = last_val
            self.nums.pop()
            self.num_map[last_val] = idx
            del self.num_map[val]

        return res

    def getRandom(self) -> int: 
        return random.choice(self.nums)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()