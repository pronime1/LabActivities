def fibonacci(p):
    if p <=0:
        return "invalid"
    elif p ==1:
        return 0
    elif p ==2:
        return 1

    return fibonacci(p-1) + fibonacci(p-2)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linklist:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last.next = new_node

    def print_recursion(self, node):
        if node is Node:
            return
        print(node.data)
        self.print_recursion(node.next)

    def start_recursion_traversal(self):
        self.print_recursion(self.head)


if __name__ == "__main__":
    linklist = Linklist()

    linklist.insert(5)
    linklist.insert(10)
    linklist.insert(15)
    linklist.insert(20)

    print("Linked List")
    linklist.start_recursion_traversal()

