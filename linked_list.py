class LinkedList:
    class Node:
        def __init__(self, data, node_list, prev=None, nex=None):
            self.data = data
            self._nex = nex
            self._prev = prev
            self._node_list = node_list

        def insert_after(self, data):
            new_node = LinkedList.Node(data, self._node_list, prev=self, nex=self._nex)
            if self is self._node_list.tail:
                self._node_list.tail = new_node
            else:  # self._nex is not None
                self._nex._prev = new_node
            self._nex = new_node
            self._node_list._length += 1
            return new_node

        def insert_before(self, data):
            new_node = LinkedList.Node(data, self._node_list, prev=self._prev, nex=self)
            if self is self._node_list.head:
                self._node_list.head = new_node
            else:  # self._prev is not None
                self._prev._nex = new_node
            self._prev = new_node
            self._node_list._length += 1
            return new_node

        def swap_with_prev(self):
            if self is self._node_list.head:
                raise IndexError()
            prev = self._prev
            prevprev = self._prev._prev
            nex = self._nex
            if self._prev is self._node_list.head:
                self._node_list.head = self
            else:
                # prevprev is not None
                prevprev._nex = self

            self._nex = prev
            prev._nex = nex

            if self is self._node_list.tail:
                self._node_list.tail = prev
            else:
                # nex is not None
                nex._prev = prev
            self._prev = prevprev
            prev._prev = self

            return self

        def remove(self):
            if self is self._node_list.head:
                self._node_list.head = self._nex
            else:
                self._prev._nex = self._nex

            if self is self._node_list.tail:
                self._node_list.tail = self._prev
            else:
                self._nex._prev = self._prev
            self._node_list._length -= 1
            return self

        def swap_with_next(self):
            if self is self._node_list.tail:
                raise IndexError()
            self._nex.swap_with_prev()
            return self

        def __str__(self):
            return f"({self.data})"

        def __repr__(self):
            return self.__str__()

        def __next__(self):
            return self._nex

    class Iterator:
        def __init__(self, node):
            self.node = node

        def __next__(self):
            if self.node is None:
                raise StopIteration()
            data = self.node.data
            self.node = self.node._nex
            return data

    def __iter__(self):
        return LinkedList.Iterator(self.head)

    def __init__(self, init_iter=None):
        self.head = None
        self.tail = None
        self._length = 0
        if init_iter is not None:
            for d in init_iter:
                self.add_back(d)

    def get_i(self, idx):
        if idx < 0:
            return self.get_i_node(idx + len(self)).data

        n = self.head
        for i in range(idx):
            n = n._nex
        return n.data

    def __getitem__(self, i):
        return self.get_i(i)

    def get_i_node(self, idx):
        if idx < 0:
            return self.get_i_node(idx + len(self))

        n = self.head
        for i in range(idx):
            n = n._nex
        return n

    def remove(self, i):
        n = self.get_i_node(i)
        data = n.data
        n.remove()
        return data

    def pop_front(self):
        if self._length == 0:
            raise IndexError()
        return self.head.remove()

    def pop_back(self):
        if self._length == 0:
            raise IndexError()
        return self.tail.remove()

    def insert(self, i, data):
        n = self.get_i_node(i)
        new_node = n.insert_before(data)
        return new_node

    def add_front(self, data):
        if self._length == 0:
            return self._add_first(data)
        else:
            new_node = self.head.insert_before(data)

    def add_back(self, data):
        if self._length == 0:
            return self._add_first(data)
        else:
            return self.tail.insert_after(data)

    def _add_first(self, data):
        n = LinkedList.Node(data, self, None, None)
        self.head = n
        self.tail = n
        self._length = 1
        return n

    def __len__(self):
        return self._length

    def __str__(self):
        s_list = []
        n = self.head
        while n is not self.tail:
            s_list.append(str(n))
            n = n._nex
        s_list.append(str(n))
        return "<" + "=".join(s_list) + ">"

    def __repr__(self):
        return self.__str__()


def sort_linked_list(linked_list, key=None):
    if len(linked_list) < 2:
        return linked_list

    if key is None:
        key = lambda x: x

    swapped = True
    while swapped:
        swapped = False
        n = linked_list.head
        while n is not linked_list.tail:
            if key(n.data) > key(n._nex.data):
                swapped = True
                n.swap_with_next()
            else:
                n = next(n)

    return linked_list


def insert_ordered(linked_list, data, key=None):
    if key is None:
        key = lambda x: x

    n = linked_list.head
    while n is not None and key(n.data) < key(data):
        n = next(n)
    if n is None:
        linked_list.add_back(data)
    else:
        n.insert_before(data)

    return linked_list
