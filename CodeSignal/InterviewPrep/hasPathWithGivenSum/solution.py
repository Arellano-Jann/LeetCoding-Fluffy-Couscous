#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def solution(t, s):
    def dfs(current_sum, subtree):
        if not subtree: # if it reaches a leaf and cannot go further, it there is no path within this subtree path that adds up to sum 's'
            return False
        if (current_sum + subtree.value == s) and not subtree.left and not subtree.right: # if leaf node and the addition of all the nodes (in a single path) up to the leaf is equal to the current sum we are finding then return true
            return True
        subtree_value = subtree.value
        return dfs(current_sum + subtree_value, subtree.left) or dfs(current_sum + subtree_value, subtree.right)
    return dfs(0, t)