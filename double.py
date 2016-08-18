class Node():
    def __init__(self,data=None,next=None,previous=None):
        self.data=data
        self.next=next
        self.previous=previous
    def get_data(self):
        return self.data

    def set_data(self,data):
        self.data=data

    def getNext(self):
         return self.next

    def setNext(self,next):
        self.next=next
    def setPrevious(self,previous):
        self.previous=previous
    def getPrevious(self):
        return self.previous

class Doublell(Node):
    def __init__(self):
        self.head=Node()

    def add_before(self,data):
        if self.head.get_data()==None:
            node=Node(data)
            self.head=node
        else:
            current=self.head
            node=Node(data)
            current.setPrevious(node)
            node.setNext(current)
            self.head=node

    def add_after(self,data):
        if self.head.getNext()==None:
            node=Node(data)
            self.head=Node
        else:
            current = self.head
            while current.getNext()!=None:
                current=current.getNext()
            node = Node(data)
            node.setPrevious(current)
            current.setNext(node)

    def remove_before(self):


        current=self.head
        current = current.getNext()
        self.head=current
        current.getNext().setPrevious(None)
        current.setPrevious(None)

    def remove_after(self):
        current=self.head
        while current.getNext()!=None:
            current=current.getNext()
        #current.getNext(None)
        current = current.getPrevious()
        current.getNext().setPrevious(None);

        current.setNext(None)

    def search(self,data):
        current=self.head
        while current:
            if current.get_data() == data:
                print(data)
            else:
                pass
                #print("no data")
            current=current.getNext()



    def display(self):
        current=self.head

        while current.getNext()!=None:
            print(current.get_data())
            current=current.getNext()
        print(current.get_data())

list=Doublell()
list.add_before(9)
list.add_before(10)
list.add_before(11)
list.display()
print("================")
list.add_after(13)
list.add_after(15)
list.display()
print("================")
list.remove_before()
list.display()
print("##########")
list.remove_after()
list.display()
print("#!!!!!!!!!!!!!")
list.search(13)
#list.display()
#print(list.search(13))













