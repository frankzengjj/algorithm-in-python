class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
         
def LCA(root, p, q):
    pathP = findPath(root, p)
    pathQ = findPath(root, q)
    return list(set(pathP).intersection(pathQ))[0]
    
def findPath(root, x):
    path = []
    if root is None:
        return path
    if root.val == x:
        path.append(root.val)
        return path
    
    leftTree = findPath(root.left, x)
    if leftTree:
        leftTree.append(root.val)
        return leftTree
    rightTree = findPath(root.right, x)
    if rightTree:
        rightTree.append(root.val)
        return rightTree
    return path
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(7)
print(LCA(root,2,3))
