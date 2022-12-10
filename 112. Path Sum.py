def hasPathSum(root, targetSum):
    def recursive_sum(node, current_sum):
        if not node:
            return False
        current_sum += node.val
        if not node.left and not node.right:
            return current_sum == targetSum
        return recursive_sum(node.right, current_sum) or recursive_sum(node.left, current_sum)
    return recursive_sum(root, 0)
