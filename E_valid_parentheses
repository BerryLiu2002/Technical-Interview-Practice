"""
Question Name: 20. Valid Parentheses
Difficulty: Easy
Category: Stack
Link: https://leetcode.com/problems/valid-parentheses/
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {")":"(", "]":"[", "}":"{"}
        for part in s:
            if part in match:
                if not stack or stack.pop() != match[part]:
                    return False
            else:
                stack.append(part)
        return len(stack) == 0