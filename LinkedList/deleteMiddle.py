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
    
    def deleteMiddle(self):
            low=high=self.head
            prev = None
            while(high and high.next):
                prev = low
                low = low.next
                high = high.next.next
            print(prev.data)
            prev.next = low.next
            print(prev.data)
            return self.head


if __name__ == "__main__":
    list1 = LinkedList()
    list1.insert_at_end(1)
    list1.insert_at_end(30)
    list1.insert_at_end(3)
    list1.insert_at_end(4)
    list1.insert_at_end(5)
    list1.insert_at_end(6)
    list1.insert_at_end(7)
    list1.insert_at_end(8)
    list1.printList()
    list1.deleteMiddle()
    list1.printList()
    
