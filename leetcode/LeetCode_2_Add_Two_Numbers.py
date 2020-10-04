"""
2. 两数相加
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        flag, cur1, cur2 = 0, l1, l2
        cur = dummy = ListNode(-1)
        while cur1 or cur2 or flag:
            s = flag
            if cur1:
                s += cur1.val
                cur1 = cur1.next
            if cur2:
                s += cur2.val
                cur2 = cur2.next
            flag = 0
            if s >= 10:
                flag = 1
                s -= 10
            cur.next = ListNode(s)
            cur = cur.next
        return dummy.next


class Solution2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 创建一个结点值为 None 的头结点, dummy 和 p 指向头结点, dummy 用来最后返回, p 用来遍历
        dummy = p = ListNode(-1)
        s = 0  # 初始化进位 s 为 0
        while l1 or l2 or s:
            # 如果 l1 或 l2 存在, 则取l1的值 + l2的值 + s(s初始为0, 如果下面有进位1, 下次加上)
            s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            p.next = ListNode(s % 10)  # p.next 指向新链表, 用来创建一个新的链表
            p = p.next  # p 向后遍历
            s //= 10  # 有进位情况则取模, eg. s = 18, 18 // 10 = 1
            l1 = l1.next if l1 else None  # 如果l1存在, 则向后遍历, 否则为 None
            l2 = l2.next if l2 else None  # 如果l2存在, 则向后遍历, 否则为 None
        return dummy.next  # 返回 dummy 的下一个节点, 因为 dummy 指向的是空的头结点, 下一个节点才是新建链表的后序节点


class Solution3:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        cur, p1, p2 = dummy, l1, l2
        flag = 0  # 进位
        while p1 and p2:
            tmp = p1.val + p2.val + flag
            if tmp >= 10:
                flag = 1
                tmp -= 10
            else:
                flag = 0
            cur.next = ListNode(tmp)
            cur, p1, p2 = cur.next, p1.next, p2.next
        while p1 or p2:
            tmp = p1.val + flag if p1 else p2.val + flag
            if tmp >= 10:
                flag = 1
                tmp -= 10
            else:
                flag = 0
            cur.next = ListNode(tmp)
            cur = cur.next
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
        # 若进位仍不为0
        if flag > 0:
            cur.next = ListNode(1)
        return dummy.next


if __name__ == '__main__':
    n1 = ListNode(2)
    n1.next = ListNode(4)
    n1.next.next = ListNode(3)

    n2 = ListNode(5)
    n2.next = ListNode(6)
    n2.next.next = ListNode(4)

    s = Solution()
    s.addTwoNumbers(n1, n2)
