class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        prev = head
        while current and current.next:
            current = current.next.next
            prev = prev.next
            if current == prev:
                return True
    
        return False
