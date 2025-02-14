class ProductOfNumbers:

    def __init__(self):
        self.stream = []
        self.prefix_prod = [1]
        self.size = 0
        
    def add(self, num: int) -> None:
        if num == 0:
            self.prefix_prod = [1]
            self.size = 0
            return 
        self.prefix_prod.append(self.prefix_prod[self.size]*num)
        self.size += 1

    def getProduct(self, k: int) -> int:
        if k > self.size:
            return 0
        return self.prefix_prod[self.size]//self.prefix_prod[self.size-k]
        

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)