# LeetCode 876. Middle of the linked list

class Solution:
    def middleNode(self, head):
        ahead = head

        while ahead and ahead.next:
            ahead = ahead.next.next
            head = head.next
        return head

# this problem can be solved using two pointers technique
# one pointer moves two steps at a time and the other moves one step at a time
# when the first pointer reaches the end of the list, the second pointer will be at the middle
# its like a table game where one player moves two steps and the other moves one step        