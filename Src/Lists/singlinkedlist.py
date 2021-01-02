class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
    def __str__(self):
        s=""
        cur=self
        while cur:
            s += str(self.val) + " -> "
            cur=cur.next
        return s

def prepend(target,head):
    newnode=ListNode(target)
    newnode.next=head
    head=newnode
    return head

def remove(target,head):
    if not head:
        return head
    prev,cur=None,head
    while cur and cur.val != target:
        prev=cur
        cur=cur.next
    if cur is head:
        head=head.next
    else:
        prev.next=cur.next
    return head
