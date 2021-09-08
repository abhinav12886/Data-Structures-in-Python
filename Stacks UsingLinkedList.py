class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next  # This is a singly linked list


class Stack:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        print("isempty func is working")
        if self.head is None:
            return True
        else:
            return False

    def push(self):
        print("push func is working")
        if self.head is None:
            self.head = Node(value=int(input("enter the data you want to add: \n")))
        else:
            new_node = Node(value=int(input("enter the data you want to add: \n")))
            new_node.next = self.head
            self.head = new_node

    def displayStack(self):
        print("displayStack func is working")
        temp = self.head
        if self.isEmpty():
            print("Stack underflow")
        else:
            while temp is not None:
                print(temp.value)
                temp = temp.next
            return

    def pop(self):
        print("pop func is working")
        if self.isEmpty():
            return None
        else:
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            return poppednode.value

    def peek(self):
        print("peek func is working")
        if self.isEmpty():
            return None
        else:
            return self.head.value


obj = Stack()
obj.push()
obj.push()
obj.push()
obj.displayStack()
obj.peek()
obj.pop()
obj.displayStack()
obj.isEmpty()
obj.displayStack()