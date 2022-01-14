class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self,data):
        NewNode = Node(data,self.head)
        if self.head == None:
            self.head = NewNode
            return self.head
        else:
            itr = self.head
            while itr.next:
                itr = itr.next

            itr.next = NewNode
            NewNode.next = None
            return NewNode

    def printList(self):
        # base case
        if self.head == None:
            print("LinkedList is empty")
        else:
            itr = self.head
            concat = ''
            while itr:
                concat += str(itr.data)+'->'
                itr = itr.next

            print(concat)
    
    def detectCycle2(self, node):
        length = 0
        slow=fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = self.head
        while(curr != slow and slow.next):
            curr = curr.next
            slow = slow.next
        
        return slow.data if slow !=None else 0

if __name__ == "__main__":
    list1 = LinkedList()
    list1.insert_at_end(3)
    list1.insert_at_end(2)
    list1.insert_at_end(0)
    list1.insert_at_end(4)
    list1.insert_at_end(3)
    list1.printList()
    print(list1.detectCycle2(1))
    list1.printList()
    
