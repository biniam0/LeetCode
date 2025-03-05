class DataStream:

    def __init__(self, value: int, k: int):
        self.val = value
        self.k = k   
        self.cnt = 0

    def consec(self, num: int) -> bool:
        if num == self.val:
            self.cnt += 1
        else:
            self.cnt = 0
            return False
        if self.cnt == self.k:
            self.cnt-=1
            return True
        return False

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)