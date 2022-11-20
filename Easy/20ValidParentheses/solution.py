# https://leetcode.com/problems/valid-parentheses/description/
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            '{' : '}',
            '[' : ']',
            '(' : ')',
        }
        for char in s:
            if char in mapping: # if there is an opening bracket to the closing bracket
                stack.append(char)
            else:
                if not stack or mapping[stack[-1]] != char: # if the closing bracket doesn't correctly close the last opening bracket or there is no directly correlating opening bracket to the closing bracket
                    return False
                else:
                    stack.pop() # if there is an open to a close, then "make a pair" and pop the stack and move on
        return True if not stack else False # return True if there are no leftover brackets in the stack
