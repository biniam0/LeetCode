from sortedcontainers import SortedList

class NumberContainers:

    def __init__(self):
        self.idx_val = defaultdict(int)
        self.val_idx = defaultdict(SortedList)

    def change(self, index: int, number: int) -> None:
        if index in self.idx_val:
            tmp_val = self.idx_val[index]
            self.idx_val[index] = number
            self.val_idx[tmp_val].discard(index)
            if len(self.val_idx[number]) == 0:
                del self.val_idx[number]
            self.val_idx[number].add(index)
        else:
            self.idx_val[index] = number
            self.val_idx[number].add(index)

    def find(self, number: int) -> int:
        if len(self.val_idx[number]) and number in self.val_idx:
            return self.val_idx[number][0]
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)