# "Basic" class definition for a Node as part of a 
# linked list data structure
class Node(object):
    """Represents a linked node"""

    def __init__(self, data, next = None):
        """Instantiates a Node with a default next of None."""
        self.data = data
        self.next = next