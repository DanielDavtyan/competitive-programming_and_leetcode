def diameterOfBinaryTree(root):
    result = 0

    def dfs(root):
        global result
        if not root:
            return -1
        right = dfs(root.right)
        left = dfs(root.left)
        result = max(result, 2 + right + left)
        return 1 + max(left, right)
    dfs(root)
    return result




