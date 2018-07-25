class Solution:
    def isValid(self, s):
        d = {'{':'}', '(':')', '[':']'}
        stack = []
        for c in s:
            if c in d:
                stack.append(c)
            elif not stack or c != d[stack.pop()]:
                return False
        return not stack
