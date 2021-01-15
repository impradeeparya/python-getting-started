# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):

        list_length = 0
        current_head = head
        while current_head is not None:
            current_head = current_head.next
            list_length += 1

        if list_length == n:
            head = head.next
        elif list_length > n:
            nthNode = head
            current_head = head
            while n > 0:
                if current_head is None:
                    return
                current_head = current_head.next
                n -= 1

            prev_node = None
            while current_head is not None:
                current_head = current_head.next
                prev_node = nthNode
                nthNode = nthNode.next
            prev_node.next = nthNode.next
            nthNode.next = None

        return head


def printLinkedList(node):
    while node is not None:
        print(node.val, end=' ')
        node = node.next
    print()


head = ListNode(1)
current_node = head
for value in range(2, 1):
    node = ListNode(value)
    current_node.next = node
    current_node = node

printLinkedList(head)
updated_list = Solution().removeNthFromEnd(head, 2)
printLinkedList(updated_list)
