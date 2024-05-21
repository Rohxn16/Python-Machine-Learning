
class Node:

    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtBeginning(self,data):
        node = Node(data,self.head)
        self.head = node
    
    def printLL(self):
        if self.head == None:
            print('The list is empty')
            return

        itr = self.head
        while itr:
            print(itr.data,' -> ',end='')
            itr = itr.next 
        print('NULL')       

    def insertAtEnd(self,data):
        
        if self.head is None:
            self.insertAtBeginning(data)
            return
        
        # travel to the last node
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data,None)

    def insertValues(self,data_list):
        # self.head = None
        for data in data_list:
            self.insertAtEnd(data)

    def getLength(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count
    
    def removeIndex(self,index):
        count = 0
        if index<0 or index>=self.getLength():
            raise Exception('Not a valid index.')
        
        if index == 0:
            self.head = self.head.next
            return
        
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1
    
    def insertAtIndex(self,index,data):

        if index == 0:
            self.insertAtBeginning(index)
            return
        
        itr = self.head
        for i in range(0,index-1):
            itr = itr.next;

        node = Node(data)
        node.next = itr.next
        itr.next = node
        return


if __name__ == '__main__':
    ll = LinkedList()
    ll.insertAtBeginning(5)
    ll.insertAtBeginning(4)
    ll.insertAtBeginning(3)
    ll.insertAtBeginning(2)
    ll.insertAtBeginning(1)
    ll.insertAtEnd(6)
    ll.insertValues(['red','blue','black'])
    ll.removeIndex(1)
    # print(ll.getLength())
    ll.insertAtIndex(3,7)
    ll.printLL()
    
    