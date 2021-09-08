class Node:
    def __init__(self, value=None, next=None, previous=None):
        self.value = value
        self.next = next
        self.prev = previous  # For doubly linkedlist

    """
    This is the structure of the Node
    """


class LinkedList:
    def __init__(self):
        self.head = None

    """
    This is the LinkedList class constructor 
    """

    def addNodeFront(self):
        """
        adding node at the front
        """
        new_node = Node(value=input("Enter the data..\n"))
        new_node.next = self.head
        self.head = new_node
        new_node.next = n1

    def addNodeAny(self):
        pos = int(input("enter the position where to insert"))
        new_node = Node(value=int(input("enter the value to be inserted")))
        p = self.head
        i = 1
        while i < pos - 1:
            p = p.next
            i += 1
        new_node.next = p.next
        p.next = new_node

    def displayNode(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def delete(self):
        key = int(input("enter the index position to be deleted"))

        if self.head is None:
            print("list is empty")  # check if the list is empty or not

        current = self.head
        z = 1
        while z < key - 1:  # it will run upto the position-2 node
            current = current.next
            z += 1
        e = current.next.value  # it contains the value deleted
        current.next = current.next.next

        return e

    """
    These are the different functions of linked list 
    """


n1 = Node(3)  # n1 is the first node object of Node class with value 3
n2 = Node(4)  # n2 is the second node Object with value 4
n3 = Node(5)  # n3 is the third node object with value 5
n4 = Node(7)
n5 = Node(9)
n6 = Node(10)

LL = LinkedList()  # LL object created of the LinkedList class
LL.head = n1  # head pointed to n1 node
n1.next = n2  # n1 node pointed to n2 using next of Node class
n2.next = n3  # n2 node pointed to n3 using next of Node class
n3.next = n4
n4.next = n5

LL.displayNode()
# LL.addNodeFront()
# LL.displayNode()
# LL.delete()
# LL.displayNode()
LL.addNodeAny()
LL.displayNode()