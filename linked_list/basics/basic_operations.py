"""
This file holds basic operations using Linked List such as,
0) __len__
1) push
2) append
3) traverse
4) collect_values
5) insert_at
6) insert_after
7) update_position
8) update_node
9) update_value
10) update_all
11) delete_node
12) delete_position
13) delete_value
14) delete_all
15) delete_linked_list
16) detect_loop_using_stack
17) detect_loop_using_floyd
18) traverse_loop
19) fix_loop_using_floyd
20) reverse
"""


class Node:
    """
    Class for defining a node of the Linked List

    """

    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    """
    Class for defining a Linked List

    """

    def __init__(self):
        self.head = None

    def __len__(self):
        count = 0
        node = self.head
        while node is not None:
            count = count + 1
            node = node.next
        return count

    def append(self, value):
        """
        Appends value to the last node of Linked List

        :param value: value to be appended to the Linked List
        :return: None
        """
        # Checks for empty Linked List
        if self.head is None:
            self.head = Node(value)
            print(value, " is the head of the Linked List")

        # Appending the value as the last node of the Linked List
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = Node(value)
            print("Value ", value, " has been appended to the Linked List")
        self.traverse()

    def push(self, value):
        """
        Pushes value as the new head of the Linked List

        :param value: value to be pushed to the Linked List
        :return: None
        """
        # Checks for empty Linked List
        if self.head is None:
            self.head = Node(value)
            print(value, " is the head of the Linked List")

        # Setting the current head as the second node of the Linked List
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            print("Value ", value, " is the new head to the Linked List")
        self.traverse()

    def traverse(self):
        """
        Traverses the Linked List

        :return: None
        """
        # Checks for empty Linked List
        if self.head is None:
            print("Empty Linked List")

        # Traverses the non-empty Linked List
        else:
            node = self.head
            print("Traversing the Linked List")
            while node is not None:
                print(node.data, "->", end=" ")
                node = node.next
            print()

    def collect_values(self):
        """
        Collects the values of the Linked List

        :return: node values as list
        """
        print("Collecting values from the Linked List")
        node_values = []
        node = self.head
        while node is not None:
            node_values.append(node.data)
            node = node.next
        return node_values

    def insert_at(self, position, value):
        """
        Inserts value at a specific position of the Linked List

        :param position: position of the node
        :param value: value to be inserted to the Linked List
        :return: None
        """
        # Checks for empty Linked List and position 0
        if self.head is None and position == 0:
            self.head = Node(value)

        # Checks for non-empty Linked List and position 0
        elif self.head is not None and position == 0:
            self.push(value)

        # Checks for non-empty Linke List and position non-zero
        else:
            current_position = 0
            curr_node = self.head
            prev_node = self.head
            while curr_node is not None:
                if current_position == position:
                    node = Node(value)
                    node.next = curr_node
                    prev_node.next = node
                    print(value, " has been inserted at ", position, " of the Linked List")
                    break
                current_position = current_position + 1
                prev_node = curr_node
                curr_node = curr_node.next
        self.traverse()

    def insert_after(self, node, value):
        """
        Inserts value after the specified node in the Linked List

        :param node: node after which the value has to be inserted
        :param value: value to be inserted in the Linked List
        :return: None
        """
        current_node = self.head
        while current_node is not None:
            if current_node == node:
                new_node = Node(value)
                new_node.next = current_node.next
                current_node.next = new_node
                print(value, " has been inserted after the node with value ", current_node.data)
                self.traverse()
                break
            current_node = current_node.next

    def update_position(self, position, value):
        """
        Updates the position with the new value in the Linked List

        :param position: position of the node in the Linked List
        :param value: value to be updated in the position
        :return: None
        """
        # Checks for empty Linked List
        if self.head is None:
            print("Empty Linked List")

        # Updates the position with the new value
        else:
            node = self.head
            current_position = 0
            while node is not None:
                if current_position == position:
                    node.data = value
                    print("Node ", position, " has been updated with value ", value)
                    self.traverse()
                    break
                current_position = current_position + 1
                node = node.next

    def update_node(self, node, value):
        """
        Updates the node with the new value

        :param node: node whose value is to be updated
        :param value: new value to be updated
        :return: None
        """
        # Checks for empty Linked List
        if self.head is None:
            print("Empty Linked List")

        # Updates the node with the new value
        else:
            current = self.head
            while current is not None:
                if current == node:
                    current.data = value
                    print("Node has been updated with value ", value)
                    self.traverse()
                    break
                current = current.next

    def update_value(self, old_value, new_value):
        """
        Updates the first occurrence of node with the old value with the new value

        :param old_value: old value of the node
        :param new_value: new value of the node
        :return: None
        """
        # Checks for empty Linked List
        if self.head is None:
            print("Empty Linked List")

        # Updates the node with the old value with the new value
        else:
            node = self.head
            while node is not None:
                if node.data == old_value:
                    node.data = new_value
                    print("Node with value ", old_value, " has been updated to ", new_value)
                    self.traverse()
                    break
                node = node.next

    def update_all(self, old_value, new_value):
        """
        Updates all the occurrences of the old value in the Linked List with the new value

        :param old_value: old value of the nodes
        :param new_value: new value to be updated
        :return: None
        """
        # Checks for empty Linked List
        if self.head is None:
            print("Empty Linked List")

        # Updates all the occurrences of the old value with the new value
        else:
            node = self.head
            while node is not None:
                if node.data == old_value:
                    node.data = new_value
                node = node.next
            print("All the occurrences of ", old_value, " has been updated with ", new_value)
            self.traverse()

    def delete_node(self, node):
        """
        Deletes the node of the Linked List

        :param node: node to be deleted from the Linked List
        :return: None
        """
        # Checks for empty Linked List
        if self.head is None:
            print("Empty Linked List")

        # Checks if the node is the head node
        elif node == self.head:
            self.head = self.head.next
            print("Head node has been deleted")
            self.traverse()

        # Deletes the node
        else:
            current = self.head
            prev = self.head
            while current is not None:
                if current == node:
                    prev.next = current.next
                    print("Node with value ", node.data, " has been deleted")
                    self.traverse()
                    break
                prev = current
                current = current.next

    def delete_position(self, position):
        """
        Deletes the specified position of the Linked List

        :param position: node position to be deleted
        :return: None
        """
        # Checks for empty Linked List
        if self.head is None:
            print("Empty Linked List")

        # Checks if the node to be deleted is head
        elif position == 0:
            self.head = self.head.next
            print("Head node has been deleted")
            self.traverse()

        # Deletes the node
        else:
            current_position = 0
            current_node = self.head
            prev_node = self.head
            while current_node is not None:
                if current_position == position:
                    prev_node.next = current_node.next
                    print("Node with value ", current_node.data, " has been deleted")
                    self.traverse()
                    break
                current_position = current_position + 1
                prev_node = current_node
                current_node = current_node.next

    def delete_value(self, value):
        """
        Deletes the first occurrence of the value in the Linked List

        :param value: value to be deleted
        :return: None
        """
        # Checks for empty Linked List
        if self.head is None:
            print("Empty Linked List")

        # Checks for the head value
        elif self.head.data == value:
            self.head = self.head.next
            print("Head node has been deleted")
            self.traverse()

        # Deletes value in the Linked List
        else:
            current_node = self.head
            prev_node = self.head
            while current_node is not None:
                if current_node.data == value:
                    prev_node.next = current_node.next
                    print("Node with value ", current_node.data, " has been deleted")
                    self.traverse()
                    break
                prev_node = current_node
                current_node = current_node.next

    def delete_all(self, value):
        """
        Deletes all the occurrences of a value in the Linked List

        :param value: value ot be deleted
        :return: None
        """
        # Checks for empty Linked List
        if self.head is None:
            print("Empty Linked List")

        # Deletes all the occurrences of the values
        else:
            if self.head.data == value:
                self.head = self.head.next
            current_node = self.head
            prev_node = self.head
            while current_node is not None:
                if current_node.data == value:
                    prev_node.next = current_node.next
                prev_node = current_node
                current_node = current_node.next
            self.traverse()

    def delete_linked_list(self):
        """
        Deletes the Linked List

        :return: None
        """
        self.head = None
        print("Deleted the Linked List")
        self.traverse()

    def detect_loop_using_stack(self):
        """
        Detects loop in the Linked List

        :return: boolean
        """
        # Checks for empty Linked List
        if self.head is None:
            print("Empty Linked List")
        else:
            nodes = []
            node = self.head
            print("Detecting presence of Loop in the Linked List")
            while node is not None:
                if node in nodes:
                    print("Loop detected in the Linked List")
                    self.traverse_loop()
                    return True
                nodes.append(node)
                node = node.next
        return False

    def detect_loop_using_floyd(self):
        """
        Detects presence of Loop in the Linked List using Floyd's algorithm

        :return: boolean
        """
        # Checks for empty Linked List
        if self.head is None:
            print("Empty Linked List")
        else:
            slow = self.head
            fast = self.head
            print("Detecting presence of loop in the Linked List")
            while slow is not None and fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    print("Loop Detected in the Linked List")
                    self.traverse_loop()
                    return True
        return False

    def traverse_loop(self):
        """
        Traverses a Linked List with loop

        :return: None
        """
        # Checks for empty Linked List
        if self.head is None:
            print("Empty Linked List")
        else:
            available_nodes = []
            node = self.head
            print("Traversing the Linked List with loop")
            while node is not None:
                print(node.data, "->", end=" ")
                if node in available_nodes:
                    break
                available_nodes.append(node)
                node = node.next
            print()

    def fix_loop_using_floyd(self):
        """
        Removes loop from the Linked List

        :return: None
        """
        # Checks for empty Linked List
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
                    slow.next.next = None
                    print("Loop fixed")
                    self.traverse()

    def reverse(self):
        """
        Reverses the Linked List

        :return: None
        """
        # Checks for an empty Linked List
        if self.head is None:
            print("Empty Linked List")
        # Reverses the Linked List
        else:
            current_node = self.head
            prev_node = None
            print("Reversing the Linked List")
            while current_node is not None:
                next_node = current_node.next
                current_node.next = prev_node
                prev_node = current_node
                current_node = next_node
            self.head = prev_node
            self.traverse()

