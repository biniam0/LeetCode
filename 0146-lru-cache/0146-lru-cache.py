class ListNode:
    def __init__(self, key=0, val=0):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self, head, tail):
        self.head = head 
        self.tail = tail
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def remove(self, node):
        left = node.prev
        right = node.next

        left.next = right
        right.prev = left

    def add(self, node):
        left = self.tail.prev
        right = self.tail

        left.next = node 
        right.prev = node

        node.next = right
        node.prev = left

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.cache = {}
        self.head = ListNode() 
        self.tail = ListNode() 
        self.head.next = self.tail
        self.tail.prev = self.head
        self.ll = LinkedList(self.head, self.tail)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.ll.remove(node)
        self.ll.add(node)
        return node.val


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value

            self.ll.remove(node)
            self.ll.add(node)
        else:
            if self.capacity == len(self.cache):
                removed_node = self.head.next
                self.ll.remove(removed_node)
                
                removed_key = removed_node.key
                del self.cache[removed_key]

            new_node = ListNode(key, value)
            self.ll.add(new_node)
            self.cache[key] = new_node

            

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)