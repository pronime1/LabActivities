class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#In-Order
def inorder_traversal (roots):
    if roots:
        inorder_traversal(roots.left)
        print(roots.value, end=" ")
        inorder_traversal(roots.right)
#Pre-Order
def preorder_traversal(roots):
    if roots:
        print(roots.value, end=" ")
        preorder_traversal(roots.left)
        preorder_traversal(roots.right)
#Post-Order
def postorder_traversal(roots):
    if roots:
        postorder_traversal(roots.left)
        postorder_traversal(roots.right)
        print(roots.value, end=" ")

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.left.left = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print("In-Order Traversal")
inorder_traversal(root)
print("\nPre-Order Traversal")
preorder_traversal(root)
print("\nPost-Order Traversal")
postorder_traversal(root)
