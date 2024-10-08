class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Queue:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__length = 0

    def push(self, data):
        new_node = Node(data)

        if not self.__head:
            self.__head = new_node
            self.__tail = new_node
            self.__length += 1
            return

        new_node.next = self.__head
        self.__head.prev = new_node
        self.__head = new_node
        self.__length += 1

    def pop(self):
        temp_node = self.__tail

        temp_node.prev.next = None
        self.__tail = self.__tail.prev

        data = temp_node.data
        del temp_node
        return data

    def peek(self):
        return self.__tail.data

    def __str__(self):
        output = ''
        current_node = self.__head

        while current_node:
            output += f'{current_node.data} '
            current_node = current_node.next

        return output

    def __len__(self):
        return self.__length


class Stack:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__length = 0

    def push(self, data):
        new_node = Node(data)

        if not self.__head:
            self.__head = new_node
            self.__tail = new_node
            self.__length += 1
            return

        new_node.next = self.__head
        self.__head.prev = new_node
        self.__head = new_node

    def pop(self):
        temp_node = self.__head

        self.__head.next.prev = None
        self.__head = self.__head.next

        data = temp_node.data
        del temp_node
        return data

    def peek(self):
        return self.__head.data

    def __str__(self):
        output = ''
        current_node = self.__head

        while current_node:
            output += f'{current_node.data} '
            current_node = current_node.next

        return output

    def __len__(self):
        return self.__length


stack = Stack()
stack.push(0)
stack.push(1)
stack.push(2)
print(stack)
print(stack.peek())
print(stack.pop())
print(stack)

