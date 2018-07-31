# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Solution for Add Two Numbers
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        sumList = None
        tmpNode = None
        sumTmp = 0
        while l1 != None and l2 != None:
            if sumList == None:
                tmpNode = ListNode(0)
                sumList = tmpNode
            else:
                tmpNode.next = ListNode(0)
                tmpNode = tmpNode.next

            sumTmp = l1.val + l2.val + sumTmp
            tmpNode.val = sumTmp % 10
            sumTmp = sumTmp // 10
            l2 = l2.next
            l1 = l1.next

        copyNode = None
        if l2 != None:
            copyNode = l2
        if l1 != None:
            copyNode = l1

        while copyNode != None:
            sumTmp = copyNode.val + sumTmp
            tmpNode.next = ListNode(0)
            tmpNode = tmpNode.next

            tmpNode.val = sumTmp % 10
            sumTmp = sumTmp // 10
            copyNode = copyNode.next
        if sumTmp != 0:
            tmpNode.next = ListNode(sumTmp)
        return sumList
    