class ListNode:
    def __init__(self, link=""):
        self.link = link
        self.next = None
        self.prev = None

class BrowserHistory:
    def __init__(self, homepage: str):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        self.cur_pos = 0

        new_page = ListNode(homepage)
        self.head.next = new_page
        self.tail.prev = new_page
        new_page.prev = self.head
        new_page.next = self.tail
        self.cur = new_page
        self.cur.next = self.tail.prev
        self.size += 1
        self.cur_pos += 1
        


    def visit(self, url: str) -> None:
        new_page = ListNode(url)
        new_page.prev = self.cur
        new_page.next = self.tail

        self.cur.next = new_page
        self.tail.prev = new_page


        self.cur = new_page
        self.size += 1
        self.cur_pos += 1      

    def back(self, steps: int) -> str:
        while steps > 0 and self.cur.prev != self.head:
            self.cur = self.cur.prev
            steps -= 1
        self.cur_pos -= (steps + 1)
        return self.cur.link

    def forward(self, steps: int) -> str:
        while steps > 0 and self.cur.next != self.tail:
            self.cur = self.cur.next
            steps -= 1
        self.cur_pos += (steps+1)
        return self.cur.link

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)