# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur:
            nex = cur.next
            cur.next, pre, cur = pre, cur, nex

        return pre


head = ListNode(1)
c = head
for i in range(2, 6):
    temp = ListNode(i)
    c.next = temp
    c = c.next

s2 = Solution().reverseList(head)
print(s2)
