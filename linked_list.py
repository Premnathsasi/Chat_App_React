
class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class linkedlist:
    def __init__(self) -> None:
        self.head=None

    def insert_at_begining(self,data):
        node=Node(data,self.head)
        self.head=node
    
    def Print(self):
        if self.head is None:
            print('Linked list is empty')
            return
        itr=self.head
        llstr=''
        while itr:
            llstr+=str(itr.data)+ '->'
            itr=itr.next
        print(llstr) 

    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        
        itr=self.head
        while itr.next:
            itr=itr.next

        itr.next=Node(data,None)

    def insert_list(self,datalist):
        self.head=None
        for data in datalist:
            self.insert_at_end(data)


ll=linkedlist()
ll.insert_list(['Premnath','Sasi','Nalini','Preethi'])
ll.Print()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_after(self, target, data):
        new_node = Node(data)
        current = self.head
        while current:
            if current.data == target:
                new_node.next = current.next
                current.next = new_node
                break
            current = current.next

    def delete(self, data):
        if self.is_empty():
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def display(self):
        if self.head is None:
            print('Linked list is empty')
            return
        itr=self.head
        llstr=''
        while itr:
            llstr+=str(itr.data)+ '->'
            itr=itr.next
        print(llstr) 

linked_list = LinkedList()

linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.display()
linked_list.prepend(0)

linked_list.insert_after(2, 2.5)

linked_list.delete(1)

linked_list.display()  # Output: [0, 2, 2.5, 3]
