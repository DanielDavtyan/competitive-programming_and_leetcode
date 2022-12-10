def maxDepth(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    return max(maxDepth(root.left) + 1, maxDepth(root.right) + 1)

