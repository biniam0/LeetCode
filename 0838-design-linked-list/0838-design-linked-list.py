class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.dummy = ListNode(0)
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        seeker = self.dummy.next
        for _ in range(index):
            seeker = seeker.next
        return seeker.val if seeker else -1

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.dummy.next
        self.dummy.next = newNode
        self.size += 1
                
    def addAtTail(self, val: int) -> None:
        cur = self.dummy
        newNode = ListNode(val)

        while cur.next and cur:
            cur = cur.next
        cur.next = newNode
        self.size += 1
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        newNode = ListNode(val)
        cur = self.dummy
        for _ in range(index):
            cur = cur.next
            
        newNode.next = cur.next
        cur.next = newNode
        self.size += 1  
        
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        seeker = self.dummy
        
        for _ in range(index):
            seeker = seeker.next
        
        if seeker.next:
            seeker.next = seeker.next.next
            self.size -= 1

        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)