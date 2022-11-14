# Optimal Iterative Solution
def rob(self, nums: List[int]) -> int:
    left, right = 0, 0
    for i in range(len(nums)):
        max_rob = max(nums[i] + left, right)
        left = right
        right = max_rob
    return right

# Memoization. Stores DP
def rob(self, nums: List[int]) -> int:
    dp = [-1] * (len(nums) + 1)
    def rob2(pos):
        if dp[pos] >= 0:
            return dp[pos]
        if pos < 0:
            return 0
        dp[pos] = max(rob2(pos-2) + nums[pos], rob2(pos-1))
        return dp[pos]
    return rob2(len(nums)-1)

# Memoization using Cache decorator
def rob(self, nums: List[int]) -> int:
    @lru_cache(None)
    def rob2(pos):
        if pos < 0:
            return 0
        return max(rob2(pos-2) + nums[pos], rob2(pos-1))
            
    return rob2(len(nums)-1)

# Recursive Solution
# Rob(pos) = max( Rob(pos-2) + nums[pos], Rob(pos-1) )
# so maximum between the current AND the second to previous houses accumulated or the last house and everything accumulated
def rob(self, nums: List[int]) -> int:
    def rob2(pos):
        if pos < 0:
            return 0
        return max(rob2(pos-2) + nums[pos], rob2(pos-1))
    return rob2(len(nums)-1)