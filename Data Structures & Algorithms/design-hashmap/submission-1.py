class ListNode:
    def __init__(self,key=-1,value=-1):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.array_list = [ListNode() for x in range(10**4)]

    def put(self, key: int, value: int) -> None:
        hash = key % 10**4
        curr = self.array_list[hash]

        while curr.next:
            if curr.next.key == key:
                curr.next.value = value
                return
            curr = curr.next
        
        curr.next = ListNode(key,value)       

    def get(self, key: int) -> int:
        hash = key % 10**4
        curr = self.array_list[hash]

        while curr.next:
            if curr.next.key == key:
                return curr.next.value
            curr = curr.next
        
        return -1          

    def remove(self, key: int) -> None:
        hash = key % 10**4
        curr = self.array_list[hash]

        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next       


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)