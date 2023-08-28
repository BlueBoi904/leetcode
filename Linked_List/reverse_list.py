def reverse_list(head):
    prev = None
    curr = head

    while curr:
        # Create temp node to hold reference to the next node
        next_node = curr.next
        # Reverse the direction of the pointer curr.next <- prev
        curr.next = prev
        # Set prev to curr node
        prev = curr

        curr = next_node

    return prev

