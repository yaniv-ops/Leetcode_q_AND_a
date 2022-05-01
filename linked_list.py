class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
        self.length += 1

    def print(self):
        if self.head == None:
            print('List is empty')
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += f"{str(itr.data)} --> "
            itr= itr.next
        print(llstr)
        print(self.length)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
            print(itr.next)
        itr.next = Node(data, None)
        self.length +=1

    def insert_values(self,data_set):
        self.head = None
        for item in data_set:
            self.insert_at_end(item)

    def remove_index(self, index):
        if index < 0 or index >= self.length:
            raise Exception('Invalid index')

        if index == 0:
            self.head = self.head.next
            self.length -=1
            return

        count = 0

        itr = self.head
        while itr:
            if count == index -1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_at_index(self, index, data):
        if index<0 or index>self.length:
            raise Exception('Invalid Index')
        if index==0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data , itr.next)
                return
            itr = itr.next

    def remove_by_value(self, data):
        if self.head is None:
            raise Exception('Empty list')
        itr = self.head
        count = 0
        while itr:
            if itr.data == data:
                break
            count += 1
            itr = itr.next
        self.remove_index(count)
