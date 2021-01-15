# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        head = None
        if l1 is None:
            return l2
        elif l2 is None:
           return l1
        elif l1.val <= l2.val:
            head = l1
            l1 = l1.next
            head.next = None
        else:
            head = l2
            l2 = l2.next
            head.next = None
        current_head = head

        while l1 is not None and l2 is not None:
            if l1.val == l2.val:
                current_head.next = l1
                current_head = current_head.next
                l1 = l1.next
                current_head.next = l2
                current_head = current_head.next
                l2 = l2.next
                current_head.next = None
            elif l1.val < l2.val:
                current_head.next = l1
                current_head = current_head.next
                l1 = l1.next
                current_head.next = None
            else:
                current_head.next = l2
                current_head = current_head.next
                l2 = l2.next
                current_head.next = None

        if l1 is not None:
            current_head.next = l1
        else:
            current_head.next = l2

        return head


def printLinkedList(node):
    while node is not None:
        print(node.val, end=' ')
        node = node.next
    print()


def generateList(head):
    for value in range(2, 5):
        node = ListNode(value)
        head.next = node
        head = node


l1 = ListNode(1)
generateList(l1)
printLinkedList(l1)

l2 = ListNode(1)
generateList(l2)
printLinkedList(l1)

l3 = Solution().mergeTwoLists(l1, l2)
printLinkedList(l3)
