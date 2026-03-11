class SimpleArray:
    def __init__(self):
        self.data = []

    def insert(self, index, value):
        self.data.insert(index, value)

    def delete(self, index):
        if 0 <= index < len(self.data):
            return self.data.pop(index)
        raise IndexError("Index out of range.")

    def access(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        raise IndexError("Index out of range.")

    def display(self):
        return self.data


class SimpleMatrix:
    def __init__(self, rows, cols, default_value=0):
        self.rows = rows
        self.cols = cols
        self.data = [[default_value for _ in range(cols)] for _ in range(rows)]

    def insert(self, row, col, value):
        self.data[row][col] = value

    def delete(self, row, col):
        self.data[row][col] = 0

    def access(self, row, col):
        return self.data[row][col]

    def display(self):
        for row in self.data:
            print(row)


class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty.")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty.")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        return self.items


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        return self.items.pop(0)

    def front(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        return self.items


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def delete_value(self, value):
        if self.head is None:
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.data != value:
            current = current.next

        if current.next:
            current.next = current.next.next

    def traverse(self):
        elements = []
        current = self.head

        while current:
            elements.append(current.data)
            current = current.next

        return elements


def main():
    print("ARRAY")
    arr = SimpleArray()
    arr.insert(0, 10)
    arr.insert(1, 20)
    arr.insert(2, 30)
    print("After insertions:", arr.display())
    print("Access index 1:", arr.access(1))
    arr.delete(1)
    print("After deletion:", arr.display())

    print("\nMATRIX")
    matrix = SimpleMatrix(2, 3)
    matrix.insert(0, 0, 5)
    matrix.insert(1, 2, 9)
    matrix.display()
    print("Access [1][2]:", matrix.access(1, 2))
    matrix.delete(1, 2)
    print("After deletion:")
    matrix.display()

    print("\nSTACK")
    stack = Stack()
    stack.push(100)
    stack.push(200)
    stack.push(300)
    print("Stack:", stack.display())
    print("Pop:", stack.pop())
    print("After pop:", stack.display())

    print("\nQUEUE")
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print("Queue:", queue.display())
    print("Dequeue:", queue.dequeue())
    print("After dequeue:", queue.display())

    print("\nSINGLY LINKED LIST")
    linked_list = SinglyLinkedList()
    linked_list.insert_at_end(11)
    linked_list.insert_at_end(22)
    linked_list.insert_at_beginning(5)
    print("Linked List:", linked_list.traverse())
    linked_list.delete_value(22)
    print("After deletion:", linked_list.traverse())


if __name__ == "__main__":
    main()