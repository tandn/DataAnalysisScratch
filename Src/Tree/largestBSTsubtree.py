class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

'''
Input: [10,5,15,1,8,null,7]

   10
   / \
  5  15
 / \   \
1   8   7

Output: 3
Explanation: The Largest BST Subtree in this case is the highlighted one.
             The return value is the subtree's size, which is 3.

'''
def largestBSTsubtree(root):
    if not root:
        return search(root)
    else:
        return root

def search(node):
    pass

def search_bst(node):
    if not node:
        return 0
    if node.left is node.right: # a leaf is bst
        return 1
    if (node.left and node.val < node.left.val) or (node.right and node.val > node.right.val):
        return -1
    left= search_bst(node.left)
    right=search_bst(node.right)
    if left == -1 or right == -1:
        return -1

    return 1 + left + right

tree=TreeNode(10,TreeNode(5,TreeNode(1),TreeNode(108)),TreeNode(15,None,TreeNode(7)))
print(search_bst(tree))
print(search_bst(TreeNode(5,TreeNode(1),TreeNode(8))))
