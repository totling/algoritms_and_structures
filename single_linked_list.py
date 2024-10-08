class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__length = 0

    def push_back(self, data):
        new_node = Node(data)
        if not self.__head:
            self.__head = new_node
            self.__tail = new_node
            self.__length += 1
            return

        self.__tail.next = new_node
        self.__tail = self.__tail.next
        self.__length += 1

    def push_front(self, data):
        new_node = Node(data)
        if not self.__head:
            self.__head = new_node
            self.__tail = new_node
            self.__length += 1
            return

        new_node.next = self.__head
        self.__head = new_node
        self.__length += 1

    def pop_front(self):
        node = self.__head
        self.__head = self.__head.next

        self.__length -= 1
        data = node.data
        del node
        return data

    def pop_end(self):
        current_node = self.__head
        while current_node.next.next:
            current_node = current_node.next
        node = self.__tail
        current_node.next = None

        self.__length -= 1
        data = node.data
        del node
        return data

    def insert(self, index, data):
        if index == 0:
            self.push_front(data)
            self.__length += 1
        elif index < self.__length:
            new_node = Node(data)
            iter_ = 0
            current_node = self.__head
            while iter_ < index - 1:
                current_node = current_node.next
                iter_ += 1

            left = current_node
            right = current_node.next
            left.next = new_node
            left.next.next = right
            self.__length += 1
        elif index >= self.__length:
            raise IndexError("Index out of range")
        else:
            self.push_back(data)
            self.__length += 1

    def erase(self, index):
        if index == 0:
            self.pop_front()
        elif index == self.__length - 1:
            self.pop_end()
        elif index < self.__length - 1:
            iter_ = 0
            current_node = self.__head

            while iter_ < index-1:
                current_node = current_node.next
                iter_ += 1

            left = current_node
            node = current_node.next
            right = current_node.next.next

            left.next = right
            self.__length -= 1
            data = node.data
            del node
            return data
        else:
            raise IndexError("There is no element with such an index")

    def __getitem__(self, index):
        iter_ = 0
        current_node = self.__head
        while iter_ < index:
            try:
                current_node = current_node.next
                iter_ += 1
            except AttributeError:
                raise IndexError("There is no element with such an index")

        if current_node:
            return current_node.data
        else:
            raise IndexError("There is no element with such an index")

    def __setitem__(self, index, data):
        iter_ = 0
        current_node = self.__head
        while iter_ < index:
            try:
                current_node = current_node.next
                iter_ += 1
            except AttributeError:
                raise IndexError("There is no element with such an index")

        if current_node:
            current_node.data = data
        else:
            raise IndexError("There is no element with such an index")

    def __str__(self):
        current_node = self.__head
        output = ''
        while current_node:
            output += f'{current_node.data} '
            current_node = current_node.next

        return output

    def __len__(self):
        return self.__length


lst = LinkedList()
lst.push_back(6)
lst.push_back(4)
lst.push_back(2)
lst.push_front(2)
print(lst[2])
print(lst)
print(len(lst))
lst[0] = 3
print(lst)
lst.insert(1, 10)
print(lst)
lst.pop_end()
print(lst)
lst.pop_front()
print(lst)
lst.erase(2)
print(lst)
