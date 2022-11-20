# https://leetcode.com/problems/binary-search/description/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        target_index = -1
        while left <= right:
            mid = (left + right) // 2
            left_element = nums[left]
            right_element = nums[right]
            mid_element = nums[mid]
            if nums[mid] == target: # this in turn makes the bottom 2 statements need to be mid-1 and mid+1 because we KNOW it's not mid from this statement alone.
                return mid # in other cases of binary search algorithms that you would use in a problem, you would need to save a target_index element or something of the sort since you are often trying to get the most optimal solution
            elif target < mid_element: # leave only the left side. right side is no longer considered
                right = mid - 1
            else: # leave only the right side. left side is no longer being considered
                left = mid + 1
        return -1
