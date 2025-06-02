class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def print_linked_list(head):
    result = []
    current = head
    while current:
        result.append(current.value)
        current = current.next
    print(result)

def build_linked_list(values):
    if not values:
        return None
    
    head = Node(values[0])
    current = head  
    
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    
    return head


def find_middle(head):
    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def merge(l1, l2):
    head = Node()
    tail = head

    while l1 and l2:
        if l1.value < l2.value:
            tail.next = l1
            l1 = l1.next 
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    if l2:
        tail.next = l2
    
    return head.next

def merge_sort(head):
    if not head or not head.next:
        return head
    
    mid = find_middle(head)
    after_mid = mid.next
    mid.next = None 

    left = merge_sort(head)
    right = merge_sort(after_mid)

    return merge(left, right)



values = [10, 7, 8, 9, 1, 5]
head = build_linked_list(values)

print_linked_list(head)

sorted_head = merge_sort(head)

print_linked_list(sorted_head)

# Time Complexity: O(n log n)
# Space Complexity: O(n)