#Easy

# Definition for singly-linked ListNode.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseListNode(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    
if __name__ == "__main__":
    s = Solution()
    # Example usage:
    # Creating a linked ListNode: 1 -> 2 -> 3 -> None
    head = ListNode(1, ListNode(2, ListNode(3)))
    
    # Reversing the linked ListNode
    reversed_head = s.reverseListNode(head)
    
    # Printing the reversed linked ListNode
    while reversed_head:
        print(reversed_head.val, end=" -> ")
        reversed_head = reversed_head.next
    print("None")