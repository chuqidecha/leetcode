# [leetcode019] Remove Nth Node From End of List 解题报告

Given a linked list, remove the n-th node from the end of list and return its head.

**Example:**

Given linked list: 1->2->3->4->5, and n = 2.

> After removing the second node from the end, the linked list becomes 1->2->3->5.

**Note:**

> Given n will always be valid.

题目大意是删除单链表倒数第N个节点，并假设N是合法的。

双指针是单链表问题常用的方法。如果要删除第N个节点，可以让一个指针先向前走N步，然后另一个指针从头开始，直到第一个指针走到最后一个节点。则另一个指针所在位置的下一个位置即为需要删除的节点。这个题目比较简单，但是需要注意待删除节点如果是第一个节点这种情况。

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = slow = head
        # fast指针向前走N步
        for _ in range(n):
            fast = fast.next
        # 如果fast指针为空，说明待删除节点是第一个节点
        if fast is None:
            return head.next
        
        # 两个指针同时开始走
        while fast.next is not  None:
            fast = fast.next
            slow = slow.next
        # 删除下一个节点
        slow.next = slow.next.next
        return head
```