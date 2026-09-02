class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        cur = self.head.next

        while cur != self.tail and index > 0:
            cur = cur.next
            index -= 1

        if cur != self.tail and index == 0:
            return cur.val

        return -1

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)

        next_node = self.head.next

        new_node.prev = self.head
        new_node.next = next_node

        self.head.next = new_node
        next_node.prev = new_node

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)

        prev_node = self.tail.prev

        new_node.prev = prev_node
        new_node.next = self.tail

        prev_node.next = new_node
        self.tail.prev = new_node

    def addAtIndex(self, index: int, val: int) -> None:

        # Negative index means add at head
        if index < 0:
            index = 0

        cur = self.head.next

        while cur != self.tail and index > 0:
            cur = cur.next
            index -= 1

        # cur can be a normal node OR the dummy tail
        if index == 0:
            new_node = ListNode(val)

            new_node.prev = cur.prev
            new_node.next = cur

            cur.prev.next = new_node
            cur.prev = new_node

    def deleteAtIndex(self, index: int) -> None:
        cur = self.head.next

        while cur != self.tail and index > 0:
            cur = cur.next
            index -= 1

        if cur != self.tail and index == 0:
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)