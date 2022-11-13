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