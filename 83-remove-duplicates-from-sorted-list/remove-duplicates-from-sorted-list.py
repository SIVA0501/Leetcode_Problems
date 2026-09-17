class Solution:
    def deleteDuplicates(self, head):
        c = head
        while c and c.next:
            if c.val == c.next.val:
                c.next = c.next.next
            else:
                c = c.next
        return head