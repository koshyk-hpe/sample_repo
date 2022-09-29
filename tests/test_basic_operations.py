"""
This file contains test cases to validate basic_operations.py
"""

import logging


def test_linked_list_append(link_list):
    """
    Checks if elements are appended to linked list

    :param: link_list: fixture for Linked List
    :return: None
    """
    logging.info("Testing if elements are appended to Linked List")
    node_data = [2, 3, 4, 5, 6, 7]
    for node_value in node_data:
        link_list.append(node_value)

    assert link_list.head.data == 2, "Head value assigned incorrectly"
    assert node_data == link_list.collect_values(), "Error in appending values to linked list"
