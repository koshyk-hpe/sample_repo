"""
This file holds functions to detect intersection between two Linked Lists
"""


def detect_intersection_stack(link01, link02):
    """
    Detects intersection using a stack

    :param link01: first Linked List
    :param link02: second Linked List
    :return: None
    """
    current_nodes = []
    current_node_01 = link01.head
    while current_node_01 is not None:
        current_nodes.append(current_node_01)
        current_node_01 = current_node_01.next

    current_node_02 = link02.head
    while current_node_02 is not None:
        if current_node_02 in current_nodes:
            print("Intersection detected at node with data", current_node_02.data)
            link01.traverse()
            link02.traverse()
            break
        current_node_02 = current_node_02.next


def detect_intersection(link01, link02):
    """
    Detects intersection between two Linked Lists

    :param link01: first Linked List
    :param link02: second Linked List
    :return: None
    """
    if link01.head is None or link02.head is None:
        print("Empty Linked List")
        link01.traverse()
        link02.traverse()
    else:
        current_01 = link01.head
        while current_01 is not None:
            current_02 = link02.head
            while current_02 is not None:
                if current_01 == current_02:
                    print("Intersection detected at node with data", current_02.data)
                    link01.traverse()
                    link02.traverse()
                    return
                current_02 = current_02.next
            current_01 = current_01.next
        print("No intersection detected between the two Linked Lists")
