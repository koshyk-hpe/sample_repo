"""
This file holds basic Linked List operations
"""


class Node:
    """
    Class for defining a Node

    """
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    """
    Class for defining Linked List
    """
    def __init__(self):
        self.head = None

    def push(self, value):
        """
        Pushes the value as the new head
        :param value: value to be pushed
        :return: None
        """
        if self.head is None:
            self.head = Node(value)
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
        print(value, "has been pushed as the new head")
        self.traverse()

    def append(self, value):
        """
        Appends a value to the tail of the Linked List

        :param value: value to be appended
        :return: None
        """
        if self.head is None:
            self.head = Node(value)
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = Node(value)
        print(value, "has been appended to the Linked List")
        self.traverse()

    def traverse(self):
        """
        Traverses the Linked List

        :return: None
        """
        if self.head is None:
            print("Empty Linked List")
        else:
            node = self.head
            print("Traversing the Linked List")
            while node is not None:
                print(node.data, "->", end=" ")
                node = node.next
            print()

    def collect_values(self):
        """
        Collects the values of Linked List as a list

        :return: Collects the values of Linked List as a list
        """
        node_values = []
        if self.head is None:
            print("Empty Linked List")
        else:
            node = self.head
            while node is not None:
                node_values.append(node.data)
                node = node.next
        return node_values

    def insert_after(self, node, value):
        """
        Inserts the value after the specific node in the Linked List

        :param node: node after which the value is to be inserted
        :param value: value to be inserted
        :return: None
        """
        if self.head is None:
            print("Empty Linked List")
        else:
            current_node = self.head
            while current_node is not None:
                if current_node == node:
                    new_node = Node(value)
                    new_node.next = current_node.next
                    current_node.next = new_node
                    print(value, "has been inserted after the node with data", current_node.data)
                    self.traverse()
                    break
                current_node = current_node.next

    def insert_at(self, position, value):
        """
        Inserts the value at the specified position of the Linked List

        :param position: position where the value is to be inserted
        :param value: value to be inserted
        :return: None
        """
        if self.head is None and position != 0:
            print("Empty Linked List")
        elif position == 0:
            self.push(value)
        else:
            current_position = 0
            node = self.head
            prev_node = self.head
            while node is not None:
                if current_position == position:
                    new_node = Node(value)
                    new_node.next = node
                    prev_node.next = new_node
                    print(value, "has been inserted at position", position)
                    self.traverse()
                    break
                prev_node = node
                node = node.next
                current_position = current_position + 1

    def update_node(self, node, value):
        """
        Updates a node with the value

        :param node: node to be updated
        :param value: new value of the node
        :return: None
        """
        current = self.head
        while current is not None:
            if current == node:
                current.data = value
                print("Node has been updated with value", value)
                self.traverse()
                break
            current = current.next

    def update_position(self, position, value):
        """
        Updates the value at the specific position of the Linked List

        :param position: position of the node
        :param value: new value of the node
        :return: None
        """
        current = 0
        node = self.head
        while node is not None:
            if current == position:
                node.data = value
                print("Node has been updated with value", value)
                self.traverse()
                break
            node = node.next
            current = current + 1

    def update_value(self, old_value, new_value):
        """
        Updates the node with the new value

        :param old_value: old value of the node
        :param new_value: new value to be updated
        :return: None
        """
        current = self.head
        while current is not None:
            if current.data == old_value:
                current.data = new_value
                print("Node has been updated with value", new_value)
                self.traverse()
                break
            current = current.next

    def delete_node(self, node):
        """
        Deletes a node based on pointer

        :param node: pointer of the node
        :return: None
        """
        if node == self.head:
            self.head = self.head.next
        else:
            current = self.head
            while current.next is not None:
                if current.next == node:
                    current.next = current.next.next
                    break
                current = current.next
        print("Node has been deleted")
        self.traverse()

    def delete_position(self, position):
        """
        Deletes the node based on position

        :param position: position of the node
        :return: None
        """
        if position == 0:
            self.head = self.head.next
        else:
            current = 0
            node = self.head
            while node.next is not None:
                if current + 1 == position:
                    node.next = node.next.next
                    break
                node = node.next
                current = current + 1
        print("Node has been deleted")
        self.traverse()

    def delete_value(self, value):
        """
        Deletes the node based on value

        :param value: value of the node
        :return: None
        """
        if self.head.data == value:
            self.head = self.head.next
        else:
            current = self.head
            while current.next is not None:
                if current.next.data == value:
                    current.next = current.next.next
                    break
                current = current.next
        print("Node has been deleted")
        self.traverse()

    def traverse_loop(self):
        """
        Traverses a Linked List with loop

        :return: None
        """
        if self.head is None:
            print("Empty Linked List")
        else:
            print("Traversing a Linked List with loop")
            node = self.head
            current_nodes = []
            while node is not None:
                print(node.data, "->", end=" ")
                if node in current_nodes:
                    break
                current_nodes.append(node)
                node = node.next
            print()

    def detect_loop_stack(self):
        """
        Detects for presence of loop in a Linked List using stack

        :return: None
        """
        if self.head is None:
            print("Empty Linked List")
        else:
            current = self.head
            prev = self.head
            current_nodes = []
            while current is not None:
                if current in current_nodes:
                    print("Loop detected")
                    self.traverse_loop()
                    prev.next = None
                    print("Loop fixed")
                    self.traverse()
                    break
                current_nodes.append(current)
                prev = current
                current = current.next

    def detect_loop_floyd(self):
        """
        Detects the presence of loop in a Linked List using Floyd's algorithm

        :return: None
        """
        if self.head is None:
            print("Empty Linked List")
        else:
            slow = self.head
            fast = self.head
            while slow is not None and fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    print("Loop detected")
                    self.traverse_loop()
                    slow.next.next.next = None
                    print("Loop fixed")
                    self.traverse()
                    break

    def delete_linked_list(self):
        """
        Deletes the complete Linked List

        :return: None
        """
        print("Deleting the Linked List")
        self.head = None
        self.traverse()
