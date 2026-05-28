class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkList:
    def __init__(self):
        self.head = None
    
    def insert(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        if temp.next is None:
            print(temp.data)
            return
        else:
            temp = self.head
            while temp:
                print(temp.data , end = " -> ")
                temp = temp.next
        print("None")
    def remove(self,data):
        temp = self.head
        pre = None
        if temp is not None:
            if temp.data == data:
                self.head = None
                temp = None
                return
            while temp is not None:
                if temp.data == data:
                    break
                pre = temp
                temp = temp.next
            if temp is None:
                return
            pre.next = temp.next
            temp = None
        
        
            
        
link = linkList()
link.insert(15)
link.insert(20)
link.insert(50)
link.insert(45)

link.display()
link.remove(50)
link.display()
        