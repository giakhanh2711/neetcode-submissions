class Solution:
    def isValid(self, s: str) -> bool:
        paren_dict = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = []
        for c in s:
            if c in paren_dict:
                stack.append(c)
            elif len(stack) > 0 and paren_dict[stack[-1]] == c:
                stack.pop()
            else:
                return False
        
        return len(stack) == 0