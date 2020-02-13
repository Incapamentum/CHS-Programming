from node import Node

# One of the main required functions of the assignment.
# Will insert at the "defined tail" of the Ouroboros
# data structure and link up the tail to the head,
# completing Ouroboros once more
def insert_and_link(head, data):

    tail = head

    while (tail.next is not head):
        tail = tail.next

    tail.next = Node(data, head)

# Will remove the "defined tail" of the Ourboros data
# structure, print out the contents of it before it is
# unlinked. Once unlinked, the new "defined tail" will
# then be relinked to the "defined head" of the struct
def remove_and_link(head):

    if (head.next is None):
        return "This is the final node. Will not remove."

    tail = head

    while (tail.next.next is not head):
        tail = tail.next

    returnVal = tail.next.data
    tail.next = head
    return returnVal

# The other one of the main required functions of the
# assignment. Given the "defined head" of the Ouroboros
# data structure, will count out the nodes that comprises
# it.
def count_nodes(head):

    if (head is None):
        return 0
    else:
        count = 1

    tail = head

    while (tail.next is not head):
        count += 1
        tail = tail.next

    return count