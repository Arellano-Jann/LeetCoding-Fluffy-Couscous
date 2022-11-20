# https://leetcode.com/problems/koko-eating-bananas/description/
def minEatingSpeed(piles: List[int], H: int) -> int:
    def valid(num): # check if the number we're at is a valid solution. in other words, checks if the current eating speed is valid for the amount of hours that we are given
        # this ^ number could also be called 'k' as in the problem statement
        # -(-a//b) # ceiling function found here https://stackoverflow.com/questions/17140332/implementing-ceil-function-without-using-if-else
        total = 0
        for pile in piles:
            total += (-(-pile // num)) # how many hours it takes to devour the current pile with the current eating speed
        return total <= H


    left, right = 1, max(piles) # left and right pointers, minimum and maximum values respectively
    res = -1
    while left <= right: # needs to be <= because if left and right are equal to each other (edge case that the max is at left or right) then it breaks and returns the default res value (which is -1 in this case)
        mid = (left + right) // 2
        if valid(mid):
            right = mid - 1 # value no longer in the right of mid. but it's inclusive bc it's a possible solution to the set?
            res = mid
        else:
            left = mid + 1 # value no longer in the left of mid
    return res

minEatingSpeed([30,11,23,4,20], 5)