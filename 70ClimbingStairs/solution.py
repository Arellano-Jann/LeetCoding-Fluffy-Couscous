# True DP. Use last 2 results to calculate current. Fibonacci Sequence Alias
def climbStairs(self, n: int) -> int:
    if n <= 3:
        return n
    right, left = 1, 1
    for x in range(n-1): # n-1 because it takes 1 step to go from n to n (if that makes sense). basically, left already takes care of it.
        prev_left = left
        left = right
        right += prev_left
    return right

# Recursive. Too slow.
def Recursive1climbStairs(self, n: int) -> int:
    def dp(current):
        if current == 0 or current == 1:
            return 1
        return dp(current-1) + dp(current-2)
    
    return dp(n)

# Recursive Second Implementation
def Recursive2climbStairs(self, n: int) -> int:
    def recurse(current):
        if current == n:
            return 1
        if current >= n:
            return 0
        return recurse(current+1) + recurse(current+2)
    
    return recurse(0)


# Memoization. Too slow
def Memo1climbStairs(self, n: int) -> int:
    cache = {}
    def dp(current):
        if current in cache:
            return cache[current]
        if current == 1 or current == 0:
            return 1
        return dp(current-1) + dp(current-2)
    
    return dp(n)

# Memoization second implementation.
def Memo2climbStairs(self, n: int) -> int:
    cache = {}
    def dp(current):
        if current in cache:
            return cache[current]
        if current == n:
            return 1
        if current >= n:
            return 0
        return dp(current+1) + dp(current+2)
    
    return dp(0)