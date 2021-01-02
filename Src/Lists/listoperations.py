class Node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

    def __str__(self):
        ret=""
        cur=self
        while cur:
            ret+=str(cur.val)+"->"
            cur=cur.next
        ret+="None"
        return ret

def insertAtHead(head,val):
    node=Node(val)
    if not head:
        head=node
    node.next=head
    head=node

def insertAtTail(head,val):
    node=Node(val)
    if not head:
        return node
    cur=head
    while cur.next:
        cur=cur.next
    cur.next=node
    return head

a=Node(1)
b=Node(2,a)
c=Node(10,b)
d=Node(5,c)
e=Node(8,d)
f=Node(5,e)
head=Node(3,f)

print(head)
h1=None
insertAtHead(h1,5)
print(h1)
insertAtHead(head,5)
print(head)
#print(insertAtTail(head,5))
