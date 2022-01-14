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
    
    # Merge Linked Lists
    def mergeLists(self,list1,list2):
        temp = Node(0)
        currNode = temp
        
        while(list1 != None and list2 != None):
            if(list1.data <= list2.data):
                currNode.next = list1
                list1 = list1.next
            else:
                currNode.next = list2
                list2 = list2.next
            currNode = currNode.next
        
        while(list1 != None):
            currNode.next = list1
            list1 = list1.next
        
        while list2 != None:
            currNode.next = list2
            list2 = list2.next

        return temp.next


if __name__ == "__main__":
    ll1 = LinkedList()
    ll2 = LinkedList()
    ll2.insert_at_end(1)
    ll2.insert_at_end(3)
    ll2.insert_at_end(3)
    ll2.insert_at_end(5)
    ll2.insert_at_end(5)

    ll1.insert_at_end(2)
    ll1.insert_at_end(4)
    ll1.insert_at_end(6)
    ll1.printList()
    ll2.printList()
    # new list
    ll3 = LinkedList()
    # print(ll1.head.data, ll2.head.data, sep=" ")
    ll3.head = ll3.mergeLists(ll1.head, ll2.head)
    ll3.printList()
