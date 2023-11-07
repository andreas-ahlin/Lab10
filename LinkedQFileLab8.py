class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedQ:

    def __init__(self):
        self.__first = None
        self.__last = None

    def enqueue(self, data):
        new = Node(data)
        if self.isEmpty():
            self.__first = new
            self.__last = new
        else:
            self.__last.next = new
            self.__last = new
            self.__last.next = None

    def peek(self):
        if self.isEmpty:
            return self.__first.data

    def dequeue(self):
        if self.isEmpty():
            print('Kön är tom')
            return self.__first
        else:
            data = self.__first.data
            self.__first = self.__first.next
            if self.__first == None:
                self.__last = None
            return data

    def isEmpty(self):
        if self.__first == None and self.__last == None:
            return True
        else:
            return False

    def size(self):
        i = 0
        pointer = None
        if self.isEmpty():
            return i
        else:
            while True:
                i = i + 1
                pointer = self.__first
                if pointer.next == None:
                    break
                else:
                    pointer = pointer.next
            return i
