class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l1_number = 0
        power = 0
        node = l1
        while node is not None:
            l1_number = l1_number + (10 ** power) * node.val
            power += 1
            node = node.next

        l2_number = 0
        power = 0
        node = l2
        while node is not None:
            l2_number = l2_number + (10 ** power) * node.val
            power += 1
            node = node.next

        total = l1_number + l2_number
        if total > 0:
            reverse_sum = None
        else:
            reverse_sum = ListNode()
        while total > 0:
            digit = total % 10
            new_node = ListNode(digit)
            if reverse_sum is None:
                reverse_sum = new_node
                current_node = reverse_sum
            else:
                current_node.next = new_node
                current_node = new_node
            total = int(total / 10)

        return reverse_sum


l1_array = [4, 3]
l1 = ListNode(2, None)
node = None
for index in range(len(l1_array)):
    if node is None:
        node = l1
    new_node = ListNode(l1_array[index], None)
    node.next = new_node
    node = new_node

l2_array = [6, 4]
l2 = ListNode(5, None)
node = None
for index in range(len(l2_array)):
    if node is None:
        node = l2
    new_node = ListNode(l2_array[index], None)
    node.next = new_node
    node = new_node

solution = Solution()
sum = solution.addTwoNumbers(l1, l2)
while sum is not None:
    print(sum.val)
    sum = sum.next
