class Node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
    def __str__(self):
        cur=self
        ret=""
        while cur:
            ret+= str(cur.val) + " -> "
            cur=cur.next
        return ret + " None "

def partition(head,val):
    ret=Node()
    cur,prev,traverse=ret,ret,head
    while traverse:
        node=Node(traverse.val)
        if traverse.val >= val:
            node.next=cur.next
            cur=node
        if traverse.val < val:
            prev.next=node

        traverse=traverse.next
    return ret.next

a=Node(1)
b=Node(2,a)
c=Node(10,b)
d=Node(5,c)
e=Node(8,d)
f=Node(5,e)
head=Node(3,f)

print(head)
print(partition(head,5))
