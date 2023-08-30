# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(
        l1: [ListNode], l2: [ListNode]
) -> [ListNode]:
    num_1 = []
    num_2 = []
    h1 = l1
    h2 = l2

    while h1:
        num_1.append(h1.val)
        h1 = h1.next

    while h2:
        num_2.append(h2.val)
        h2 = h2.next
    res = int("".join(map(str, num_1)))
    res2 = int("".join(map(str, num_2)))
    my_list = list(map(int, str(res + res2)))

    head = ListNode(my_list.pop(0))
    temp_head = head
    print(my_list)
    while len(my_list) > 0:
        # Inefficient pop from front of list
        temp_head.next = ListNode(my_list.pop(0))
        temp_head = temp_head.next
    return head
