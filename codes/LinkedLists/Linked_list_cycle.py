# Leetcode 141. Linked List Cycle

class Solution:
    def hasCycle(self, head) -> bool:
        slow = head
        fast = head 

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next

            if slow == fast:
                return True
            
        
        return False

# this problem can be solved using two pointers technique
# similar to the middle of the linked list problem
# when the first pointer meets the second pointer, it means there is a cycle
# if the first pointer reaches the end of the list, it means there is no cycle


        