#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def solution(t, s):
    def dfs(current_sum, subtree):
        if not subtree:
            return False
        if (current_sum + subtree.value == s) and not subtree.left and not subtree.right:
            return True
        subtree_value = subtree.value
        return dfs(current_sum + subtree_value, subtree.left) or dfs(current_sum + subtree_value, subtree.right)
    return dfs(0, t)