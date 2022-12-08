def minDepth(root):
    depth = 0
    q = [root]
    while True:
        depth += 1
        for elem in q:
            if elem.right is elem.left:
                return depth
        q = [c for n in q for c in [n.left, n.right] if c]
