# Optimal Iterative Solution
def rob(self, nums: List[int]) -> int:
    left, right = 0, 0
    for i in range(len(nums)):
        max_rob = max(nums[i] + left, right)
        left = right
        right = max_rob
    return right