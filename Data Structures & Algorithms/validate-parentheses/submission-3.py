class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == " " or ch.isdigit():
                continue
            if ch == '{' or ch == '(' or ch == '[':
                stack.append(ch)
            if (ch == ')' or ch == '}' or ch == ']'):
                if (len(stack) == 0):
                    return  False
                top = stack[-1]
                if ( (ch == ')' and top != '(') or (ch == '}' and top != '{') or (ch == ']' and top != '[')):
                    return False
                stack.pop()
        if (len(stack) != 0):
            return False
        return True