class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def averageOfLevels(root):
    q = ["#"]
    results = []
    q.append(root)
    while len(q) - 1:
        if q[0] == "#":
            q.pop(0)
            results.append(numerical_mean(q))
            q.append("#")
        else:
            if q[0].left:
                q.append(q[0].left)
            if q[0].right:
                q.append(q[0].right)
            q.pop(0)


    return results


def numerical_mean(q):
    s = 0
    for i in q:
        s += i.val
    return s / len(q)

# Pythonic BFS solution
def averageOfLevels(root):
    ans = []
    lvl = [root]
    while lvl:
        ans.append(sum(n.val for n in lvl) / float(len(lvl)))
        lvl = [c for n in lvl for c in [n.left, n.right] if c]
    return ans