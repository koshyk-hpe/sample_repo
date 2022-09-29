"""
This file holds fixtures and methods for test cases

"""

import pytest
from linked_list.basics import LinkedList


@pytest.fixture(scope='module')
def link_list():
    """
    Fixture for creating LinkedList instance

    :return: Vertica DB connection instance
    """
    llist = LinkedList()
    return llist
