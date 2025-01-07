class LinkedList:
    class Node:
        def init(self, data):
            self.data = data
            self.next = None

    def init(self):
        self.head = None

    def display(self):
        current_node = self.head
        output = ""
        while current_node:
            output += str(current_node.data) + " -> "
            current_node = current_node.next
        output += "None"
        print(output)

    def insert_at_index(self, data, index):
        if index < 0:
            print("Error: Invalid index.")
            return
        new_node = self.Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current_node = self.head
        for _ in range(index - 1):
            if current_node is None:
                print("Error: Index does not exist.")
                return
            current_node = current_node.next

        if current_node is None:
            print("Error: Index does not exist.")
            return
        new_node.next = current_node.next
        current_node.next = new_node

    def insert_at_end(self, data):
        new_node = self.Node(data)
        if not self.head:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def insert_at_first(self, data):
        new_node = self.Node(data)
        new_node.next = self.head
        self.head = new_node

    def update_node(self, data, index):
        if not self.head:
            print("Error: List is empty.")
            return
        if index < 0:
            print("Error: Invalid index.")
            return
        current_node = self.head
        for _ in range(index):
            if not current_node:
                print("Error: Index does not exist.")
                return
            current_node = current_node.next
        if not current_node:
            print("Error: Index does not exist.")
            return
        current_node.data = data

    def remove_node_at_index(self, index):
        if not self.head:
            print("Error: List is empty.")
            return None

        if index < 0:
            print("Error: Invalid index.")
            return None

        if index == 0:
            removed_data = self.head.data
            self.head = self.head.next
            return removed_data

        current_node = self.head
        for _ in range(index - 1):
            if current_node is None or current_node.next is None:
                print("Error: Index does not exist.")
                return None
            current_node = current_node.next
        if current_node is None or current_node.next is None:
            print("Error: Index does not exist.")
            return None

        removed_data = current_node.next.data
        current_node.next = current_node.next.next
        return removed_data

    def remove_node_at_begin(self):
        if not self.head:
            print("Error: List is empty.")
            return None
        removed_data = self.head.data
        self.head = self.head.next
        return removed_data

    def remove_node_at_end(self):
        if not self.head:
            print("Error: List is empty.")
            return None

        if not self.head.next:
            removed_data = self.head.data
            self.head = None
            return removed_data

        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next

        removed_data = current_node.next.data
        current_node.next = None
        return removed_data

    def size(self):
        count = 0
        current_node = self.head
        while current_node:
            current_node = current_node.next
            count += 1
        return count

    def concatenate(self, new_list):
        if not new_list.head:
            print("Error: New list is empty.")
            return
            if not self.head:
            self.head = new_list.head
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_list.head
        new_list.head = None

    def invert(self):
        previous_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node