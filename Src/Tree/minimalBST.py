'''
sorted array
create a bst with minimal height
'''
class Node:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class BST:
    def __init__(self,val):
        self.root=Node(val)

    def insert(self,val):
        self._insert_node(self.root,val)

    def _insert_node(self,cur,val):
        if not cur:
            return
        newnode=Node(val)
        if not cur.left and cur.val > val:
            cur.left=newnode
            return
        if not cur.right and cur.val < val:
            cur.right=newnode
            return
        if cur.val > val:
            self._insert_node(cur.left,val)
        if cur.val < val:
            self._insert_node(cur.right,val)

    def __str__(self):
        return self._inorder_traverse(self.root)

    def _inorder_traverse(self,node):
        if not node:
            return ""
        return self._inorder_traverse(node.left) + "," + str(node.val) + "," + self._inorder_traverse(node.right)

def mimialheight(arr):
    n=len(arr)
    mid=n//2
    root=BST(arr[mid])
    for elem in arr[:mid] + arr[mid+1:]:
        root.insert(elem)
    return root

arr=[1,2,3,3,4,5,6,7]
print(mimialheight(arr))
