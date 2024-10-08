
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__length = 0

    def push_front(self, data):
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

    def push_back(self, data):
        new_node = Node(data)

        if not self.__head:
            self.__head = new_node
            self.__tail = new_node
            self.__length += 1
            return

        temp_node = self.__tail
        self.__tail = new_node
        self.__tail.prev = temp_node
        temp_node.next = self.__tail
        self.__length += 1

    def pop_front(self):
        temp_node = self.__head
        self.__head.next.prev = None
        self.__head = self.__head.next

        data = temp_node.data
        self.__length -= 1
        del temp_node
        return data

    def pop_back(self):
        temp_node = self.__tail
        self.__tail.prev.next = None
        self.__tail = self.__tail.prev

        data = temp_node.data
        self.__length -= 1
        del temp_node
        return data

    def insert(self, index, data):
        if index == 0:
            self.push_front(data)
        elif index < self.__length:
            new_node = Node(data)
            self.__length += 1
            if index - self.__length // 2 < 0:
                iter_ = 0
                current_node = self.__head

                while iter_ < index:
                    current_node = current_node.next
                    iter_ += 1

                left = current_node.prev
                right = current_node

                left.next = new_node
                new_node.prev = left

                right.prev = new_node
                new_node.next = right
            elif index - self.__length // 2 >= 0 and index < self.__length:
                iter_ = self.__length - 1
                current_node = self.__tail

                while iter_ > index:
                    current_node = current_node.prev
                    iter_ -= 1

                left = current_node.prev
                right = current_node

                left.next = new_node
                new_node.prev = left

                right.prev = new_node
                new_node.next = right
        else:
            self.push_back(data)

    def erase(self, index):
        if index == 0:
            self.pop_front()
        elif index == self.__length - 1:
            self.pop_back()
        elif index < self.__length - 1:
            self.__length -= 1
            if index - self.__length // 2 < 0:
                iter_ = 0
                current_node = self.__head

                while iter_ < index:
                    current_node = current_node.next
                    iter_ += 1

                left = current_node.prev
                temp_node = current_node
                right = current_node.next

                left.next = right
                right.prev = left
                data = temp_node.data
                del temp_node
                return data
            elif index - self.__length // 2 >= 0 and index < self.__length:
                iter_ = self.__length - 1
                current_node = self.__tail

                while iter_ > index:
                    current_node = current_node.prev
                    iter_ -= 1

                left = current_node.prev
                temp_node = current_node
                right = current_node.next

                left.next = right
                right.prev = left
                data = temp_node.data
                del temp_node
                return data
        else:
            raise IndexError("Index out of range")

    def __getitem__(self, index):
        if index == 0:
            return self.__head.data
        elif index == self.__length - 1:
            return self.__tail.data
        elif self.__length - 1 > index > 0:
            if index - self.__length // 2 < 0:
                iter_ = 0
                current_node = self.__head
                while iter_ < index:
                    current_node = current_node.next
                    iter_ += 1

                return current_node.data
            elif index - self.__length // 2 >= 0 and index < self.__length:
                iter_ = self.__length - 1
                current_node = self.__tail
                while iter_ > index:
                    current_node = current_node.prev
                    iter_ -= 1

                return current_node.data
        else:
            raise IndexError("Index out of range")

    def __setitem__(self, index, data):
        if index == 0:
            self.__head.data = data
        elif index == self.__length - 1:
            self.__tail.data = data
        elif self.__length - 1 > index > 0:
            if index - self.__length // 2 < 0:
                iter_ = 0
                current_node = self.__head
                while iter_ < index:
                    current_node = current_node.next
                    iter_ += 1

                current_node.data = data
            elif index - self.__length // 2 >= 0 and index < self.__length:
                iter_ = self.__length - 1
                current_node = self.__tail
                while iter_ > index:
                    current_node = current_node.prev
                    iter_ -= 1

                current_node.data = data
        else:
            raise IndexError("Index out of range")

    def __str__(self):
        output = ''
        current_node = self.__head
        while current_node:
            output += f"{current_node.data} "
            current_node = current_node.next

        return output

    def __len__(self):
        return self.__length


lst = DoubleLinkedList()
lst.push_back(6)
lst.push_back(7)
lst.push_front(5)
print(lst)
print(len(lst))
lst.push_back(8)
lst.push_front(4)
print(lst)
print(lst[4])
lst[4] = 3
print(lst)
# lst.insert(7, 10)
# print(lst)
# lst.erase(6)
# print(lst)
