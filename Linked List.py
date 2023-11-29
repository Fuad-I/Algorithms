class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        return self.data


class SLinkedList:
    def __init__(self, nodes=None):
        self.head = None
        self.tail = None
        if nodes is not None:
            self.count = len(nodes)
            if len(nodes) == 1:
                node = Node(nodes.pop(0))
                self.head = node
            elif len(nodes) == 2:
                node = Node(nodes.pop(0))
                self.head = node
                tail = Node(nodes.pop(0))
                self.tail = tail
            else:
                node = Node(nodes.pop(0))
                self.head = node
                for elem in nodes[:len(nodes) - 1]:
                    node.next = Node(elem)
                    node = node.next
                tail = Node(nodes[len(nodes) - 1])
                node.next = tail
                self.tail = tail

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.data)
        nodes.append("None")
        return " -> ".join(nodes)

    def __getitem__(self, index):
        if index > self.count - 1:
            raise Exception("Out of bounds")

        i = 0
        for node in self:
            if i == index:
                return node.data
            i += 1

    def add_first(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        self.count += 1

    def add_last(self, new_data):
        new_node = Node(new_data)
        if not self.head:
            self.head = new_node
            self.count += 1
            return

        self.tail.next = new_node
        self.tail = new_node
        self.count += 1

    def add_after(self, target_node_data, new_data):
        if not self.head:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                new_node = Node(new_data)
                new_node.next = node.next
                node.next = new_node
                self.count += 1
                return

        raise Exception("Node with data '%s' not found" % target_node_data)

    def add_before(self, target_node_data, new_data):
        if not self.head:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            new_node = Node(new_data)
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                new_node = Node(new_data)
                prev_node.next = new_node
                new_node.next = node
                self.count += 1
                return
            prev_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

    def remove(self, target_node_data):
        if not self.head:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            self.count -= 1
            return

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = node.next
                self.count -= 1
                return
            prev_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

    def reverse(self):
        if not self.head:
            raise Exception("Empty list")
        if self.head.next is None:
            return

        previous_node = None
        current_node = self.head
        self.tail = self.head
        while current_node is not None:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node


class DLinkedList:
    def __init__(self, nodes=None):
        self.head = None
        self.tail = None

        if nodes is not None:
            self.count = len(nodes)
            if len(nodes) == 1:
                node = Node(nodes.pop(0))
                self.head = node
            elif len(nodes) == 2:
                node = Node(nodes.pop(0))
                self.head = node
                tail = Node(nodes.pop(0))
                tail.previous = self.head
                self.tail = tail
            else:
                node = Node(nodes.pop(0))
                self.head = node
                for elem in nodes[:len(nodes) - 1]:
                    node.next = Node(elem)
                    node.next.previous = node
                    node = node.next

                tail = Node(nodes[len(nodes) - 1])
                node.next = tail
                tail.previous = node
                self.tail = tail

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.data)
        nodes.append("None")
        return " <-> ".join(nodes)

    def __getitem__(self, index):
        if index > self.count - 1:
            raise Exception("Out of bounds")

        i = 0
        for node in self:
            if i == index:
                return node.data
            i += 1

    def add_first(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head.previous = new_node

        self.head = new_node
        self.count += 1

    def add_last(self, new_data):
        new_node = Node(new_data)
        if not self.head:
            self.head = new_node
            self.count += 1
            return

        new_node.previous = self.tail
        self.tail.next = new_node
        self.tail = new_node
        self.count += 1

    def add_after(self, target_node_data, new_data):
        if not self.head:
            raise Exception("List is empty")

        if self.tail.data == target_node_data:
            self.add_last(new_data)
            return

        for node in self:
            if node.data == target_node_data:
                new_node = Node(new_data)
                new_node.next = node.next
                node.next = new_node
                new_node.previous = node
                self.count += 1
                return

        raise Exception("Node with data '%s' not found" % target_node_data)

    def add_before(self, target_node_data, new_data):
        if not self.head:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            new_node = Node(new_data)
            return self.add_first(new_node)

        for node in self:
            if node.data == target_node_data:
                self.add_after(node.previous.data, new_data)
                return

        raise Exception("Node with data '%s' not found" % target_node_data)

    def remove(self, target_node_data):
        if not self.head:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            self.head.previous = None
            self.count -= 1
            return

        for node in self:
            if node.data == target_node_data:
                node.previous.next = node.next
                node.next.previous = node.previous
                self.count -= 1
                return

        raise Exception("Node with data '%s' not found" % target_node_data)


class CLinkedList:
    def __init__(self, nodes=None):
        self.head = None
        self.tail = None
        if nodes is not None:
            self.count = len(nodes)
            if len(nodes) == 1:
                node = Node(nodes.pop(0))
                self.head = node
            elif len(nodes) == 2:
                node = Node(nodes.pop(0))
                self.head = node
                tail = Node(nodes.pop(0))
                self.tail = tail
            else:
                node = Node(nodes.pop(0))
                self.head = node
                for elem in nodes[:len(nodes) - 1]:
                    node.next = Node(elem)
                    node = node.next
                tail = Node(nodes[len(nodes) - 1])
                node.next = tail
                tail.next = self.head
                self.tail = tail

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.data)
        nodes.append(self.head.data)
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
            if node == self.head:
                break

    def __getitem__(self, index):
        if index > self.count - 1:
            raise Exception("Out of bounds")

        i = 0
        for node in self:
            if i == index:
                return node.data
            i += 1

    def add_first(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        self.count += 1

    def add_last(self, new_data):
        new_node = Node(new_data)
        if not self.head:
            self.head = new_node
            self.count += 1
            return

        self.tail.next = new_node
        self.tail = new_node
        self.count += 1

    def add_after(self, target_node_data, new_data):
        if not self.head:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                new_node = Node(new_data)
                new_node.next = node.next
                node.next = new_node
                self.count += 1
                return

        raise Exception("Node with data '%s' not found" % target_node_data)

    def add_before(self, target_node_data, new_data):
        if not self.head:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            new_node = Node(new_data)
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                new_node = Node(new_data)
                prev_node.next = new_node
                new_node.next = node
                self.count += 1
                return
            prev_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

    def remove(self, target_node_data):
        if not self.head:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            self.count -= 1
            return

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = node.next
                self.count -= 1
                return
            prev_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

    def reverse(self):
        if not self.head:
            raise Exception("Empty list")
        if self.head.next is None:
            return

        previous_node = None
        current_node = self.head
        self.tail = self.head
        while current_node is not None:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node


list1 = SLinkedList(['Mon', 'Tue', 'Wed', 'Thu'])
print(list1)
list2 = DLinkedList(['Jan', 'Feb', 'Mar', 'Apr', 'May'])
print(list2)
list3 = CLinkedList([x for x in '1234567'])
print(list3)
