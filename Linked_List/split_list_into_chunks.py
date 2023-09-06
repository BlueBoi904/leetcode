class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        res = []
        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next

        multiple = count // k
        rem = count % k

        for i in range(k):
            # if not head: res.append(None)
            dummy = ListNode(-1, head)
            cur = dummy
            if i < rem:
                loop = multiple + 1
            else:
                loop = multiple
            for j in range(loop):
                cur = cur.next
            head = cur.next
            cur.next = None
            res.append(dummy.next)

        return res
